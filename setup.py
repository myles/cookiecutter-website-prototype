#!/usr/bin/env python

import json

from distutils.core import setup

with open('cookiecutter.json', 'r') as cookiecutter_json:
    cookiecutter_config = json.loads(cookiecutter_json.read())

setup(
    name=cookiecutter_config['project_name'],
    packages=[],
    version=cookiecutter_config['version'],
    description=cookiecutter_config['project_short_description'],
    author=cookiecutter_config['full_name'],
    author_email=cookiecutter_config['email'],
    license='BSD',
    url='https://github.com/myles/cookiecutter-website-prototype',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
    ],
)

