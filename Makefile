# Makefile for the project
.PHONY: install format lint test sec

requirements:
	@poetry show --no-dev | tr -s " " | sed 's/ /==/' | sed 's/ .*//' > requirements.txt
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