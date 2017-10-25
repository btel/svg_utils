To do a new release:

- update version information and download link in setup.py
- add a new tag and push it to github `git push --tags`
- build source distribution `python setup.py sdist`
- build universal binary distribution `python setup.py bdist_wheel --universal`
- upload to PyPI `twine upload dist/*`



