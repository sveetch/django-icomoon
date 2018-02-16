PYTHON=python3

PIP=venv/bin/python -m pip
FLAKE=venv/bin/flake8
PYTEST=venv/bin/py.test
DJANGOMANAGER=venv/bin/python project_test/manage.py

.PHONY: help clean delpyc install install-dev tests flake quality runserver

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  delpyc              -- to remove all *.pyc files, this is recursive from the current directory"
	@echo "  clean               -- to clean local repository from all stuff created during development"
	@echo
	@echo "  install             -- to install as develop package"
	@echo "  install-dev         -- to install as develop package with every for development"
	@echo
	@echo "  flake               -- to launch Flake8 checking on boussole code (not the tests)"
	@echo "  tests               -- to launch tests using py.test"
	@echo "  quality             -- to launch Flake8 checking and tests with py.test"
	@echo
	@echo "  runserver           -- to launch a Django instance on 0.0.0.0:8001"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	rm -Rf venv dist .tox django_icomoon.egg-info .cache project_test/.cache/ project_test/__pycache__/ project_test/tests/__pycache__/

venv:
	$(PYTHON) -m venv venv

install: venv
	$(PIP) install -e .

install-dev: install
	$(PIP) install -r requirements/dev.txt

flake:
	$(FLAKE) --show-source icomoon

tests:
	$(PYTEST) -vv project_test/

quality: tests flake

runserver:
	@if [ ! -e project_test/db.sqlite3 ]; then $(DJANGOMANAGER) migrate --settings=project.settings.development; fi;
	$(DJANGOMANAGER) runserver 0.0.0.0:8001 --settings=project.settings.development
