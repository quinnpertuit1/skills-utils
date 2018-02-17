#!/usr/bin/env python

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

with open('requirements_dev.txt') as requirements_file:
    test_requirements = requirements_file.readlines() + requirements

setup(
    name='Skills Utils',
    version='0.3.0',
    description='Shared utilities for skills/jobs taxonomy creation',
    author="Center for Data Science and Public Policy",
    author_email='datascifellows@gmail.com',
    url='https://github.com/workforce-data-initiative/skills-utils',
    packages=find_packages(include=['skills_utils*']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
