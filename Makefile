init:
	pip install -r requirements.txt

test:
	nosetests tests

GH_PAGES_SOURCES =.vscode src test .travis Makefile LICENSE README.md requirements.txt setup.py


gh-pages:
    git checkout gh-pages
    rm -rf _build $(GH_PAGES_SOURCES)
    git checkout master 
    git reset HEAD
    cd docs 
    make html
    rsync -av _build/html/* ./
