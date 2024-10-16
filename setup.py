#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

setup(
    name="python-package-template",
    version="0.0.1",
    description="Basic package template for python using setuptools.",
    author="cuttlefisch",
    author_email="",
    packages=find_packages(),
    test_suite="nose.collector",
    tests_require=["nose==1.3.7"],
    python_requires="==3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
