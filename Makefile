#!/usr/bin/make

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

format:
	black ./src/
	ruff check --fix-only ./src/
.PHONY: format

lint:
	black --check ./src/
	ruff check ./src/
.PHONY: lint