.PHONY: help clean dev docs package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "	 dev 	install all deps for dev env"
	@echo "  docs	create pydocs for all relveant modules"
	@echo "	 test	run all tests with coverage"

clean:
	${INFO} "clean..."
	rm -rf dist/*

dev:
	${INFO} "dev..."
	pip install coverage
	pip install codecov
	pip install pylint
	pip install twine
	pip install sphinx
	pip install sphinx-autobuild
	pip install sphinx_rtd_theme
	pip install -e .

docs:
	${INFO} "docs..."
	$(MAKE) -C docs html

package:
	${INFO} "package..."
	python setup.py sdist
	python setup.py bdist_wheel

test:
	${INFO} "test..."
	coverage run -m unittest discover
	coverage html
	
	
# Cosmetics
YELLOW := "\e[1;33m"
NC := "\e[0m"

# Shell Functions
INFO := @bash -c '\
  printf $(YELLOW); \
  echo "=> $$1"; \
  printf $(NC)' SOME_VALUE