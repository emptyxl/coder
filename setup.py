#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='coder',
    version='0.9.0',
    description='A graphical interface tool, integrated web encoding/decoding method, hash method and the ASCII table.',
    long_description='More information you can see: https://github.com/emptyxl/coder',
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
