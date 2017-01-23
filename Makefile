init:
	pip install -r requirements.txt

test:
	nosetests tests

GH_PAGES_SOURCES =.vscode src test .travis Makefile LICENSE README.md requirements.txt setup.py


gh-pages:
    git checkout gh-pages
    rm -rf build _sources _static $(GH_PAGES_SOURCES)
    git checkout master 
    git reset HEAD
    cd docs 
    make html
    mv -fv _build/html/**/*.* ./**/*.*
    rm -rf $(GH_PAGES_SOURCES) _build
    git add -A
    git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" 
    git push origin gh-pages
    git checkout master
