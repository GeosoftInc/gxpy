# coding = utf-8

import json
import sys
import tempfile
import shutil
from os import path, remove, environ
from glob import glob
from setuptools import setup
import zipfile

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
            if pythontag == "cp35":
                shutil.copyfile('gxapi_cy.cp35-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp35-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            elif pythontag == "cp36":
                shutil.copyfile('gxapi_cy.cp36-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp36-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            elif pythontag == "cp37":
                shutil.copyfile('gxapi_cy.cp37-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
                shutil.copyfile('gxapi_cy_extend.cp37-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
            break
else:
    # Copy the version we are building for
    py_ver_major_minor = sys.version_info[:2]
    if py_ver_major_minor == (3, 5):
        shutil.copyfile('gxapi_cy.cp35-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp35-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
    elif py_ver_major_minor == (3, 6):
        shutil.copyfile('gxapi_cy.cp36-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp36-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')
    elif py_ver_major_minor == (3, 7):
        shutil.copyfile('gxapi_cy.cp37-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy.pyd')
        shutil.copyfile('gxapi_cy_extend.cp37-win_amd64.pyd', 'geosoft/gxapi/gxapi_cy_extend.pyd')

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
    'geosoft.gxapi': ['geosoft.key', 'gxapi_cy.pyd',  'gxapi_cy_extend.pyd', '*.dll'],
    'geosoft.gxpy._jdcal': ['*.txt', '*.rst'],
    'geosoft.gxpy._xmltodict': ['LICENSE', '*.md'],
    'geosoft.gxpy.user_input': ['*.gx']
}

redist_packages=[
    'geosoft.gxapi.GeosoftRedist',
    'geosoft.gxapi.GeosoftRedist.bin',
    'geosoft.gxapi.GeosoftRedist.csv',
    'geosoft.gxapi.GeosoftRedist.etc',
    'geosoft.gxapi.GeosoftRedist.fonts',
    'geosoft.gxapi.GeosoftRedist.ger',
    'geosoft.gxapi.GeosoftRedist.ini',
    'geosoft.gxapi.GeosoftRedist.tbl',
    'geosoft.gxapi.GeosoftRedist.tbl.Geophysics',
    'geosoft.gxapi.GeosoftRedist.tbl.miscellaneous',
    'geosoft.gxapi.GeosoftRedist.tbl.monochromatic',
    'geosoft.gxapi.GeosoftRedist.tbl.topography'
]

redist_package_data={
    'geosoft.gxapi.GeosoftRedist': ['*'],
    'geosoft.gxapi.GeosoftRedist.bin': ['*'],
    'geosoft.gxapi.GeosoftRedist.csv': ['*'],
    'geosoft.gxapi.GeosoftRedist.etc': ['*'],
    'geosoft.gxapi.GeosoftRedist.fonts': ['*'],
    'geosoft.gxapi.GeosoftRedist.ger': ['*'],
    'geosoft.gxapi.GeosoftRedist.ini': ['*'],
    'geosoft.gxapi.GeosoftRedist.tbl': ['*'],
    'geosoft.gxapi.GeosoftRedist.tbl.Geophysics': ['*'],
    'geosoft.gxapi.GeosoftRedist.tbl.miscellaneous': ['*'],
    'geosoft.gxapi.GeosoftRedist.tbl.monochromatic': ['*'],
    'geosoft.gxapi.GeosoftRedist.tbl.topography': ['*']
}

standalone_dist = None
standalone_temp = None
standalone_user = None
for arg in sys.argv:
    if arg.startswith('--standalone_dist='):
        standalone_dist = arg[18:]
        index = sys.argv.index(arg)
        sys.argv.pop(index)  # Removes the arg

if standalone_dist:
    for arg in sys.argv:
        if arg.startswith('--standalone_temp='):
            standalone_temp = arg[18:]
            index = sys.argv.index(arg)
            sys.argv.pop(index)  # Removes the arg
    for arg in sys.argv:
        if arg.startswith('--standalone_user='):
            standalone_user = arg[18:]
            index = sys.argv.index(arg)
            sys.argv.pop(index)  # Removes the arg
    if not standalone_temp or not standalone_user:
        raise RuntimeError("Need to specify standalone_temp as well as standalone_user directories with standalone_dist.")
    packages.extend(redist_packages)
    package_data = {**package_data, **redist_package_data}

if standalone_dist:
    if path.exists('geosoft/gxapi/GeosoftRedist'):
        shutil.rmtree('geosoft/gxapi/GeosoftRedist')
    zip_ref = zipfile.ZipFile(standalone_dist, 'r')
    zip_ref.extractall('geosoft/gxapi')
    zip_ref.close()

key_file = path.join('geosoft', 'gxapi', 'geosoft.key')
if standalone_dist:
    if path.exists(key_file):
        remove(key_file)
    remove('geosoft/gxapi/geoengine.core.gx_ansi.dll')
    remove('geosoft/gxapi/geoengine.core.gx_u.dll')
    remove('geosoft/gxapi/geoengine.core.gxnet.dll')
    remove('geosoft/gxapi/geoengine.core.gxnetx.dll')
    remove('geosoft/gxapi/geogx.dll')
    remove('geosoft/gxapi/geogx_u.dll')
    remove('geosoft/gxapi/geosoft.desktop.gxnet.dll')
    remove('geosoft/gxapi/geosoft.desktop.gxnetx.dll')
    with open('geosoft/gxapi/GeosoftRedist/geosoft.redist', 'w') as f:
        f.writelines([standalone_user, '\n', standalone_temp, '\n'])

else:
    with open(key_file, 'w') as f:
        use_default_key = True
        for arg in sys.argv:
            if arg.startswith('--use_geosoft_key='):
                index = sys.argv.index(arg)
                sys.argv.pop(index)  # Removes the arg
                geosoft_key = arg[18:]
                f.write(geosoft_key)
                use_default_key = False
                break
        if use_default_key:
            f.write("Core")


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
    install_requires=dependencies,
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

