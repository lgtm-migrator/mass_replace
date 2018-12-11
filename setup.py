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

# What packages are required for this module to be executed?
REQUIRED = ["pyaml"]

setup(
    name=NAME,
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": ["replace=mass_replace.__main__:main"]},
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
)
