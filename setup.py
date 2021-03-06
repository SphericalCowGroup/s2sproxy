#!/usr/bin/env python

"""
setup.py
"""

from setuptools import setup, find_packages

setup(
    name='s2sproxy',
    version='0.1.0',
    description='Simple configurable proxy from SAML2 to SAML2.',
    author='DIRG',
    author_email='dirg@its.umu.se',
    license='Apache 2.0',
    url='https://github.com/its-dirg/s2sproxy',
    packages=find_packages('src/'),
    package_dir={'': 'src'},
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: Apache Software License',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Programming Language :: Python :: 3.4'],
    install_requires=["pysaml2 >= 3.0.0"],
    zip_safe=False,
)
