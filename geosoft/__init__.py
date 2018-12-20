# coding = utf-8

import json
from os.path import dirname, join

import logging

mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.WARNING)

with open(join(dirname(__file__), 'pkg_info.json')) as fp:
    _info = json.load(fp)

__version__ = "{}{}".format(_info['version'], _info['pre-release'])
version = __version__

__all__ = ['gxapi', 'gxpy']


class GXRuntimeError(RuntimeError):
    """
    A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_
    which is the base class for any runtime type error originating from the Geosoft Python APIS

    .. versionadded:: 9.1
    """

    def __init__(self, message):
        super(RuntimeError, self).__init__(message)
