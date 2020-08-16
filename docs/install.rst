.. _intro_install:

=======
Install
=======

Install package in your environment : ::

    pip install django-icomoon

For development usage see :ref:`install_development`.

Add it to your installed Django apps in settings : ::

    INSTALLED_APPS = (
        ...
        "icomoon",
        ...
    )

Import default app settings: ::

    from icomoon.settings import *

Default behavior require users to be authenticated to view the gallery, if you
want to open it for anonymous define the following setting: ::

    ICOMOON_PRIVATE = False


.. _install_manifest:

Webfonts and manifests
----------------------

Now you must define at least one webfont in your project settings like this: ::

    ICOMOON_MANIFEST_FILEPATH = {
        "Default": {
            "fontdir_path": "/home/work/myproject/static/fonts/default",
            "csspart_path": "/home/work/myproject/static/css/icomoon_icons.scss"
        },
    }

Each website entry is a dict containing the following values:

fontdir_path
    (Required) Absolute path to the webfont directory. It will be created with
    Manifest file and font files on each deploy.
csspart_path
    (Optional) Absolute path where will be written the css part containing
    webfont icons.


Urls
----

Just mount its urls in your main ``urls.py`` : ::

    urlpatterns = [
        ...
        path("icomoon/", include("icomoon.urls", namespace="icomoon")),
        ...
    ]


Templates
---------

This is at your responsability to load the webfont and CSS (which enable icons
from webfont) into your website templates, this app won't do it for you.

Note that shipped template gallery in ``templates/icomoon/`` is inherits from
a ``templates/skeleton.html`` that you have to create yourself.

Here is an example of a this skeleton template: ::

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{% block head_title %}Sample site{% endblock %}</title>
        {% block head_assets %}{% endblock %}
    </head>

    <body>
    {% spaceless %}
        {% block base_content %}{% endblock %}
    {% endspaceless %}
    </body>
    </html>

The most important thing to retain is the template block ``base_content`` where
the app template will insert its content.
