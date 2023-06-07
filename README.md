# Documentation for FigCapsHF

1. Install sphinx and furo

```
python -m pip install sphinx
pip install furo
```

2. Run

```
mkdir source/_static
sphinx-build -b html source build/html
```

and open docs/build/html/index.html inside of your browser, where you should see a locally hosted version of the docs website.

3. After this has been built once, you can run

```
make clean
make html
```

every time you make changes.

Follow https://www.sphinx-doc.org/en/master/index.html for more details and tutorial.
