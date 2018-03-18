import setuptools
import os

NAME = 'namanager'
VERSION = '0.0.1'
DESCRIPTION = (
    'A checker could check name of file/directory is expectable or not.'
)
LONG_DESCRIPTION = open(
     os.path.join(os.path.dirname(__file__), 'README.md')).read()

LICENSE = 'GNU General Public License v3.0'
AUTHOR = (
    'Ernest Chang (iattempt@github) and '
    'Arnav Borborah (arnavb@github)'
)
AUTHOR_EMAIL = 'iattempt.net@gmail.com'
URL = 'https://github.com/iattempt/namanager'
PACKAGES = {'namanager'}
KEYWORDS = ['name', 'manager', 'checker', 'formatter', 'filename']
PYTHON_REQUIRES = '==3.4.*,==3.5.*,==3.6.*'

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=PACKAGES,
    keywords=KEYWORDS,
    python_requires=PYTHON_REQUIRES
)