#!/usr/bin/env python2

import os, codecs
from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='Divine',
      py_modules=['divine'],
      version='1.0',
      description='A zork-inspired game',
      long_description=read("README.md"),
      license="MIT",
      author='Robin Choudhury',
      author_email='xrobinc@gmail.com',
      url='http://git.io/divine'
     )
