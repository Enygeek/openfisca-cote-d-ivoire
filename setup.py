#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-COTE_D_IVOIRE',
    version='0.4.0',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description=u'OpenFisca tax and benefit system for CO   TE_D_IVOIRE',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/country-template',
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core[web-api] >= 24.0, < 25.0',
        ],
    extras_require = {
        'dev': [
            'flake8 >= 3.4.0, < 3.5.0',
            'flake8-print',
            'nose',
            ]
        },
    packages=find_packages(),
    test_suite='nose.collector',
    )
