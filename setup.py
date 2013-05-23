#!/usr/bin/python

from distutils.core import setup

setup(name='GW Instek tools',
	version='0.1',
	description='Python modules for controlling GW Instek instruments over USB',
	license='GPL',
	long_description=open("README").read(),
	author='Tomaz Solc',
	author_email='tomaz.solc@tablix.org',

	packages = [ 'gwinstek' ],

	provides = [ 'gwinstek' ],

	classifiers = [
		"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3",
	],
)
