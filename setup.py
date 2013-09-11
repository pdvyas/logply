import os
from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='logply',
    version=version,
    description='Log processor',
    author='Pratik Vyas',
    author_email='m@pd.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read().split(),
)
