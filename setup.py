#!/usr/bin/env python

from distutils.core import setup

setup(name="osrs_exchange",
	version="0.5",
	description="API wrapper for the OSRS WIKI Exchange databse",
	author="Yannick Dorn",
	author_email="yannick.dorn@gmail.com",
	url="ydorn.com",
	packages=["requests"]
)

package_dir = {'':'exchange'}