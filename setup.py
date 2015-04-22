#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://pytestpackage.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pytestpackage',
    version='0.1.1',
    description='testing python packaging...',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Carlo Dri',
    author_email='carlo.dri@gmail.com',
    url='https://github.com/carlodri/pytestpackage',
    packages=[
        'pytestpackage',
    ],
    package_dir={'pytestpackage': 'pytestpackage'},
    include_package_data=True,
    install_requires=['numpy'
    ],
    license='MIT',
    zip_safe=False,
    keywords='pytestpackage',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
