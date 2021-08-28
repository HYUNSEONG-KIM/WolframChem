#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = '''A simple Python wrapper around the wolfram api.'''

setup(
    name='wolframchem',
    version='0.0.1',
    author='Kim, Hyeansung',
    author_email='qwqwhsnote@gm.gist.ac.kr',
    license='MIT',
    url='https://github.com/mcs07/ChemSpiPy',
    packages=['wolframchem'],
    description='Python ',
    long_description=long_description,
    keywords='chemistry cheminformatics pubchem, wolfram, chemspider, Open',
    zip_safe=False,
    install_requires=['requests', 'six'],
    tests_require=['pytest'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS dependent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
