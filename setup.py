#!/usr/bin/env python3

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="staticyah",
    version="0.0.1",
    author="Aphex Creations",
    description="Simple Static Site Generator For Jinja",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aphexcreations/staticyah",
    scripts=[
        "scripts/staticyah",
    ],
    install_requires=["jinja2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
