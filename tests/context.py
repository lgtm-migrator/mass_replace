# -*- coding: utf-8 -*-
"""
context.py
~~~~~~~~~~
Access main module from tests folder
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   '../mass_replace')))

import mass_replace

print('USING context.py')

if __name__ == '__main__':
    print(__doc__)
    print('\tMODULES')
    print(mass_replace.__doc__)