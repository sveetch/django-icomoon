PYTHON_INTERPRETER=python3
VENV_PATH=.venv
PACKAGE_NAME=django-icomoon
PACKAGE_SLUG=`echo $(PACKAGE_NAME) | tr '-' '_'`
APPLICATION_NAME=icomoon
PIP=$(VENV_PATH)/bin/pip
FLAKE=$(VENV_PATH)/bin/flake8
PYTEST=$(VENV_PATH)/bin/pytest
TWINE=$(VENV_PATH)/bin/twine
DJANGO_MANAGE=$(VENV_PATH)/bin/python sandbox/manage.py
SPHINX_RELOAD=$(VENV_PATH)/bin/python sphinx_reload.py

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install             -- to install this project with virtualenv and Pip"
	@echo ""
	@echo "  clean               -- to clean EVERYTHING (Warning)"
	@echo "  clean-pycache       -- to remove all __pycache__, this is recursive from current directory"
	@echo "  clean-statics       -- to clean static stuff from sandbox"
	@echo "  clean-install       -- to clean Python side installation"
	@echo ""
	@echo "  run                 -- to run Django development server"
	@echo "  migrate             -- to apply demo database migrations"
	@echo "  superuser           -- to create a superuser for Django admin"
	@echo "  icomoon             -- to deploy an icon font map on demo from an Icomoon snapshot (icomoon.zip)"
	@echo ""
	@echo "  livedocs            -- to run livereload server to rebuild documentation on source changes"
	@echo ""
	@echo "  flake               -- to launch Flake8 checking"
	@echo "  tests               -- to launch base test suite using Pytest"
	@echo "  quality             -- to launch Flake8 checking and every tests suites"
	@echo ""
	@echo "  release             -- to release package for latest version on PyPi (once release has been pushed to repository)"
	@echo

clean-pycache:
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-statics:
	rm -Rf sandbox/static
.PHONY: clean-statics

clean-install:
	rm -Rf $(VENV_PATH)
	rm -Rf $(PACKAGE_SLUG).egg-info
.PHONY: clean-install

clean: clean-install clean-pycache clean-statics
.PHONY: clean

venv:
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# This is required for those ones using old distribution
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
.PHONY: venv

create-var-dirs:
	@mkdir -p data/db
	@mkdir -p data/static/css
	@mkdir -p sandbox/media
	@mkdir -p sandbox/static/css
.PHONY: create-var-dirs

migrate:
	@DJANGO_SECRET_KEY=$(DEMO_DJANGO_SECRET_KEY) \
	$(DJANGO_MANAGE) migrate
.PHONY: migrate

superuser:
	@DJANGO_SECRET_KEY=$(DEMO_DJANGO_SECRET_KEY) \
	$(DJANGO_MANAGE) createsuperuser
.PHONY: superuser

install: venv create-var-dirs
	$(PIP) install -e .[dev]
	${MAKE} migrate
.PHONY: install

run:
	@DJANGO_SECRET_KEY=$(DEMO_DJANGO_SECRET_KEY) \
	$(DJANGO_MANAGE) runserver 0.0.0.0:8001
.PHONY: run

icomoon:
	$(DJANGO_MANAGE) icomoon_deploy
.PHONY: icomoon

livedocs:
	$(SPHINX_RELOAD)
.PHONY: livedocs

flake:
	$(FLAKE) --show-source $(APPLICATION_NAME)
	$(FLAKE) --show-source tests
.PHONY: flake

tests:
	$(PYTEST) -vv tests/
.PHONY: tests

quality: tests flake
.PHONY: quality

release:
	rm -Rf dist
	$(VENV_PATH)/bin/python setup.py sdist
	$(TWINE) upload dist/*
.PHONY: release
