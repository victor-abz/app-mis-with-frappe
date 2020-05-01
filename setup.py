# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in contact_app/__init__.py
from contact_app import __version__ as version

setup(
	name='contact_app',
	version=version,
	description='App to manage contacts',
	author='Abizeyimana Victor',
	author_email='svicky.shema@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
