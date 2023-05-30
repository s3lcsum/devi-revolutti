#!/usr/bin/env make -f
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: run tests clean install

run: install
	$(PYTHON) src/cli.py

tests: install
	(cd src && ../$(PYTHON) -m pytest ../tests/)

install: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf tests/__pycache__
	rm -rf $(VENV)

build:
	docker build -t=$(TAG) .
