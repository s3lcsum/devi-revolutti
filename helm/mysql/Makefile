.PHONY: help

ns ?= default
pkg ?= database

path ?= $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

install:
	helm dep update
	helm upgrade $(pkg) $(path) --namespace $(ns) --install

test: install
	helm test $(pkg)