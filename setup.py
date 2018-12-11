#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# Package meta-data.
NAME = "mass_replace"
DESCRIPTION = "Walkthrough directories and find and replace txt on select filetypes."
URL = "https://github.com/Kilo59/mass_replace"
EMAIL = "gabriel59kg@gmail.com"
AUTHOR = "Gabriel Gore"
# replace with __version__
VERSION = "0.0.3"

# What packages are required for this module to be executed?
REQUIRED = ["pyaml"]

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(HERE.joinpath(NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": ["replace=mass_replace.__main__:main"]},
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
)
