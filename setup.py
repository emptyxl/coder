#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='coder',
    version='0.0.1',
    description='A universal encoder/decoder written in Python, supports common encoding formats.',
    long_description='More information you can see: https://github.com/emptyxl/encoder-decoder',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ],
    keywords='python encdoer decoder common encoding formats',
    author='empty_xl',
    author_email='empty_xl@163.com',
    license='MIT',
    packages=['coder'],
    url='https://github.com/emptyxl/encoder-decoder',
    install_requires=[
        # 'Pillow',
        # 'docopt'
    ],
    entry_points={
        'console_scripts': [
            'coder = coder.coder:GUI'
        ]
    },
)
