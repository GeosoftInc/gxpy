import os
from setuptools import setup

import build_version

product_version = '.'.join(build_version.PRODUCT_VERSION_BLOCK.split(','))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='geosoft',
    version=product_version,
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

