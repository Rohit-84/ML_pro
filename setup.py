#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Rohit",
    author_email='rohit@gmil.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="ml project",
    entry_points={
        'console_scripts': [
            'python_boilerplate=python_boilerplate.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='python_boilerplate',
    name='python_boilerplate',
    packages=find_packages(include=['python_boilerplate', 'python_boilerplate.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rohit_84/python_boilerplate',
    version='1.0.0',
    zip_safe=False,
)
