#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ezfintech",
    version="0.0.32",
    author="Yizhe Zhang",
    author_email="ervinzhang319@gmail.com",
    description="get stock data from different APIs and Analyze Stock Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/YizheZhang-Ervin/EZFintech",
    packages = find_packages(),
    install_requires=["numpy","pandas","matplotlib","requests","mplfinance","pandas_datareader","tensorflow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
