"""
mass_replace.py
~~~~~~~~~~~~~~~
WIP
"""
import yaml
from pprint import pprint as pp


def load_config():
    """Load a .yml config file as a dictionary and return it."""
    with open('config.yaml', 'r') as f_in:
        return yaml.safe_load(f_in)


def get_items():
    """Returns a list of files and folders in a directory"""
    pass
    return


if __name__ == '__main__':
    print(__doc__)
    pp(load_config())
