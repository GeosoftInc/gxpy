from . import gxapi_cy

from geosoft.gxapi import GXAPIError

import threading
from threading import current_thread

_tls = threading.local()

class GXContext:
    _gxa_geo = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        _tls._gxa_geo = None
        print("GXContext exit")

    def __del__(self):
        _tls._gxa_geo = None
        print("GXContext deleted")

    def __init__(self, wrapper):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if not tls_geo is None:
            raise GXAPIError("Only one GXContext instance per thread allowed.");
        _tls._gxa_geo = wrapper
        print("GXContext init")

    @classmethod
    def _get_tls_geo(cls):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            raise GXAPIError("A GXContext instance has not been created for current thread yet.");
        return tls_geo

    @classmethod
    def create(cls, application: str, version: int, wind_id: int = 0, flags: int = 0):
        return GXContext(gxapi_cy.WrapPGeo(application, version, wind_id, flags))
         

