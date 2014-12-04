import os
from setuptools import setup, find_packages

NAME = "gae-search"
PACKAGES = find_packages()
DESCRIPTION = ("Gae-search is a wrapper for Google App Engine's search API that uses Django-like syntax for defining "
               "documents, and searching and filtering search indexes.")
URL = "https://github.com/potatolondon/search"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
AUTHOR = 'Potato London Ltd.'

setup(
    name=NAME,
    version='0.0.1',
    packages=PACKAGES,

    # metadata for upload to PyPI
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=["django", "Google App Engine", "GAE"],
    url=URL,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
