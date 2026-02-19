#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ecc_finder',
    version='v1.1.0',
    description='A tool for detecting extrachromosomal circular DNA (eccDNA) from sequencing data.',
    author='Panpan Zhang',
    author_email='njaupanpan@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pysam',
        'numpy',
        'pandas',
        'matplotlib',
        'pybedtools'
    ],
    entry_points={
        'console_scripts': [
            'ecc_finder=ecc_finder.cli:main',
        ],
    },
    zip_safe=True
)
