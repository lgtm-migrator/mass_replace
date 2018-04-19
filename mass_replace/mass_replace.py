"""
mass_replace.py
~~~~~~~~~~~~~~~
WIP
"""
import os
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
    item_list = []
    return item_list


if __name__ == '__main__':
    print(__doc__)
    resolve_wd()
    pp(load_config())
