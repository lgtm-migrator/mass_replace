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

mr.resolve_wd('mass_replace')


def test_mass_replace_import():
    assert isinstance(mr.__doc__, str)
    print(type(mr))


def test_correct_working_dir():
    pass


def test_load_config():
    load_config_return_type = type(mr.load_config())
    print(load_config_return_type, dict)
    assert load_config_return_type is dict


def test_get_items():
    assert type(mr.get_items()) is list


def test_get_dirs():
    assert type(mr.get_dirs()) is list


def test_get_files():
    assert type(mr.get_files()) is list


if __name__ == '__main__':
    print(__doc__)
    pytest.main(args=['-v'])
    # print(test_load_config())
    # print(test_mass_replace_import())
