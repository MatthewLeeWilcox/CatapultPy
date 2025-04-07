from setuptools import setup, find_packages

setup(
    name='CatapultPy',
    version='0.1',
    packages=find_packages(),
    description='Applies wrapper to Catapult API queries for data science projects for Python Users. Similar to CatapultR',
    author='Matthew Wilcox',
    author_email='matthewleewilcox@gmail.com',
    install_requires=[
    'pandas>=2.2.0',
    'numpy>=1.26.0',
    'requests>=2.32.0',
],
)
