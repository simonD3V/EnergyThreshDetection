#!/usr/bin/env python
# encoding: utf-8


import os
from setuptools import setup, find_packages

KEYWORDS = '''
maximum energy thresholds
'''.strip().split('\n')

DESCRIPTION='Signal processing tool to detect the maximum energy threshold of one or more audio files'

setup(
    name = "EnergyThresholdDetection",
    version = "0.1.0",
    author = "Simon Devauchelle",
    author_email = "devausimon@gmail.com",
    test_suite="run_test.py",
    description = DESCRIPTION,
    install_requires=["numpy", "librosa", "scipy"],
    url = "https://github.com/simonD3V/EnergyThreshDetection",
    keywords = KEYWORDS,
    packages = find_packages(),
    include_package_data = True,
    data_files = ['LICENSE'],
    long_description_content_type='text/markdown',
    python_requires='>=3.10.2',
)
