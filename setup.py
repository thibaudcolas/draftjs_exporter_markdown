#!/usr/bin/env python

import io

from setuptools import find_packages, setup

__title__ = 'draftjs_exporter_markdown'
__version__ = '0.2.3'
__description__ = 'Library to convert rich text from Draft.js raw ContentState to Markdown, based on draftjs_exporter'
__url__ = 'https://github.com/thibaudcolas/draftjs_exporter_markdown'
__author__ = 'Thibaud Colas'
__author_email__ = 'thibaudcolas@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018-present %s' % __author__

dependencies = [
    'draftjs_exporter>=2.1.0,<5',
]

testing_dependencies = [
    # Required for running the tests.
    'tox>=2.3.1',

    # For coverage and PEP8 linting.
    'coverage>=4.1.0',
    'flake8>=3.2.0',
    'autopep8>=1.3.3',
    'isort==4.3.21',
    'coveralls==2.0.0',
] + dependencies

documentation_dependencies = [

]

with io.open('README.md', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Editors :: Word Processors',
    ],
    keywords=[
        'draftjs',
        'exporter',
        'markdown',
        'content'
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=dependencies,
    extras_require={
        'testing': testing_dependencies,
        'docs': documentation_dependencies,
    },
    zip_safe=False,
)
