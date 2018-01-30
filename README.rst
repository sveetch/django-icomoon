.. _Django: https://www.djangoproject.com/
.. _Icomoon: http://icomoon.io/
.. _django-braces: http://django-braces.readthedocs.org/

Django Icomoon
==============

A `Django`_ app to deploy downloaded wefonts from `Icomoon`_ and display them in a gallery.

Links
*****

* Download his `PyPi package <https://pypi.python.org/pypi/django-icomoon>`_;
* Clone it on his `Github repository <https://github.com/sveetch/django-icomoon>`_;

Requires
********
* six;
* `Django`_ >= 1.8;
* `django-braces`_ >= 1.2.0;

Install
*******

First install the package ::

    pip install django-icomoon

Add it to your installed Django apps in settings : ::

    INSTALLED_APPS = (
        ...
        'icomoon',
        ...
    )

Import default app settings: ::

    from icomoon.settings import *

Default behavior require users to be authenticated to view the gallery, if you want to open it for anonymous define the following setting: ::

    ICOMOON_PRIVATE = False

Webfonts and manifests
----------------------


Now you must define at least one webfont in your project settings like this: ::

    ICOMOON_MANIFEST_FILEPATH = {
        'Default': {
            'fontdir_path': '/home/work/myproject/webapp_statics/fonts/default',
            'csspart_path': '/home/work/myproject/webapp_statics/css/icomoon_icons.scss'
        },
    }

Each website entry is a dict containing the following values:

fontdir_path
    (Required) Absolute path to the webfont directory. It will be created with Manifest file and font files on each deploy.
csspart_path
    (Optional) Absolute path where will be written the css part containing webfont icons.

Urls
----

Just mount its urls in your main ``urls.py`` : ::

    urlpatterns = [
        ...
        url(r'^icomoon/', include('icomoon.urls', namespace='icomoon')),
        ...
    ]

Templates
---------

This at your responsability to load the webfont into your website templates, this app won't do it for you.

Note that shipped templates in ``templates/icomoon/`` are written using Foundation5 components and inherits from a ``templates/skeleton.html`` that you have to create yourself. You better gives an eye to this app templates to correctly integrate them into your project.

Usage
*****

Gallery
-------

When it's installed you can reach the webfont gallery at ``/icomoon/``.

The gallery display all defined icons in the manifest, giving the CSS classname, unicode codepoint and UTF-8 code for each defined icon.

Deployment
----------

Put the downloaded ZIP archive on your server then simply use the command line: ::

    ./manage.py icomoon_deploy Default icomoon.zip

The first argument is the webfont key name (defined in your settings, see `Webfonts and manifests`_) to use and the second argument is the path to your downloaded archive to deploy: ::

    ./manage.py icomoon_deploy [Webfont name] [Zip archive path]

Default values for these two arguments are respectively ``Default`` and ``icomoon.zip``, so if they match your webfont settings, you don't need to give them: ::

    ./manage.py icomoon_deploy

The tool will validate the archive content structure then if all requirements are meets (a JSON manifest and at least one supported font format) it will deploy the archive content to defined path (``fontdir_path``) in webfont settings.

Optionaly, if ``csspart_path`` is defined, the manifest will be used to build a css file where all icon selectors are defined, so you can import it to directly use your icons. This option use ``ICOMOON_CSS_TEMPLATE`` settings to find template to use to build this file. Default value is ``icomoon/icon_map.css`` but there is also a template ``icomoon/icon_map.scss`` that will produce a Sass file with icons exposed as variables and mixin to include their classes.

Finally the manifest is installed in the same directory than font files.

History
*******

Version 1.1.0 - 2018/01/30
--------------------------

* Fixed compatibiliy with django>=1.10 in management command, close #9;
* Added missing semicolon on pseudo element classes in CSS template;
* Added ``icon_map.scss`` template to create an useful Sass file instead of simple CSS classes, close #5;

Version 1.0.0 - 2017/05/29
--------------------------

* Added tests structure;
* Covered all code with tests except for the management command;
* Confirmed support for Django 1.8 to Django 1.11, Python 2 and Python 3.5 through 'tox';

Version 0.4.0 - 2016/04/06
--------------------------

* Dropped support for Django <= 1.7;
* Fixed command line arguments for Django == 1.8;

Version 0.3.1 - 2015/10/24
--------------------------

* Lowering down minimal 'django-braces' dependancy, better classifiers for Django versions in setup.py;

Version 0.3.0 - 2015/10/11
--------------------------

* Implemented command line to deploy webfont from download ZIP on Icomoon, contains many backward incompatible settings, this is related to issue #2;

