#!/usr/bin/env python
# encoding: utf-8


import os
from setuptools import setup, find_packages

KEYWORDS = '''
energy
bandwidth estimation
'''.strip().split('\n')

DESCRIPTION='Signal processing tool to detect the maximum energy threshold of one or more audio files'
LONGDESCRIPTION='Energy above a certain threshold may be lost due to compression manipulations (typically occurs when converting wav to mp3 to wav). This loss can be easily identified for a given sampling rate by examining the maximum frequency obtained for a percentage of the signal energy.'

setup(
    name = "bandwidthestimation",
    version = "0.1.0",
    author = "Simon Devauchelle",
    author_email = "devausimon@gmail.com",
    test_suite="run_test.py",
    description = DESCRIPTION,
    install_requires=["numpy", "scipy"],
    url = "https://github.com/simonD3V/bandwidthestimation",
    keywords = KEYWORDS,
    packages = find_packages(),
    include_package_data = True,
    data_files = ['LICENSE'],
    long_description=LONGDESCRIPTION,
    long_description_content_type='text/markdown',
    python_requires='>=3.10.2',
)
