#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


def long_description():
    with open('README.rst') as f:
        return f.read()


setup(
    name='coder',
    version='1.0.4',
    description='A graphical interface tool, integrated web encoding/decoding method, hash method and the ASCII table.',
    # long_description='More information you can see: https://github.com/emptyxl/coder',
    long_description=long_description(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ],
    keywords='encdoer decoder encoding decoding ',
    author='empty_xl',
    author_email='empty_xl@163.com',
    license='MIT',
    packages=['coder'],
    url='https://github.com/emptyxl/coder',
    install_requires=[
        'wxPython'
    ],
    entry_points={
        'console_scripts': [
            'coder = coder.coder:main'
        ]
    },
)
