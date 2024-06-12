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
class GXCSYMB3D(gxapi_cy.WrapCSYMB3D):
    """
    GXCSYMB3D class.

    This class is used for generating and modifying 3D colored symbol objects.
    Symbols are assigned colors based on their Z values and a zone, Aggregate
    or `GXITR <geosoft.gxapi.GXITR>` file which defines what colors are associated with different ranges
    of Z values. The position of a symbol is defined by its X,Y,Z coordinates.
    """

    def __init__(self, handle=0):
        super(GXCSYMB3D, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXCSYMB3D <geosoft.gxapi.GXCSYMB3D>`
        
        :returns: A null `GXCSYMB3D <geosoft.gxapi.GXCSYMB3D>`
        :rtype:   GXCSYMB3D
        """
        return GXCSYMB3D()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Create and Destroy


    @classmethod
    def create(cls, size, colour):
        """
        Create a `GXCSYMB3D <geosoft.gxapi.GXCSYMB3D>`.
        
        :param size:    Symbol size (> 0.0)
        :param colour:  colour to use for the fixed colour
        :type  size:    float
        :type  colour:  int

        :returns:       `GXCSYMB3D <geosoft.gxapi.GXCSYMB3D>` handle
        :rtype:         GXCSYMB3D

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The default object uses fixed size and colour.
        """
        ret_val = gxapi_cy.WrapCSYMB3D._create(GXContext._get_tls_geo(), size, colour)
        return GXCSYMB3D(ret_val)






# Data



    def add_locations(self, vv_x, vv_y, vv_z):
        """
        Add x,y,z locations to a CSYMB3D object.
        
        :param vv_x:     `GXVV <geosoft.gxapi.GXVV>` for X locations
        :param vv_y:     `GXVV <geosoft.gxapi.GXVV>` for Y locations
        :param vv_z:     `GXVV <geosoft.gxapi.GXVV>` for Z locations
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  vv_z:     GXVV

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_locations(vv_x, vv_y, vv_z)
        




    def add_color_data(self, vv_data):
        """
        Add data for colors to a CSYMB3D object.
        
        :param vv_data:  `GXVV <geosoft.gxapi.GXVV>` for colour data values.
        :type  vv_data:  GXVV

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To use these values, add a colour transform using the SetITR function.
        Ensure you add an equal number of locations.
        """
        self._add_color_data(vv_data)
        




    def add_size_data(self, vv_data):
        """
        Add data for sizes to a CSYMB3D object.
        
        :param vv_data:  `GXVV <geosoft.gxapi.GXVV>` for size data values.
        :type  vv_data:  GXVV

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To use these values, call the SetSizeScale or SetSizeMinMax functions.
        Ensure you add an equal number of locations.
        """
        self._add_size_data(vv_data)
        




    def get_locations(self, vv_x, vv_y, vv_z):
        """
        Get x,y,z locations from a color symbol object.
        
        :param vv_x:     `GXVV <geosoft.gxapi.GXVV>` for X locations
        :param vv_y:     `GXVV <geosoft.gxapi.GXVV>` for Y locations
        :param vv_z:     `GXVV <geosoft.gxapi.GXVV>` for Z locations
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  vv_z:     GXVV

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_locations(vv_x, vv_y, vv_z)
        




    def get_color_data(self, vv_data):
        """
        Get data for colors from a CSYMB3D object.
        
        :param vv_data:  `GXVV <geosoft.gxapi.GXVV>` for colour data values.
        :type  vv_data:  GXVV

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_color_data(vv_data)
        




    def get_size_data(self, vv_data):
        """
        Get data for sizes from a CSYMB3D object.
        
        :param vv_data:  `GXVV <geosoft.gxapi.GXVV>` for size data values.
        :type  vv_data:  GXVV

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_size_data(vv_data)
        




    def get_st(self, st):
        """
        Get a copy of the CSYMB3D statistics object
        
        :param st:       `GXST <geosoft.gxapi.GXST>` Handle
        :type  st:       GXST

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns all dummies if no values are input with the locations.
        If both colour and size data are present, returns the colour ST.
        """
        self._get_st(st)
        




    def statistics(self, st):
        """
        Add the CSYMB values to a statistics object
        
        :param st:       `GXST <geosoft.gxapi.GXST>` Handle
        :type  st:       GXST

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns all dummies if no values are input with the locations.
        If both colour and size data are present, uses the colour data.
        """
        self._statistics(st)
        




# Colours



    def set_fixed_color(self, colour):
        """
        Set symbols to a fixed colour
        
        :param colour:   colour to use for the fixed colour
        :type  colour:   int

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_fixed_color(colour)
        




    def get_fixed_color(self):
        """
        Get the fixed colour. There is always one even if we are using an ITR
        
        :rtype:          int

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_fixed_color()
        return ret_val




    def fixed_color(self):
        """
        Return whether colours are fixed (1) or use a transform (0)
        
        :rtype:          int

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._fixed_color()
        return ret_val




    def get_itr(self, itr):
        """
        Get the `GXITR <geosoft.gxapi.GXITR>` of the `GXCSYMB3D <geosoft.gxapi.GXCSYMB3D>`
        
        :param itr:      `GXITR <geosoft.gxapi.GXITR>` object
        :type  itr:      GXITR

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns an empty ITR if fixed colours are being used.
        """
        self._get_itr(itr)
        




    def set_itr(self, itr):
        """
        Set the `GXITR <geosoft.gxapi.GXITR>` of the `GXCSYMB3D <geosoft.gxapi.GXCSYMB3D>`
        
        :param itr:      `GXITR <geosoft.gxapi.GXITR>` object
        :type  itr:      GXITR

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Setting the ITR puts the symbols in colour-transform mode.
        Data for colours must be added using the AddSizeData function.
        """
        self._set_itr(itr)
        




# Symbol, Size and Scaling



    def set_symbol(self, symbol):
        """
        Set the symbol type.
        
        :param symbol:   :ref:`CSYMB3D_SYMBOL`
        :type  symbol:   int

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_symbol(symbol)
        




    def set_fixed_size(self, size):
        """
        Fix the symbol size.
        
        :param size:     Symbol size (> 0.0)
        :type  size:     float

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_fixed_size(size)
        




    def set_size_scale(self, scale, log_scaling, log_minimum):
        """
        Set the symbol size based on a scale.
        
        :param scale:        Symbol scale (> 0.0)
        :param log_scaling:  1 - Use log scaling, 0 - linear scaling
        :param log_minimum:  divide by this value before taking the log (default = 1.0, must be > 0.0
        :type  scale:        float
        :type  log_scaling:  int
        :type  log_minimum:  float

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Data for sizes must be added using the AddSizeData function.
        For log scaling, take the log then apply the scale factor to get the symbol size
        (negative logs do not plot).
        """
        self._set_size_scale(scale, log_scaling, log_minimum)
        




    def set_size_min_max(self, min_size, max_size, log_scaling, log_minimum):
        """
        Scale the symbol size based on value. By default symbols are fixed size
        
        :param min_size:     If defined, make smallest symbol this size (>=0)
        :param max_size:     If defined, make largest symbol this size
        :param log_scaling:  If 1, use log scaling, 0 - linear between min and max
        :param log_minimum:  divide by this value before taking the log (default = 1.0, must be > 0.0)
        :type  min_size:     float
        :type  max_size:     float
        :type  log_scaling:  int
        :type  log_minimum:  float

        .. versionadded:: 2024.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Data for sizes must be added using the AddSizeData function.
        For log scaling, take the log then apply the scaling method to get the symbol size
        (negative logs do not plot).
        """
        self._set_size_min_max(min_size, max_size, log_scaling, log_minimum)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer