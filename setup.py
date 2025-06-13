#  Copyright (c) 2025 Bentley Systems, Incorporated. All rights reserved.
# coding = utf-8

import json
import sys
import shutil
from os import path, remove, environ
from glob import glob
from setuptools import setup

with open('geosoft/pkg_info.json') as fp:
    _info = json.load(fp)

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

version_tag = "{}{}".format(_info['version'], _info['pre-release'])

if _info['pre-release'] == '':
    dev_status_classifier = "Development Status :: 5 - Production/Stable"
else:
    dev_status_classifier = "Development Status :: 4 - Beta"


for f in glob("geosoft/*.pyd"):
    try:
        remove(f)
    except PermissionError as e:
        raise Exception("An application is using a file we need to change: \n {}".format(str(e)))


dependencies = ['numpy', 'pandas', 'requests']
if 'bdist_wheel' in sys.argv:
    # Have to specify python-tag to specify which module
    for arg in sys.argv:
        if arg.startswith('--python-tag='):
            pythontag = arg[13:]
            if pythontag == "cp39":
                shutil.copyfile('gxapi_cy.cp39-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp39-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            elif pythontag == "cp310":
                shutil.copyfile('gxapi_cy.cp310-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp310-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            elif pythontag == "cp311":
                shutil.copyfile('gxapi_cy.cp311-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp311-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            elif pythontag == "cp312":
                shutil.copyfile('gxapi_cy.cp312-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp312-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            elif pythontag == "cp313":
                shutil.copyfile('gxapi_cy.cp313-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp313-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            break
else:
    # Copy the version we are building for
    py_ver_major_minor = sys.version_info[:2]
    if py_ver_major_minor == (3, 9):
        shutil.copyfile('gxapi_cy.cp39-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp39-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
    elif py_ver_major_minor == (3, 10):
        shutil.copyfile('gxapi_cy.cp310-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp310-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
    elif py_ver_major_minor == (3, 11):
        shutil.copyfile('gxapi_cy.cp311-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp311-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
    elif py_ver_major_minor == (3, 12):
        shutil.copyfile('gxapi_cy.cp312-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp312-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
    elif py_ver_major_minor == (3, 13):
        shutil.copyfile('gxapi_cy.cp313-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp313-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
packages=[
    'geosoft',
    'geosoft.gxapi',
    'geosoft.gxpy',
    'geosoft.gxpy._jdcal',
    'geosoft.gxpy._xmltodict',
    'geosoft.gxpy.user_input'
]

package_data={
    'geosoft': ['*.json'],
    'geosoft.gxapi': ['gxapi_cy.pyd',  'gxapi_cy_extend.pyd', '*.dll'],
    'geosoft.gxpy._jdcal': ['*.txt', '*.rst'],
    'geosoft.gxpy._xmltodict': ['LICENSE', '*.md'],
    'geosoft.gxpy.user_input': ['*.gx']
}

install_requires=[
    "numpy>=2.2.1", 
    "pandas>=2.2.3", 
    "requests>=2.31.0",
    "jdcal>=1.3"
]

if sys.version_info >= (3, 12):
    install_requires.append('setuptools>=75.8.0')

setup(
    name='geosoft',
    version=version_tag,
    description='Geosoft GX API module for Python',
    long_description=read('README.md'),
    author='Geosoft Inc.',
    author_email='support@geosoft.com',
    platforms=["win_amd64"],
    url='https://github.com/GeosoftInc/gxpy',
    license='BSD',
    install_requires=install_requires,
    packages=packages,
    package_data=package_data,
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

