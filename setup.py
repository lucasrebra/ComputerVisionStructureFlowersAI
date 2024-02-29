import io
import os
from setuptools import find_packages, setup

# Metadata of package
NAME = 'flowers_prediction'
DESCRIPTION = 'Predict flower types using machine learning models'
URL = 'https://github.com/tu_usuario/flowers_prediction'
EMAIL = 'tu@email.com'
AUTHOR = 'Tu Nombre'
REQUIRES_PYTHON = '>=3.6'

# Get the list of packages to be installed
def list_reqs(fname='requirements.txt'):
    with io.open(fname, encoding='utf-8') as f:
        return f.read().splitlines()

try:
    with io.open('README.md', encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_DIR = os.path.join(ROOT_DIR, NAME)
about = {}
with open(os.path.join(PACKAGE_DIR, 'VERSION')) as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={NAME: ['VERSION']},
    install_requires=list_reqs(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
