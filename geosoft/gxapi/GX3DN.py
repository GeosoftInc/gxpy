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
class GX3DN:
    """
    GX3DN class.

    This class manages the rendering of a 3D view. It allows
    the positioning of the camera, specification of the zoom
    as well as some rendering controls for the axis. It is
    directly related to the :class:`geosoft.gxapi.GXMVIEW` class.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.Wrap3DN(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GX3DN`
        
        :returns: A null :class:`geosoft.gxapi.GX3DN`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GX3DN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GX3DN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, p2):
        """
        Copy one :class:`geosoft.gxapi.GX3DN` object to another.
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls):
        """
        Creates a :class:`geosoft.gxapi.GX3DN`.
        """
        ret_val = gxapi_cy.Wrap3DN.create(GXContext._get_tls_geo())
        return GX3DN(ret_val)






    def get_point_of_view(self, p2, p3, p4):
        """
        Get location of the point we are looking from
        """
        p2.value, p3.value, p4.value = self._wrapper.get_point_of_view(p2.value, p3.value, p4.value)
        




    def get_scale(self, p2, p3, p4):
        """
        Get the axis relative scales.
        """
        p2.value, p3.value, p4.value = self._wrapper.get_scale(p2.value, p3.value, p4.value)
        




    def get_axis_color(self):
        """
        Get the Axis draw color
        """
        ret_val = self._wrapper.get_axis_color()
        return ret_val




    def get_axis_font(self, p2):
        """
        Get the Axis font
        """
        p2.value = self._wrapper.get_axis_font(p2.value.encode())
        




    def get_background_color(self):
        """
        Get the window background color
        """
        ret_val = self._wrapper.get_background_color()
        return ret_val




    def get_render_controls(self, p2, p3, p4, p6, p8):
        """
        Get the rendering controls
        """
        p2.value, p3.value, p4.value, p6.value, p8.value = self._wrapper.get_render_controls(p2.value, p3.value, p4.value.encode(), p6.value.encode(), p8.value.encode())
        




    def get_shading(self):
        """
        Set the shading control on or off
        """
        ret_val = self._wrapper.get_shading()
        return ret_val




    def set_axis_color(self, p2):
        """
        Set the Axis draw color
        """
        self._wrapper.set_axis_color(p2)
        




    def set_axis_font(self, p2):
        """
        Set the Axis font
        """
        self._wrapper.set_axis_font(p2.encode())
        




    def set_background_color(self, p2):
        """
        Set the window background color
        """
        self._wrapper.set_background_color(p2)
        




    def set_point_of_view(self, p2, p3, p4):
        """
        Set location of the point we are looking from
        """
        self._wrapper.set_point_of_view(p2, p3, p4)
        




    def set_render_controls(self, p2, p3, p4, p5, p6):
        """
        Set the rendering controls
        """
        self._wrapper.set_render_controls(p2, p3, p4.encode(), p5.encode(), p6.encode())
        




    def set_scale(self, p2, p3, p4):
        """
        Set the axis relative scales.

        **Note:**

        By default all scales are equal (1.0). By setting
        these scales, relative adjustments to the overall
        view of the 3D objects can be made. Note that they
        are relative to each other. Thus, setting the scaling
        to 5,5,5 is the same as 1,1,1. This is typically used
        to exaggerate one scale such as Z (1,1,5).
        """
        self._wrapper.set_scale(p2, p3, p4)
        




    def set_shading(self, p2):
        """
        Set the shading control on or off
        """
        self._wrapper.set_shading(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
    def test(self):
        print("test")
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer