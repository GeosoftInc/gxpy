### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXSURFACEITEM import GXSURFACEITEM


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSURFACE:
    """
    GXSURFACE class.

    The `GXSURFACE` class allows you to create, read and alter Geosurface files (``*.geosoft_surface``).
    A Geosurface file can contain one or more surface items (see `GXSURFACEITEM` class). In turn each item can
    contains one or more triangular polyhedral meshes.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSURFACE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSURFACE`
        
        :returns: A null `GXSURFACE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSURFACE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSURFACE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2):
        """
        Create a new Geosurface file
        """
        ret_val = gxapi_cy.WrapSURFACE.create(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GXSURFACE(ret_val)



    @classmethod
    def open(cls, p1, p2):
        """
        Open a Geosurface file
        """
        ret_val = gxapi_cy.WrapSURFACE.open(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXSURFACE(ret_val)






    def get_ipj(self, p2):
        """
        Get the coordinate system of the `GXSURFACE`.
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def set_ipj(self, p2):
        """
        Change the coordinate system of the `GXSURFACE`.
        """
        self._wrapper.set_ipj(p2._wrapper)
        




    def get_surface_items(self, p2):
        """
        Get the surfaces items in a Geosurface file
        """
        self._wrapper.get_surface_items(p2._wrapper)
        




    def get_surface_item(self, p2):
        """
        Get the an existing surface item from the `GXSURFACE`
        """
        ret_val = self._wrapper.get_surface_item(p2.encode())
        return GXSURFACEITEM(ret_val)




    def add_surface_item(self, p2):
        """
        Add a new surface item to the `GXSURFACE`
        """
        self._wrapper.add_surface_item(p2._wrapper)
        



    @classmethod
    def get_surface_names(cls, p1, p2):
        """
        Get the surface item names in a Geosurface file
        """
        gxapi_cy.WrapSURFACE.get_surface_names(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        



    @classmethod
    def get_closed_surface_names(cls, p1, p2):
        """
        Get the names of closed surface items in a Geosurface file (may return an empty list)
        """
        gxapi_cy.WrapSURFACE.get_closed_surface_names(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        




    def get_extents(self, p2, p3, p4, p5, p6, p7):
        """
        Get the spatial range of all surface items.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def crc(cls, p1, p2, p3):
        """
        Compute an XML CRC of a Geosurface file.
        """
        ret_val, p3.value = gxapi_cy.WrapSURFACE.crc(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value)
        return ret_val



    @classmethod
    def sync(cls, p1):
        """
        Syncronize the Metadata for this Geosurface
        """
        gxapi_cy.WrapSURFACE.sync(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def create_from_dxf(cls, p1, p2, p3):
        """
        Create Geosurface file from DXF file.
        """
        gxapi_cy.WrapSURFACE.create_from_dxf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def create_from_vulcan_triangulation(cls, p1, p2, p3):
        """
        Create Geosurface file from a Maptek Vulcan triangulation file.
        """
        gxapi_cy.WrapSURFACE.create_from_vulcan_triangulation(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode())
        



    @classmethod
    def append_vulcan_triangulation(cls, p1, p2, p3):
        """
        Create new surface from a Maptek Vulcan triangulation file and add to an existing geosurface.
        """
        gxapi_cy.WrapSURFACE.append_vulcan_triangulation(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer