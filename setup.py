import io
import os

from setuptools import find_packages, setup


# Package meta-data.
NAME = 'intime-sdk'
DESCRIPTION = 'Python SDK for InTime API services.'
URL = 'https://github.com/njnur/InTime-Python-SDK'
EMAIL = 'mnjnurrumen@gmail.com'
AUTHOR = 'MD Nurujjaman Nur'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '1.0.0'

# Packages required
REQUIRED = [
    'requests'
]

# Optional packages
EXTRAS = {
    # 'fancy-feature': ['django'],
}

package_root = os.path.abspath(os.path.dirname(__file__))

# README used as the long-description.
try:
    with io.open(os.path.join(package_root, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(package_root, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["docs", "source", "tests", "*.tests", "*.tests.*", "tests.*", ".pypirc"]),
    # For Single a module Package, use this instead of 'packages'
    # py_modules=['module_name'],

    # entry_points={},

    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ]
)
