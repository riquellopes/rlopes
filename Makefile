.SILENT:

BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/output
GITHUB_PAGES_BRANCH=master

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
freezer: tests
	python run.py freezer
tests: clean
	nosetests test/ -v
setup:
	pip install -U pip
	pip install -r requirements.txt
setup-dev: setup
	pip install -r requirements-dev.txt
run: clean
	python run.py
github: freezer
	ghp-import -m "Generate HenriqueLopes site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH) -f
