### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GX3DN(gxapi_cy.Wrap3DN):
    """
    GX3DN class.

    This class manages the rendering of a 3D view. It allows
    the positioning of the camera, specification of the zoom
    as well as some rendering controls for the axis. It is
    directly related to the `GXMVIEW <geosoft.gxapi.GXMVIEW>` class.
    """

    def __init__(self, handle=0):
        super(GX3DN, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GX3DN <geosoft.gxapi.GX3DN>`
        
        :returns: A null `GX3DN <geosoft.gxapi.GX3DN>`
        :rtype:   GX3DN
        """
        return GX3DN()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def copy(self, source):
        """
        Copy one `GX3DN <geosoft.gxapi.GX3DN>` object to another.
        
        :param source:  Source `GX3DN <geosoft.gxapi.GX3DN>` to Copy from
        :type  source:  GX3DN

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(source)
        



    @classmethod
    def create(cls):
        """
        Creates a `GX3DN <geosoft.gxapi.GX3DN>`.
        

        :returns:    `GX3DN <geosoft.gxapi.GX3DN>` Object
        :rtype:      GX3DN

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.Wrap3DN._create(GXContext._get_tls_geo())
        return GX3DN(ret_val)






    def get_point_of_view(self, distance, declination, inclination):
        """
        Get location of the point we are looking from
        
        :param distance:     Distance from center relative to longest grid dimension (which is 1.0)
        :param declination:  Declination, 0 to 360 CW from Y
        :param inclination:  Inclination, -90 to +90
        :type  distance:     float_ref
        :type  declination:  float_ref
        :type  inclination:  float_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        distance.value, declination.value, inclination.value = self._get_point_of_view(distance.value, declination.value, inclination.value)
        




    def get_scale(self, x, y, z):
        """
        Get the axis relative scales.
        
        :param x:     X Scale
        :param y:     Y Scale
        :param z:     Z Scale
        :type  x:     float_ref
        :type  y:     float_ref
        :type  z:     float_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x.value, y.value, z.value = self._get_scale(x.value, y.value, z.value)
        




    def get_axis_color(self):
        """
        Get the Axis draw color
        

        :returns:     Axis Color
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_axis_color()
        return ret_val




    def get_axis_font(self, font):
        """
        Get the Axis font
        
        :param font:  Font name
        :type  font:  str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        font.value = self._get_axis_font(font.value.encode())
        




    def get_background_color(self):
        """
        Get the window background color
        

        :returns:     Background Color value
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_background_color()
        return ret_val




    def get_render_controls(self, box, axis, label_x, label_y, label_z):
        """
        Get the rendering controls
        
        :param box:      Render Bounding Box (0 or 1)
        :param axis:     Render Axis (0 or 1)
        :param label_x:  Label for X axis
        :param label_y:  Label for Y axis
        :param label_z:  Label for Z axis
        :type  box:      int_ref
        :type  axis:     int_ref
        :type  label_x:  str_ref
        :type  label_y:  str_ref
        :type  label_z:  str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        box.value, axis.value, label_x.value, label_y.value, label_z.value = self._get_render_controls(box.value, axis.value, label_x.value.encode(), label_y.value.encode(), label_z.value.encode())
        




    def get_shading(self):
        """
        Set the shading control on or off
        

        :returns:     Shading On/Off
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_shading()
        return ret_val




    def set_axis_color(self, color):
        """
        Set the Axis draw color
        
        :param color:  Axis Color
        :type  color:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_axis_color(color)
        




    def set_axis_font(self, font):
        """
        Set the Axis font
        
        :param font:  Font name
        :type  font:  str

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_axis_font(font.encode())
        




    def set_background_color(self, color):
        """
        Set the window background color
        
        :param color:  Background Color
        :type  color:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_background_color(color)
        




    def set_point_of_view(self, distance, declination, inclination):
        """
        Set location of the point we are looking from
        
        :param distance:     Distance from center relative to longest grid dimension (which is 1.0)
        :param declination:  Declination, 0 to 360 CW from Y
        :param inclination:  Inclination, -90 to +90
        :type  distance:     float
        :type  declination:  float
        :type  inclination:  float

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_point_of_view(distance, declination, inclination)
        




    def set_render_controls(self, box, axis, label_x, label_y, label_z):
        """
        Set the rendering controls
        
        :param box:      Render Bounding Box (0 or 1)
        :param axis:     Render Axis (0 or 1)
        :param label_x:  Label for X axis
        :param label_y:  Label for Y axis
        :param label_z:  Label for Z axis
        :type  box:      int
        :type  axis:     int
        :type  label_x:  str
        :type  label_y:  str
        :type  label_z:  str

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_render_controls(box, axis, label_x.encode(), label_y.encode(), label_z.encode())
        




    def set_scale(self, x, y, z):
        """
        Set the axis relative scales.
        
        :param x:     X Scale (default 1.0)
        :param y:     Y Scale (default 1.0)
        :param z:     Z Scale (default 1.0)
        :type  x:     float
        :type  y:     float
        :type  z:     float

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** By default all scales are equal (1.0). By setting
        these scales, relative adjustments to the overall
        view of the 3D objects can be made. Note that they
        are relative to each other. Thus, setting the scaling
        to 5,5,5 is the same as 1,1,1. This is typically used
        to exaggerate one scale such as Z (1,1,5).
        """
        self._set_scale(x, y, z)
        




    def set_shading(self, shading):
        """
        Set the shading control on or off
        
        :param shading:  0: Off, 1:  On.
        :type  shading:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_shading(shading)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer