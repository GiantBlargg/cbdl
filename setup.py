from setuptools import setup, find_packages

setup(
	name="cdl",
	version="0.0.1",
	url="https://github.com/GiantBlargg/cdl",
	author="GiantBlargg",
	license="MIT",
	install_requires=["requests","click"],
	python_requires=">=3",
	packages=find_packages("src"),
	package_dir={'':'src'},
	entry_points={"console_scripts":"cdl = main:main"}
)
