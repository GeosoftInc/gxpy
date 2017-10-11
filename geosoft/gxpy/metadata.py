"""
Geosoft metadata.

:Classes:

    ================= =========================
    :class:`Metadata` metadata
    ================= =========================

.. seealso:: :mod:`geosoft.gxapi.GXMETA`

.. note::

    Regression tests provide usage examples:    
    `vv tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_metadata.py>`_

"""

import geosoft
import numpy as np
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class MetadataException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.metadata`.

    .. versionadded:: 9.3
    """
    pass


class Metadata:
    """
    Metadata handling.


    .. versionadded:: 9.3 added unit_of_measure
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, metadata=None):

        if metadata:
            self._meta = metadata
        else:
            self._meta = {}

    @classmethod
    def from_geosoft_meta(cls, geometa):

        def rep(c, a):
            geometa.get_obj_name(a, sr)
            print('<{}> {}({}) has value? {}'.format(c, sr.value, a, geometa.has_value(c, a)))

        def write_file():
            wa = gxapi.GXWA.create('meta.txt', 0)
            geometa.write_text(wa)

        def iterate_class(c):
            token = geometa.h_get_next_item(c, gxapi.H_META_INVALID_TOKEN)
            if token == gxapi.H_META_INVALID_TOKEN:
                geometa.get_obj_name(c, sr)
                print('{}({}) has no items'.format(sr.value, c))
            while token != gxapi.H_META_INVALID_TOKEN:
                rep(c, token)
                i = geometa.h_get_next_item(c, token)

        sr = gxapi.str_ref()

        iterate_class(-100)

        geosoft = geometa.create_class('geosoft', -100)
        rep(-100, geosoft)
        iterate_class(geosoft)

        a = geometa.create_attrib('maki_float', geosoft, gxapi.META_CORE_TYPE_R8)
        geometa.set_attrib_double(geosoft, a, 9.9)
        rep(geosoft, a)

        b = geometa.create_attrib('maki_empty', geosoft, gxapi.META_CORE_TYPE_String)
        geometa.set_empty_attrib(geosoft, b)
        rep(geosoft, b)

        c = geometa.create_attrib('maki_string', geosoft, gxapi.META_CORE_TYPE_String)
        geometa.set_attrib_string(geosoft, c, 'ian')
        rep(geosoft, c)

        geometa.export_table_csv(geosoft, 'meta.csv')
        write_file()

        data = geometa.create_class('data', geosoft)
        rep(geosoft, data)
        iterate_class(data)

        grid = geometa.create_class('grid', data)
        rep(data, grid)
        iterate_class(grid)


    @property
    def metadata(self):
        return self._meta
