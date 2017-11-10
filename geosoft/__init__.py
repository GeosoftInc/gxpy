# coding = utf-8

import json
import warnings
from os.path import dirname, join

with open(join(dirname(__file__), 'pkg_info.json')) as fp:
    _info = json.load(fp)

__version__ = "{}{}".format(_info['version'], _info['pre-release'])
version = __version__

__all__ = ['gxapi', 'gxpy']

# docstring overrides for C++ classes inside gxapi module

import geosoft.gxapi as gxapi



