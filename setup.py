# coding: utf-8

from setuptools import setup, find_packages


setup(
    name='go_fuck',
    version='1.0',
    author='tonic',
    zip_safe=False,
    author_email='tonic@wolege.ca',
    description='add your current working directory into GOPATH',
    packages=find_packages(),
    entry_points={
        'console_scripts':['gofuck=gofuck:fuck_go'],
    },
)
