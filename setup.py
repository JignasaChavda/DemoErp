from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in demo3_app/__init__.py
from demo3_app import __version__ as version

setup(
	name="demo3_app",
	version=version,
	description="app",
	author="jignasa",
	author_email="jignasachavda15@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
