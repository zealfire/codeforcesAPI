from setuptools import setuptools

setup(
	name='codeforcesAPI',
	version='0.0.1'
	author="Alok Pandey",
	author_email="iamalok185@gmail.com",
	packages=['codeforcesAPI', 'test', ],
	license='MIT',
	description="Python wrapper for codeforces API.",
	long_description=open('READ.md','r').read(),
	install_requires=['requests', ],
	)