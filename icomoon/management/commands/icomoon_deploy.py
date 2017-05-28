# -*- coding: utf-8 -*-
"""
TODO:
    * Add a list option to only list defined webfont in settings;
"""
import json, os, shutil, tempfile, zipfile

from optparse import OptionValueError, make_option

from django.conf import settings
from django.core.management.base import CommandError, BaseCommand
from django import template
from django.template.loader import render_to_string

from icomoon.store import WebfontStore
from icomoon.utils import IcomoonSettingsError, extend_webfont_settings


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        #make_option("--name", dest="webfont_name", default=None, help="Webfont name as defined into settings.ICOMOON_WEBFONTS, this is required"),
    )
    help = "Icomoon CLI to deploy an Icomoon webfont from downloaded ZIP archive."


    def add_arguments(self, parser):
        parser.add_argument('webfont_name', nargs='?', default='Default', help="Webfont key name from 'settings.ICOMOON_MANIFEST_FILEPATH'. (default: %(default)s)")
        parser.add_argument('archive_path', nargs='?', default='icomoon.zip', help="ZIP archive from icomoon to deploy. (default: %(default)s)")

    def handle(self, *args, **options):
        self.webfont_name = options['webfont_name']
        self.archive_path = options['archive_path']
        self.css_templatepath = options.get('css_template', settings.ICOMOON_CSS_TEMPLATE)
        self.requirements = options.get('requirements', settings.ICOMOON_ARCHIVE_REQUIREMENT)
        self.verbosity = int(options.get('verbosity'))

        self._info("* Using webfont name: {}", self.webfont_name)

        # Get the current manifest for given webfont name
        if self.webfont_name not in settings.ICOMOON_WEBFONTS:
            choices = "', '".join(settings.ICOMOON_WEBFONTS.keys())
            self._error("There is no defined webfont name '{name}' in your settings, choices are: '{choices}'", name=self.webfont_name, choices=choices)

        try:
            self.webfont_settings = extend_webfont_settings(settings.ICOMOON_WEBFONTS[self.webfont_name])
        except IcomoonSettingsError as e:
            self._error("Invalid webfont settings for '{}': {}", self.webfont_name, e.value)

        self._info("* Using webfont font dir: {}", self.webfont_settings['fontdir_path'])

        self.deploy()
        self._info("Finished !")

    def print_output(self, msg, *args, **kwargs):
        self.stdout.write(msg.format(*args, **kwargs))

    def _error(self, msg, *args, **kwargs):
        raise CommandError(msg.format(*args, **kwargs))

    def _debug(self, msg, *args, **kwargs):
        if self.verbosity >= 3:
            self.print_output(msg, *args, **kwargs)

    def _warning(self, msg, *args, **kwargs):
        if self.verbosity >= 2:
            self.print_output(msg, *args, **kwargs)

    def _info(self, msg, *args, **kwargs):
        if self.verbosity >= 1:
            self.print_output(msg, *args, **kwargs)

    def deploy(self):
        """
        Open a ZIP archive, validate requirements then deploy the webfont into
        project static files
        """
        self._info("* Opening archive: {}", self.archive_path)
        if not os.path.exists(self.archive_path):
            self._error("Given path does not exists: {}", self.archive_path)

        with zipfile.ZipFile(self.archive_path, 'r') as zip_archive:
            font_dir = self.requirements['font_dir']+'/'
            allowed_extensions = ['.'+item for item in self.requirements['extensions']]
            members = [member for member in zip_archive.namelist()]

            if settings.ICOMOON_MANIFEST_FILENAME not in members:
                raise self._error("Icomoon archive must contain a JSON manifest '{}'", settings.ICOMOON_MANIFEST_FILENAME)

            if font_dir not in members:
                raise self._error("Icomoon archive must contain the font directory '{}'", font_dir)

            # Scan for supported font files
            font_files = []
            for item in members:
                # Dont catch the font_dir itself nor sub directories, just files with allowed extensions
                if item.startswith(font_dir) and not item.endswith('/') and os.path.splitext(item)[-1] in allowed_extensions:
                    font_files.append(item)

            if not font_files:
                self._error("Font dir does not contain any supported format: {}", ', '.join(allowed_extensions))
            else:
                self._debug("* Finded font files in archive: {}", ', '.join(font_files))

            # Extract files from archive
            tmp_container, css_content = self.extract(zip_archive, font_files)

        # Install files
        self.install(tmp_container, font_dir, css_content)

    def extract(self, zip_archive, font_files):
        """
        Extract files to install
        """
        # Get a temp directory
        tmp_container = tempfile.mkdtemp(prefix='icomoon-tmp')
        self._debug("* Temporary dir for extracted archive: {}", tmp_container)

        # Extract manifest to temp directory
        zip_archive.extract(settings.ICOMOON_MANIFEST_FILENAME, tmp_container)
        # Then the font files
        for item in font_files:
            zip_archive.extract(item, tmp_container)

        # Get manifest for icon map
        webfont_store = WebfontStore(settings.ICOMOON_MANIFEST_FILENAME)
        webfont_store.get(self.webfont_name, {
            'fontdir_path': tmp_container,
        })
        icons = webfont_store.get_manifests()[self.webfont_name]
        #print json.dumps(icons, indent=4)

        # Render CSS icon part
        css_content = self.render_css(self.css_templatepath, icons)

        return tmp_container, css_content

    def render_css(self, template_path, icons):
        """
        Render CSS template to contain the icons stylesheet map
        """
        return render_to_string(template_path, {'icons': icons})

    def install(self, tmp_container, font_tmpdir, css_content):
        """
        Install extracted files and builded css
        """
        # Write builded css file to its destination
        with open(self.webfont_settings['csspart_path'], 'w') as css_file:
            css_file.write(css_content)

        # Clean previous font dir
        if os.path.exists(self.webfont_settings['fontdir_path']):
            shutil.rmtree(self.webfont_settings['fontdir_path'])
        font_srcdir = os.path.join(tmp_container, font_tmpdir)
        self._debug("* Installing font")
        self._debug("  - From: {}", font_srcdir)
        self._debug("  - To: {}", self.webfont_settings['fontdir_path'])

        shutil.copytree(font_srcdir, self.webfont_settings['fontdir_path'])

        # Copy new manifest into font dir
        manifest_src = os.path.join(tmp_container,
                                    settings.ICOMOON_MANIFEST_FILENAME)
        self._debug("* Installing manifest")
        self._debug("  - From: {}", manifest_src)
        self._debug("  - To: {}", self.webfont_settings['fontdir_path'])
        shutil.copy(manifest_src, self.webfont_settings['fontdir_path'])

        # Remove temp directory when all is done
        self._debug("* Removing temporary dir")
        shutil.rmtree(tmp_container)

