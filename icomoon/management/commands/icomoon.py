# -*- coding: utf-8 -*-
"""
...
"""
import json, os

from optparse import OptionValueError, make_option

from django.conf import settings
from django.core.management.base import CommandError, BaseCommand

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        #make_option("--manifest", dest="manifest_path", default=None, help="Webfont manifest in JSON that comes within the download archive from Icomoon. Commonly a 'selection.json' file"),
    )
    help = "Icomoon CLI"

    def handle(self, *args, **options):
        if len(args) != 0:
            raise CommandError("Command doesn't accept any arguments")
        
        self.manifest_path = options.get('manifest_path')
        self.verbosity = int(options.get('verbosity'))
        
        print "Nothing here yet."
        
