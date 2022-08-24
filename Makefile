# Makefile for the project
.PHONY: install format lint test sec
install:
	@poetry install
format:
	@blue .
	@isort .
lint:
	@blue .
	@isort .
	@prospector
test:
	@pytest -v
sec:
	@pip-audit