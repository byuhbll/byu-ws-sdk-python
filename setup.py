#!/usr/bin/env python2.7

import sys

from setuptools import setup, find_packages


if sys.version_info < (2, 7, 0) or sys.version_info >= (3,):
    sys.stderr.write("byu_ws_sdk currently requires Python 2.7.\n")
    sys.exit(-1)

# we only use the subset of markdown that is also valid reStructuredText so
# that our README.md works on both github (markdown) and pypi (reStructuredText)
with open("README.md") as rm_file:
    long_description = rm_file.read()

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='byu_ws_sdk',
      version='0.9.13',
      description='A Python SDK for calling BYU REST web services.',
      long_description=long_description,
      author='BYU OIT Core Application Engineering',
      author_email='paul_eden@byu.edu',
      url='https://github.com/byu-oit-core-appeng/byu-ws-sdk-python',
      packages=find_packages(),
      data_files=[('', ['README.md', 'LICENSE'])],
      test_suite="byu_ws_sdk.test",
      license="MIT",
      install_requires=['requests == 0.14.1', 'simplejson', 'decorator'],
      zip_safe=True,
      **extra
      )
