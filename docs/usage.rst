.. _intro_usage:

=====
Usage
=====

Gallery
-------

When it's installed you can reach the webfont gallery at ``/icomoon/``.

The gallery display all defined icons in the manifest, giving the CSS classname,
unicode codepoint and UTF-8 code for each defined icon.

Deployment
----------

Put the downloaded Icomoon ZIP archive at root of your project then simply use
the command line: ::

    ./manage.py icomoon_deploy Default icomoon.zip

The first argument is the webfont key name (defined in your settings,
see :ref:`install_manifest`) to use and the second argument is the path to
your downloaded archive to deploy: ::

    ./manage.py icomoon_deploy [Webfont name] [Zip archive path]

Default values for these two arguments are respectively ``Default``
and ``icomoon.zip``, if they match your webfont settings you don't need to give
them: ::

    ./manage.py icomoon_deploy

The tool will validate the archive content structure then if all requirements
are meets (a JSON manifest and at least one supported font format) it will
deploy the archive content to defined path (``fontdir_path``) in webfont
settings.

Optionaly, if ``csspart_path`` is defined, the manifest will be used to build
a css file where all icon selectors are defined, so you can import it to
directly use your icons. This option use ``ICOMOON_CSS_TEMPLATE`` settings to
find template to use to build this file. Default value
is ``icomoon/icon_map.css`` but there is also a
template ``icomoon/icon_map.scss`` that will produce a Sass file with icons
exposed as variables and mixin to include their classes.

Finally the manifest is installed in the same directory than font files.
