#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if "execute" in sys.argv:
        execfile(os.path.abspath(os.path.dirname(__file__)) + '/core/__init__.py')

