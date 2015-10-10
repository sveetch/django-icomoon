.. _Django: https://www.djangoproject.com/
.. _Icomoon: http://icomoon.io/
.. _django-braces: http://django-braces.readthedocs.org/en/v1.3.1/

Django Icomoon
==============

A `Django`_ app to display an icon gallery, listing all defined icons in Zip archive you downloaded from `Icomoon`_.

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

Each item is a tuple of three elements, respectively:

Name
    Displayed webfont name in Gallery, also used in the command line tool so you should keep it 'slug' compatible (no spaces, no special character).
Font directory
    Path to the directory where belong these webfont font files.

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

Deployment from command line
----------------------------

Put the downloaded ZIP archive on your server then simply use the command line: ::

    django-instance icomoon_deploy Default icomoon.zip

Where the first argument is the webfont name (defined in your settings, see `Webfonts and manifests`_) to use and the second argument is the path to your download archive.

The tool will validate the archive content structure then if all requirements are meets (a JSON manifest and at least one supported font format) it will deploy the archive content to defined webfont paths in settings. 

The manifest is used to build a css file where all icon selectors are defined, so you can import it to directly use your icons.

Finally the manifest is installed in the same directory than font files.