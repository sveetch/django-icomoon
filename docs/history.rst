.. _intro_history:

=======
History
=======

Version 1.4.0 - Unreleased
--------------------------

**Project and package refactoring**

* Drop ``six`` usage;
* Drop ``django-braces`` usage;
* Migrate to ``setup.cfg`` for package configuration;
* Cover every supported Django versions with tox;
* Updated demo project with sandbox;
* Add documentation on ReadTheDoc;
* Update ``icon_map.scss`` template to include a Sass map for available icons,
  close #11;

Version 1.3.0 - 2020/08/13
--------------------------

**This has not be released into a package on Pypi** due to packaging
configuration problem, the **1.4.0 release resolve everything** without any
behavior changes.

This is a maintenance release for recent (>=2.0) Django environment.

Pin your project dependancies to ``django-icomoon<1.3.0`` if your environment
does not match the new requirements.

* Drop support for Django<=2.0, add support for Django 2.0 to 3.1;
* Drop support for Python2, at least Python 3.6 is required;


Version 1.2.0 - 2018/02/16
--------------------------

* Fix Sass template for bad selector, close #10;
* Cleaned icon gallery template;
* Dropped support for Django <= 1.8;
* Better Makefile for development install;

Version 1.1.1 - 2018/01/30
--------------------------

* Fixed missing ``mixin()`` in Sass template;

Version 1.1.0 - 2018/01/30
--------------------------

* Fixed compatibiliy with django>=1.10 in management command, close #9;
* Added missing semicolon on pseudo element classes in CSS template;
* Added ``icon_map.scss`` template to create an useful Sass file instead of
  simple CSS classes, close #5;

Version 1.0.0 - 2017/05/29
--------------------------

* Added tests structure;
* Covered all code with tests except for the management command;
* Confirmed support for Django 1.8 to Django 1.11, Python 2 and Python 3.5
  through 'tox';

Version 0.4.0 - 2016/04/06
--------------------------

* Dropped support for Django <= 1.7;
* Fixed command line arguments for Django == 1.8;

Version 0.3.1 - 2015/10/24
--------------------------

* Lowering down minimal 'django-braces' dependancy, better classifiers for
  Django versions in setup.py;

Version 0.3.0 - 2015/10/11
--------------------------

* Implemented command line to deploy webfont from download ZIP on Icomoon,
  contains many backward incompatible settings, this is related to issue #2;
