from setuptools import setup

setup(
	name='codeforcesAPI',
	version='0.0.1',
	author="Alok Pandey",
	author_email="iamalok185@gmail.com",
	packages=['codeforces', 'test', ],
	license='MIT',
	description="Python wrapper for codeforces API.",
	long_description=open('README.md','r').read(),
	install_requires=['requests', ],
	)