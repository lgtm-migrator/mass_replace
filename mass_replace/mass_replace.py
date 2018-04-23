"""
mass_replace.py
~~~~~~~~~~~~~~~
WIP
"""
import os
import fileinput
import yaml
from pprint import pprint as pp


def resolve_wd(target_dir='mass_replace'):
    try:
        os.chdir(target_dir)
    except Exception as E:
        print(E)


def load_config():
    """Load a .yml config file as a dictionary and return it."""
    with open('config.yaml', 'r') as f_in:
        return yaml.safe_load(f_in)


def get_items():
    """Returns a list of files and folders in a directory"""
    return [x for x in os.listdir()]


def get_dirs():
    """Returns a list of all folders in the current working directory."""
    return [x for x in get_items() if os.path.isdir(x)]


def get_files():
    """Returns a list of all files in the current working directory."""
    return [x for x in get_items() if os.path.isfile(x)]


def file_find_replace(filename, text_to_search, replacement_text):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')


if __name__ == '__main__':
    print(__doc__)
    resolve_wd()
    pp(load_config())
