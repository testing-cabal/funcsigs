#!/usr/bin/env python
from setuptools import setup
import re
import sys

def requirements():
    "Get the module requirements"
    if sys.version_info < (2, 7):
        return ['ordereddict']
    return []

def load_version(filename='funcsigs/version.py'):
    "Parse a __version__ number from a source file"
    with open(filename) as source:
        text = source.read()
        match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", text)
        if not match:
            msg = "Unable to find version number in {}".format(filename)
            raise RuntimeError(msg)
        version = match.group(1)
        return version


setup(
    name="funcsigs",
    version=load_version(),
    packages=['funcsigs'],
    zip_safe=False,
    author="Testing Cabal",
    author_email="testing-in-python@lists.idyll.org",
    url="http://funcsigs.readthedocs.org",
    description="Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+",
    long_description=open('README.rst').read(),
    license="ASL",
    install_requires = requirements(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    tests_require = ['unittest2'],
    test_suite = 'unittest2.collector',
)
