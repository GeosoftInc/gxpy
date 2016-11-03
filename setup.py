# coding = utf-8

import json
from os.path import dirname, join
from setuptools import setup

with open('geosoft/pkg_info.json') as fp:
    _info = json.load(fp)

def read(fname):
    return open(join(dirname(__file__), fname)).read()

if _info['branch'] == 'release':
    dev_status_classifier = "Development Status :: 5 - Production/Stable"
    version_tag = _info['version']
else:
    dev_status_classifier = "Development Status :: 4 - Beta"
    version_tag = "{}.{}".format(_info['version'], _info['branch'])

setup(
    name='geosoft',
    version=version_tag,
    description='Geosoft GX API module for Python',
    long_description=read('README.rst'),
    author='Geosoft Inc.',
    author_email='support@geosoft.com',
    url='https://github.com/GeosoftInc/gxpy',
    license='BSD',
    install_requires=[
        'numpy>=1.7',
        'jdcal'
    ],
    packages=[
        'geosoft',
        'geosoft.gxpy'
    ],
    package_data={'geosoft': ['*.key', '*.dll', '*.pyd', '*.json', '*.zip']},
    test_suite="geosoft.gxpy.tests",
    classifiers=[
        dev_status_classifier,
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
    ],
    )

