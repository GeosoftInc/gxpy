from . import gxapi_cy

from geosoft.gxapi import GXAPIError, int_ref

import threading
from threading import current_thread

_tls = threading.local()

class GXContext:
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._release_tls_geo:
            _tls._gxa_geo = None
        #print("GXContext exit")

    def __del__(self):
        if self._release_tls_geo:
            _tls._gxa_geo = None
        #print("GXContext deleted")

    def __init__(self, wrapper):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            _tls._gxa_geo = wrapper
            self._release_tls_geo = True
        else:
            self._release_tls_geo = False
        #print("GXContext init")

    @classmethod
    def _get_tls_geo(cls):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            raise GXAPIError("A GXContext instance has not been created for current thread yet, or the original context has been released.");
        return tls_geo

    @classmethod
    def create(cls, application, version, wind_id = 0, flags = 0):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            p_geo = gxapi_cy.WrapPGeo()
            p_geo._create(application, version, wind_id, flags)
            return GXContext(p_geo)
        else:
            return GXContext(tls_geo)

    @classmethod
    def _create_internal(cls, internal_p_geo):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if not tls_geo is None:
            raise GXAPIError("Illegal call to GXContext._create_internal. An instance was already instantiated for this thread.");
        p_geo = gxapi_cy.WrapPGeo()
        p_geo._create_internal(internal_p_geo)
        return GXContext(p_geo)

    @classmethod
    def _internal_p(cls):
        p_geo = GXContext._get_tls_geo()
        return p_geo._internal_p()

    def get_main_wnd_id(self):
        p_geo = GXContext._get_tls_geo()
        return p_geo.get_main_wnd()

    def get_active_wnd_id(self):
        p_geo = GXContext._get_tls_geo()
        return p_geo.get_active_wnd()

    def enable_application_windows(self, enable):
        p_geo = GXContext._get_tls_geo()
        return p_geo.enable_application_windows(enable)


    def has_ui_console(self):
        return True # TODO 
    
    def is_ui_console_visible(self):
        return True # TODO 

    def show_ui_console(self, show):
        pass # TODO

    def clear_ui_console(self, show):
        pass # TODO
