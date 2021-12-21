#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "pandas",
    "psycopg2",
]

setup_requirements = []

test_requirements = []

setup(
    author="Justin Keller",
    author_email="kellerjustin@protonmail.com",
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
    description="Pandas database helper library",
    entry_points={
        "console_scripts": [
            "pd_db_wrangler=pd_db_wrangler.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="pd_db_wrangler",
    name="pd_db_wrangler",
    packages=find_packages(include=["pd_db_wrangler", "pd_db_wrangler.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/kellerjustin/pd_db_wrangler",
    version="0.12.0",
    zip_safe=False,
)
