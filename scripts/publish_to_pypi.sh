#!/usr/bin/env bash

# Use this script to manually publish to PyPI!

python setup.py sdist bdist_wheel

python -c 'import pkgutil; exit(0 if pkgutil.find_loader("twine") else 2)' || { echo 'Installing twine...'; pip install --quiet twine; }

while true; do
    read -p "Do you want to upload to PyPI (Y/N)? " yn
    case $yn in
        [Yy]* ) python -m twine upload dist/*; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
