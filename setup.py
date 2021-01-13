#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from subprocess import getoutput

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "spacy==2.3.5",    
    "pandas==1.1.5",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

class PostInstall(install):
    spacy_model = 'python -m spacy download en'
    def run(self):
        install.run(self)
        print(getoutput(self.spacy_model))
        #https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program
        #subprocess.call([sys.executable, '-m', 'pip', 'install', self.pkgs])


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        PostInstall()


class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        PostInstall()


class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        PostInstall()


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
    extras_require={'interactive': ['matplotlib>=3.3.0']},
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'egg_info': CustomEggInfoCommand,
    },
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
    version="0.1.31",
    zip_safe=False,
)