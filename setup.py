from setuptools import setup

setup(name='GitHide',
	version='0.1',
	description='Hide/Show .git folder',
	url='http://github.com/AlexMili/githide',
	author='AlexMili',
	license='MIT',
	zip_safe=True,
	entry_points={
		'console_scripts': [
			'githide = githide:githide',
			'gitshow = githide:gitshow',
		]
	}
)