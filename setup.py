#!/usr/bin/env python

from setuptools import setup

install_requires = [
    'pysaml2'
]

tests_require = [
    'pytest',
]

setup(
    name='s2sproxy',
    version='0.1.0',
    description='Simple configurable proxy from SAML2 to SAML2.',
    author='DIRG',
    author_email='dirg@its.umu.se',
    license='Apache 2.0',
    url='https://github.com/its-dirg/s2sproxy',
    packages=['s2sproxy'],
    package_dir={'': 'src'},
    classifiers=["Development Status :: 4 - Beta",
                 "License :: OSI Approved :: Apache Software License",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Programming Language :: Python :: 2.7"],
    tests_require=tests_require,
    install_requires=install_requires,
    zip_safe=False,
)
