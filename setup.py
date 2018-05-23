from setuptools import setup, Distribution, find_packages

class BinaryDistribution(Distribution):
	def is_pure(self):
		return False

setup(	name='amadeus', version='0.0',
		description='PDE Solver Package',
		url='https://github.com/yoon-gu/amadeus/',
		author=['Dong-wook Shin', 'Yoon-gu Hwang'],
		author_email=['dwshin.yonsei@gmail.com', 'yz0624@gmail.com'],
		license='MIT',
		packages=find_packages(),
		install_requires=[
			'numpy',
		],
		distclass=BinaryDistribution,
		zip_safe=False)
