"""
tests_basic.py
~~~~~~~~~~~~~~
Basic unit tests for `mass_replace` python module written using pytest.
"""
import pytest
try:
    import mass_replace as mr
except ModuleNotFoundError:
    print('`mass_replace` not imported')


def test_mass_replace_import():
    assert isinstance(mr.__doc__, str)
    print(type(mr))


def test_load_config():
    print(type(mr.load_config()))
    assert isinstance(type(mr.load_config()), dict)


def test_get_items():
    assert isinstance(mr.get_items(), list)


if __name__ == '__main__':
    print(__doc__)
    print(test_mass_replace_import())