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
    directly related to the `GXMVIEW <geosoft.gxapi.GXMVIEW>` class.
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
        A null (undefined) instance of `GX3DN`
        
        :returns: A null `GX3DN`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GX3DN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GX3DN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, source):
        """
        Copy one `GX3DN <geosoft.gxapi.GX3DN>` object to another.
        """
        self._wrapper.copy(source._wrapper)
        



    @classmethod
    def create(cls):
        """
        Creates a `GX3DN <geosoft.gxapi.GX3DN>`.
        """
        ret_val = gxapi_cy.Wrap3DN.create(GXContext._get_tls_geo())
        return GX3DN(ret_val)






    def get_point_of_view(self, distance, declination, inclination):
        """
        Get location of the point we are looking from
        """
        distance.value, declination.value, inclination.value = self._wrapper.get_point_of_view(distance.value, declination.value, inclination.value)
        




    def get_scale(self, x, y, z):
        """
        Get the axis relative scales.
        """
        x.value, y.value, z.value = self._wrapper.get_scale(x.value, y.value, z.value)
        




    def get_axis_color(self):
        """
        Get the Axis draw color
        """
        ret_val = self._wrapper.get_axis_color()
        return ret_val




    def get_axis_font(self, font):
        """
        Get the Axis font
        """
        font.value = self._wrapper.get_axis_font(font.value.encode())
        




    def get_background_color(self):
        """
        Get the window background color
        """
        ret_val = self._wrapper.get_background_color()
        return ret_val




    def get_render_controls(self, box, axis, label_x, label_y, label_z):
        """
        Get the rendering controls
        """
        box.value, axis.value, label_x.value, label_y.value, label_z.value = self._wrapper.get_render_controls(box.value, axis.value, label_x.value.encode(), label_y.value.encode(), label_z.value.encode())
        




    def get_shading(self):
        """
        Set the shading control on or off
        """
        ret_val = self._wrapper.get_shading()
        return ret_val




    def set_axis_color(self, color):
        """
        Set the Axis draw color
        """
        self._wrapper.set_axis_color(color)
        




    def set_axis_font(self, font):
        """
        Set the Axis font
        """
        self._wrapper.set_axis_font(font.encode())
        




    def set_background_color(self, color):
        """
        Set the window background color
        """
        self._wrapper.set_background_color(color)
        




    def set_point_of_view(self, distance, declination, inclination):
        """
        Set location of the point we are looking from
        """
        self._wrapper.set_point_of_view(distance, declination, inclination)
        




    def set_render_controls(self, box, axis, label_x, label_y, label_z):
        """
        Set the rendering controls
        """
        self._wrapper.set_render_controls(box, axis, label_x.encode(), label_y.encode(), label_z.encode())
        




    def set_scale(self, x, y, z):
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
        self._wrapper.set_scale(x, y, z)
        




    def set_shading(self, shading):
        """
        Set the shading control on or off
        """
        self._wrapper.set_shading(shading)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
    def test(self):
        print("test")
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer