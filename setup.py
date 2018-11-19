# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

<<<<<<< HEAD
# get version from __version__ variable in app1/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('app1/__init__.py', 'rb') as f:
=======
# get version from __version__ variable in cpfa/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('cpfa/__init__.py', 'rb') as f:
>>>>>>> e749145085c0ecdeac8d83ab3f36927a070bec7c
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
<<<<<<< HEAD
	name='app1',
	version=version,
	description='Test App',
	author='frappe',
	author_email='ebukaakeru@gmail.com',
=======
	name='cpfa',
	version=version,
	description='Total E&P NIG CPFA ERPNext customization',
	author='Manqala',
	author_email='dev@manqala.com',
>>>>>>> e749145085c0ecdeac8d83ab3f36927a070bec7c
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
