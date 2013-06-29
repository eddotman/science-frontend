#!/usr/bin/env python

"""
setup.py file for SWIG mucal
"""

from distutils.core import setup, Extension
import numpy


mucal_module = Extension('_mucal',
                           sources=['mucal_wrap.c', 'mucal.c'],
                           )

setup (name = 'mucal',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig mucal from docs""",
       ext_modules = [mucal_module],
       py_modules = ["mucal"],
       )
