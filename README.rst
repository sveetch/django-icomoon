.. _Django: https://www.djangoproject.com/
.. _Icomoon: http://icomoon.io/
.. _django-braces: http://django-braces.readthedocs.org/en/v1.3.1/

Django Icomoon
==============

A `Django`_ app to deploy downloaded wefonts from `Icomoon`_ and display them in a gallery.

Links
*****

* Download his `PyPi package <https://pypi.python.org/pypi/django-icomoon>`_;
* Clone it on his `Github repository <https://github.com/sveetch/django-icomoon>`_;

Requires
********

* `Django`_ >= 1.4;
* `django-braces`_ >= 1.2.0,<1.4;

Install
*******

.. warning::
        Since ``0.3.0`` lots of settings have changed in a backward incompatible way, you shoud totally redo them when updating.

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
    (Required) Absolute path to the webfont directory.
csspart_path
    (Optional) Absolute path where will be written the css part containing webfont icons.

Urls
----

Just mount its urls in your main ``urls.py`` : ::

    urlpatterns = patterns('',
        ...
        (r'^icomoon/', include('icomoon.urls', namespace='icomoon')),
        ...
    )

Templates
---------

This at your responsability to load the webfont into your website templates, this app won't do it for you.

Note that shipped templates in ``templates/icomoon/`` are written using Foundation5 components and inherits from a ``templates/skeleton.html`` that you have to create yourself. You better gives an eye to this app templates to correctly integrate them into your project.

Usage
*****

Gallery
-------

When it's installed you could reach the webfont gallery from ``/icomoon/``.

The gallery display all defined icons in the manifest, giving the CSS classname, the unicode codepoint and the UTF-8 code.

Deployment
----------

Put the downloaded ZIP archive on your server then simply use the command line: ::

    ./manage.py icomoon_deploy Default icomoon.zip

The first argument is the webfont key name (defined in your settings, see `Webfonts and manifests`_) to use and the second argument is the path to your downloaded archive to deploy: ::

    ./manage.py icomoon_deploy [Webfont name] [Zip archive path]

The tool will validate the archive content structure then if all requirements are meets (a JSON manifest and at least one supported font format) it will deploy the archive content to defined path (``fontdir_path``) in webfont settings. 

Optionaly, if a path (``csspart_path``) is defined for, the manifest will be used to build a css file where all icon selectors are defined, so you can import it to directly use your icons.

Finally the manifest is installed in the same directory than font files.