.PHONY: clean-pyc init help test-ci
.DEFAULT_GOAL := help

help: ## See what commands are available.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36mmake %-15s\033[0m # %s\n", $$1, $$2}'

init: clean-pyc ## Install dependencies and initialise for development.
	pip install -r requirements.txt
	./.githooks/deploy

lint: ## Lint the project.
	flake8 draftjs_exporter_markdown tests example.py setup.py
	isort --check-only --diff --recursive draftjs_exporter_markdown tests example.py setup.py
	npm run lint

test: ## Test the project.
	python -m unittest discover

test-watch: ## Restarts the tests whenever a file changes.
	nodemon -q -e py -w tests -w draftjs_exporter_markdown -x "clear && make test -s || true"

test-coverage: ## Run the tests while generating test coverage data.
	coverage run -m unittest discover && coverage report

test-ci: ## Continuous integration test suite.
	tox

dev: ## Restarts the example whenever a file changes.
	nodemon -q -e py -w tests -w draftjs_exporter_markdown -w example.py  -x "clear && python example.py || true"

clean-pyc: ## Remove Python file artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

release: ## Prepare a release for publication.
	npm run release

publish: ## Publishes a new version to pypi
	rm -f dist/* && python setup.py clean sdist bdist_wheel && twine upload dist/*
