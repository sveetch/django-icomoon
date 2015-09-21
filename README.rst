.. _Django: https://www.djangoproject.com/
.. _Icomoon: http://icomoon.io/

Django Icomoon
==============

A `Django`_ app to display an icon gallery, listing all defined icons in the `Icomoon`_ manifest you download.

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

Define the setting for the path to the Icomoon manifest file. This is the ``selection.json`` file given in the webfont archive downloaded from Icomoon: ::

    ICOMOON_MANIFEST_FILEPATH = '/home/work/myproject/webapp_statics/fonts/selection.json'

Default behavior require users to be authenticated to view the gallery, if you want to open it also for anonymous, define the following setting: ::

    ICOMOON_PRIVATE = True

Obviously the path may differ for your project.

Then mount its urls in your main ``urls.py`` : ::

    urlpatterns = patterns('',
        ...
        (r'^icomoon/', include('icomoon.urls', namespace='icomoon')),
        ...
    )

Finally this at your responsability to load the webfont into your website, this app won't do it for you.

Note that shipped templates in ``templates/icomoon/`` are written using Foundation5 components and inherits from a ``templates/skeleton.html`` that you have to create yourself. You better gives an eye to this app templates to correctly integrate them or override them.

Usage
*****

When it's installed you could reach the webfont gallery from ``/icomoon/``.

The gallery display all defined icons in the manifest, giving the CSS classname, the unicode codepoint and the UTF-8 code.
