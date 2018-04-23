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


def load_config(filename='config.yaml'):
    """Load a .yml config file as a dictionary and return it."""
    with open(filename, 'r') as f_in:
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
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')


def many_find_replace(filename, text_search_replace_dicts):
    for text_to_search, replacement_text in text_search_replace_dicts.items():
        file_find_replace(filename, text_to_search, replacement_text)


def discover_filetypes(root_folder=None, hard_copy=True):
    if not root_folder:
        try:
            root_folder = load_config('config.yaml')['root_folder']
            if root_folder is None:
                raise(FileNotFoundError)
        except FileNotFoundError:
            root_folder = os.getcwd()
    file_types = set() 
    for _, _, filenames in os.walk(root_folder):
        f_types = ['.{}'.format(ext.split('.')[-1]) for ext in filenames]
        file_types.update(f_types)
    if hard_copy:
        with open('file_exts.txt', 'w') as f_out:
            f_out.writelines('\n'.join(file_types))
    return file_types


def mass_replace(root_folder=None, config=None, verbose=False):
    """Peforms find and replace operations on files nested in a root direcotry
    according to settings in the `config.yaml` file."""
    if not config:
        config = load_config('config.yaml')
    if not root_folder:
        root_folder = config['root_folder']
    print(f'ROOT: {root_folder}')
    replacement_pairs = config['replacement_pairs']
    for i in replacement_pairs.items():
        print(i)
    counter = 0
    for dirpath, dirnames, filenames in os.walk(root_folder):
        valid_files = [f for f in filenames if f.split('.')[-1]
                       in config['filetypes']]
        if verbose:
            print(f'\tCurrent Path - STEP:{counter}')
            pp(dirpath)
            print(f'\tDirectories - STEP:{counter}')
            pp(dirnames)
            print(f'\tFiles: - STEP:{counter}')
            pp(filenames)
            print()
        counter += 1
        for fname in valid_files:
            print(f'|----{fname}')
            many_find_replace(f'{dirpath}\\{fname}', replacement_pairs)
    return


if __name__ == '__main__':
    print(__doc__)
    pp(discover_filetypes(hard_copy=True))
    # file_find_replace('lorem.txt', 'Lorem', 'REPLACED')
    # print('\tMASS_REPLACE')
    # mass_replace(verbose=True)

