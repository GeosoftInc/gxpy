### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSURFACEITEM:
    """
    GXSURFACEITEM class.

    The :class:`geosoft.gxapi.GXSURFACEITEM` allows you to create, read and alter Geosurface files (``*.geosoft_surface``).
    A Geosurface file can contain one or more surface items (see :class:`geosoft.gxapi.GXSURFACE` class). A surface item can
    contains one or more triangular polyhedral meshes.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSURFACEITEM(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXSURFACEITEM`
        
        :returns: A null :class:`geosoft.gxapi.GXSURFACEITEM`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXSURFACEITEM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXSURFACEITEM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2):
        """
        Create a :class:`geosoft.gxapi.GXSURFACEITEM`
        """
        ret_val = gxapi_cy.WrapSURFACEITEM.create(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return GXSURFACEITEM(ret_val)






    def get_guid(self, p2):
        """
        Gets the GUID of the surface item.

        **Note:**

        The value returned by this call will not be valid for newly created items until after a call to AddSurfaceItem_SURFACE.
        """
        p2.value = self._wrapper.get_guid(p2.value.encode())
        




    def set_properties(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Sets the properties of the surface item.
        """
        self._wrapper.set_properties(p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8.encode(), p9)
        




    def set_properties_ex(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Sets the properties of the surface item (includes new properties introduced in 8.5).
        """
        self._wrapper.set_properties_ex(p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8.encode(), p9, p10, p11)
        




    def get_properties(self, p2, p4, p6, p8, p10, p11, p13, p15):
        """
        Gets the properties of the surface item.
        """
        p2.value, p4.value, p6.value, p8.value, p10.value, p11.value, p13.value, p15.value = self._wrapper.get_properties(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value.encode(), p10.value, p11.value.encode(), p13.value.encode(), p15.value)
        




    def get_properties_ex(self, p2, p4, p6, p8, p10, p11, p13, p15, p16, p17):
        """
        Gets the properties of the surface item  (includes new properties introduced in 8.5).
        """
        p2.value, p4.value, p6.value, p8.value, p10.value, p11.value, p13.value, p15.value, p16.value, p17.value = self._wrapper.get_properties_ex(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value.encode(), p10.value, p11.value.encode(), p13.value.encode(), p15.value, p16.value, p17.value)
        




    def set_default_render_properties(self, p2, p3, p4):
        """
        Sets default render properties of the surface item.
        """
        self._wrapper.set_default_render_properties(p2, p3, p4)
        




    def get_default_render_properties(self, p2, p3, p4):
        """
        Gets default render properties of the surface item.
        """
        p2.value, p3.value, p4.value = self._wrapper.get_default_render_properties(p2.value, p3.value, p4.value)
        




    def num_components(self):
        """
        Get the number of components in the surface item.
        """
        ret_val = self._wrapper.num_components()
        return ret_val




    def add_mesh(self, p2, p3, p4, p5, p6, p7):
        """
        Adds a triangular polyhedral mesh component to the surface item.
        """
        ret_val = self._wrapper.add_mesh(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper)
        return ret_val




    def get_mesh(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Gets a triangular polyhedral mesh of a component in the surface item.
        """
        self._wrapper.get_mesh(p2, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def get_extents(self, p2, p3, p4, p5, p6, p7):
        """
        Get the spatial range of the the surface item.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_mesh_info(self, p2, p3, p4, p5, p6, p7):
        """
        Gets information about a triangular polyhedral mesh component in the surface item.
        """
        p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_mesh_info(p2, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_info(self, p2, p3, p4, p5):
        """
        Gets information about the surface item.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_info(p2.value, p3.value, p4.value, p5.value)
        




    def get_geometry_info(self, p2, p3):
        """
        Get the total number of vertices and triangles of all mesh components in item.
        """
        p2.value, p3.value = self._wrapper.get_geometry_info(p2.value, p3.value)
        




    def compute_extended_info(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Compute more information (including validation) about of all mesh components in the surface item.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.compute_extended_info(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer