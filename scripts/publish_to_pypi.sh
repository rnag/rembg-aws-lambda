#!/usr/bin/env bash

# Use this script to manually publish to PyPI!
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
