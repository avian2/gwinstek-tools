#!/usr/bin/python

from distutils.core import setup

setup(name='gwinstek-tools',
	version='0.1',
	description='Remote control for controlling GW Instek instruments.',
	license='GPL',
	long_description=open("README").read(),
	author='Tomaz Solc',
	author_email='tomaz.solc@tablix.org',

	packages = [ 'gwinstek' ],

	provides = [ 'gwinstek' ],

	classifiers = [
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2",
		"Topic :: Scientific/Engineering",
	],
)
