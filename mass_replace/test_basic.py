"""
tests_basic.py
~~~~~~~~~~~~~~
Basic unit tests for `mass_replace` python module written using pytest.
"""
from sys import version_info
from os import path
import pytest
try:
    import mass_replace as mr
except ModuleNotFoundError:
    print('`mass_replace` not imported')

PYTHON_VER = version_info[0]
mr.resolve_wd('mass_replace')


def test_mass_replace_import():
    assert isinstance(mr.__doc__, str)
    print(type(mr))


def test_correct_working_dir():
    pass


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_load_config():
    load_config_return_type = type(mr.load_config())
    print(load_config_return_type, dict)
    assert load_config_return_type is dict


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_get_items():
    assert type(mr.get_items()) is list


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_get_dirs():
    assert type(mr.get_dirs()) is list


@pytest.mark.skipif(PYTHON_VER <= 2,
                    reason="List comprehension error with Python 2")
def test_get_files():
    """Test that `get_files()` returns a list and that every item within the
    list is a file."""
    files = mr.get_files()
    assert type(files) is list
    for f in files:
        assert path.isfile(f)


if __name__ == '__main__':
    print('Python: {}.{}'.format(version_info[0], version_info[1]))
    print(__doc__)
    pytest.main(args=['-v'])
    # print(test_load_config())
    # print(test_mass_replace_import())
