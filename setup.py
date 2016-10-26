# coding = utf-8

import json
from os.path import dirname, join
from setuptools import setup

with open('geosoft/pkg_info.json') as fp:
    _info = json.load(fp)

def read(fname):
    return open(join(dirname(__file__), fname)).read()

if _info['branch'] == 'release':
    version_tag = _info['version']
else:
    version_tag = "{}.{}0".format(_info['version'], _info['branch'])

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
          'jdcal',
      ],
    packages=['geosoft',
      'geosoft.gxpy',
      'geosoft.gxpy.gx',
      'geosoft.gxpy.system',
      'geosoft.gxpy.om',
	  'geosoft.gxpy.vv',
	  'geosoft.gxpy.grd',
	  'geosoft.gxpy.gdb',
	  'geosoft.gxpy.ipj',
      'geosoft.gxpy.utility'],
    package_data={'geosoft': ['*.key', '*.dll', '*.pyd']},
    classifiers=[
        "Development Status :: 4 - Beta", #TODO Upgrade to production and review other classifiers (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
    ],
    )

