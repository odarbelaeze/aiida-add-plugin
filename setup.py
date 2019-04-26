#!/usr/bin/env python

from setuptools import setup

version = "19.4.0"

setup(
    name="aiida-add-plugin",
    version=version,
    description="An AiiDA plugin for the very complex add program",
    author="Oscar Arbelaez",
    author_email="oscar.arbelaez@epfl.ch",
    url="https://github.com/odarbelaeze/aiida-add-plugin",
    packages=["add"],
    long_description=open("README.md").read(),
    install_requires=["aiida-core>=1.0.0b2,<2"],
    entry_points={
        "aiida.calculations": ["add.calculation = add.calculation:AddCalculation"],
        "aiida.parsers": ["add.parser = add.parser:AddParser"],
    },
    classifiers=[
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering"
        "Topic :: Scientific/Engineering :: Information Analysis"
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)

