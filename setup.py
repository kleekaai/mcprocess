#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Mohit Jain",
    author_email="mohit.j@molecularconnections.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Text Processing Library",
    entry_points={
        "console_scripts": [
            "mcprocess=mcprocess.cli:main",
        ],
    },
    install_requires=requirements,
    extras_requires=[
        'spacy',
        'en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz',
    ],
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="mcprocess",
    name="mcprocess",
    packages=find_packages(include=["mcprocess", "mcprocess.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/kleekaai/mcprocess",
    version="0.1.0",
    zip_safe=False,
)