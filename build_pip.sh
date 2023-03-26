source ~/venv/bin/activate
python setup.py sdist build
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*