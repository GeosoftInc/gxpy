### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXREG import GXREG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXITR(gxapi_cy.WrapITR):
    """
    GXITR class.

    The `GXITR <geosoft.gxapi.GXITR>` class provides access to `GXITR <geosoft.gxapi.GXITR>` files. An `GXITR <geosoft.gxapi.GXITR>` file maps
    ranges of values to specific colors. The `GXITR <geosoft.gxapi.GXITR>` object is typically
    used in conjunction with `GXMVIEW <geosoft.gxapi.GXMVIEW>` objects (see `GXMVIEW <geosoft.gxapi.GXMVIEW>` and `GXMVU <geosoft.gxapi.GXMVU>`).

    **Note:**

    Histogram ranges and color zone ranges

    Histogram bins are defined with inclusive minima and exclusive maxima;
    for instance if Min = 0 and Inc = 1, then the second bin would include
    all values z such that  0 <= z < 1 (the first bin has all values < 0).

    Color zones used in displaying grids (`GXITR <geosoft.gxapi.GXITR>`, ZON etc...) are the
    opposite, with exclusive minima and inclusive maxima.
    For instance, if a zone is defined from 0 to 1, then it would
    contain all values of z such that 0 < z <= 1.

    These definitions mean that it is impossible to perfectly assign
    `GXITR <geosoft.gxapi.GXITR>` colors to individual bars of a histogram. The best work-around
    when the data values are integers is to define the color zones using
    0.5 values between the integers. A general work-around is to make the
    number of histogram bins much larger than the number of color zones.

    The `ITR_NULL <geosoft.gxapi.ITR_NULL>` is used to hold a NULL handle to an `GXITR <geosoft.gxapi.GXITR>` class.
    """

    def __init__(self, handle=0):
        super(GXITR, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXITR <geosoft.gxapi.GXITR>`
        
        :returns: A null `GXITR <geosoft.gxapi.GXITR>`
        :rtype:   GXITR
        """
        return GXITR()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def change_brightness(self, brt):
        """
        Change the brightness.
        
        :param brt:  -1.0 - black; 0.0 no change; 1.0 white
        :type  brt:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 0.0 brightness does nothing.
        -1.0 to 0.0 makes colors darker, -1.0 is black
        0.0 to 1.0 makes colors lighter, 1.0 is white
        """
        self._change_brightness(brt)
        




    def color_vv(self, vv_d, vv_c):
        """
        Get color transform of a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_d:  Input `GXVV <geosoft.gxapi.GXVV>` of values (none-string)
        :param vv_c:  Output `GXVV <geosoft.gxapi.GXVV>` of colors (type INT)
        :type  vv_d:  GXVV
        :type  vv_c:  GXVV

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the input value is a dummy, then the output color
        is 0 (no color).
        """
        self._color_vv(vv_d, vv_c)
        




    def copy(self, it_rs):
        """
        Copies ITRs
        
        :param it_rs:  `GXITR <geosoft.gxapi.GXITR>` Source
        :type  it_rs:  GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(it_rs)
        



    @classmethod
    def create(cls):
        """
        Create an `GXITR <geosoft.gxapi.GXITR>` object
        

        :returns:    `GXITR <geosoft.gxapi.GXITR>` object
        :rtype:      GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapITR._create(GXContext._get_tls_geo())
        return GXITR(ret_val)



    @classmethod
    def create_file(cls, file):
        """
        Create an `GXITR <geosoft.gxapi.GXITR>` object from an itr, tbl, zon, lut file.
        
        :param file:  File name, type determined from extension
        :type  file:  str

        :returns:     `GXITR <geosoft.gxapi.GXITR>` object
        :rtype:       GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapITR._create_file(GXContext._get_tls_geo(), file.encode())
        return GXITR(ret_val)



    @classmethod
    def create_img(cls, img, tbl, zone, contour):
        """
        Create an `GXITR <geosoft.gxapi.GXITR>` for an image.
        
        :param tbl:      Color table name, NULL for default
        :param zone:     :ref:`ITR_ZONE`
        :param contour:  Color contour interval or `rDUMMY <geosoft.gxapi.rDUMMY>`
        :type  img:      GXIMG
        :type  tbl:      str
        :type  zone:     int
        :type  contour:  float

        :returns:        `GXITR <geosoft.gxapi.GXITR>` object
        :rtype:          GXITR

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `ITR_ZONE_DEFAULT <geosoft.gxapi.ITR_ZONE_DEFAULT>` model will ask the `GXIMG <geosoft.gxapi.GXIMG>` to provide
        a model if it can.

        If a shaded relief model is selected, a shaded image
        will be created and a shaded image file will be created with
        the same name as the original grid but with the suffux "_s"
        added to the name part of the grid.
        """
        ret_val = gxapi_cy.WrapITR._create_img(GXContext._get_tls_geo(), img, tbl.encode(), zone, contour)
        return GXITR(ret_val)



    @classmethod
    def create_map(cls, map, name):
        """
        Create `GXITR <geosoft.gxapi.GXITR>` from Map with `GXAGG <geosoft.gxapi.GXAGG>` Group name.
        
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` on which to place the view
        :param name:  `GXAGG <geosoft.gxapi.GXAGG>` Group name
        :type  map:   GXMAP
        :type  name:  str

        :returns:     `GXITR <geosoft.gxapi.GXITR>` object
        :rtype:       GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapITR._create_map(GXContext._get_tls_geo(), map, name.encode())
        return GXITR(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create an `GXITR <geosoft.gxapi.GXITR>` object from a `GXBF <geosoft.gxapi.GXBF>`
        
        :param bf:  `GXBF <geosoft.gxapi.GXBF>` to serialize from
        :type  bf:  GXBF

        :returns:    `GXITR <geosoft.gxapi.GXITR>` object
        :rtype:      GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapITR._create_s(GXContext._get_tls_geo(), bf)
        return GXITR(ret_val)






    def equal_area(self, st, contour):
        """
        Calculate an equal area transform.
        
        :param st:       Stat object with a histogram
        :param contour:  Color contour interval or dummy for none
        :type  st:       GXST
        :type  contour:  float

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._equal_area(st, contour)
        




    def get_data_limits(self, min, max):
        """
        Get `GXITR <geosoft.gxapi.GXITR>` max/min data limits.
        
        :param min:  Data minimum value (or `rDUMMY <geosoft.gxapi.rDUMMY>` if not set)
        :param max:  Data maximum value (or `rDUMMY <geosoft.gxapi.rDUMMY>` if not set)
        :type  min:  float_ref
        :type  max:  float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** In some ITRs, especially those defined and
        embedded inside grid (`GXIMG <geosoft.gxapi.GXIMG>`) objects, the
        actual data minimum and maximum values are
        stored. This function retrieves those values.
        This is NOT true of all `GXITR <geosoft.gxapi.GXITR>` objects, and in
        those cases dummy values will be returned.
        """
        min.value, max.value = self._get_data_limits(min.value, max.value)
        




    def get_reg(self):
        """
        Get the `GXITR <geosoft.gxapi.GXITR>`'s `GXREG <geosoft.gxapi.GXREG>`
        

        :returns:    `GXREG <geosoft.gxapi.GXREG>` object
        :rtype:      GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_reg()
        return GXREG(ret_val)




    def get_zone_color(self, zone, color):
        """
        Get the color in a zone of the `GXITR <geosoft.gxapi.GXITR>`
        
        :param zone:   Number of the zone to set.
        :param color:  :ref:`MVIEW_COLOR`
        :type  zone:   int
        :type  color:  int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Valid indices are 0 to N-1, where N is the size of the `GXITR <geosoft.gxapi.GXITR>`.
        """
        color.value = self._get_zone_color(zone, color.value)
        




    def color_value(self, val):
        """
        Transform single data value to color
        
        :param val:  Data value
        :type  val:  float

        :returns:    :ref:`MVIEW_COLOR`
        :rtype:      int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._color_value(val)
        return ret_val




    def get_size(self):
        """
        Get the number of zones in an `GXITR <geosoft.gxapi.GXITR>`
        

        :returns:    The number of zones.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_size()
        return ret_val




    def get_zone_model_type(self):
        """
        Get the `GXITR <geosoft.gxapi.GXITR>` zone model (e.g. Linear, LogLin, Equal Area).
        

        :returns:    :ref:`ITR_ZONE_MODEL`
        :rtype:      int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function may be used to determine if a color
        transform is included in an `GXITR <geosoft.gxapi.GXITR>`.
        """
        ret_val = self._get_zone_model_type()
        return ret_val




    def linear(self, min, max, contour):
        """
        Calculate a linear transform.
        
        :param min:      Minimum
        :param max:      Maximum
        :param contour:  Color contour interval or dummy for none
        :type  min:      float
        :type  max:      float
        :type  contour:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._linear(min, max, contour)
        




    def load_a(self, file):
        """
        Load to an ASCII file, ZON, TBL or ER-Mapper LUT
        
        :param file:  File name
        :type  file:  str

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._load_a(file.encode())
        




    def log_linear(self, min, max, contour):
        """
        Calculate a log transform.
        
        :param min:      Minimum ( > 0)
        :param max:      Maximum ( > minimum)
        :param contour:  Color contour interval or dummy for none
        :type  min:      float
        :type  max:      float
        :type  contour:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The function name is a misnomer. This is a pure log transform.
        """
        self._log_linear(min, max, contour)
        




    def normal(self, std_dev, mean, exp, contour):
        """
        Calculate a normal distribution transform.
        
        :param std_dev:  Standard deviation
        :param mean:     Mean
        :param exp:      Expansion, normally 1.0
        :param contour:  Color contour interval or dummy for none
        :type  std_dev:  float
        :type  mean:     float
        :type  exp:      float
        :type  contour:  float

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._normal(std_dev, mean, exp, contour)
        




    def power_zone(self, pow):
        """
        Modified `GXITR <geosoft.gxapi.GXITR>` zone values to 10 (or e) raized to the power of the values
        
        :param pow:  :ref:`ITR_POWER`
        :type  pow:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._power_zone(pow)
        




    def get_brightness(self):
        """
        Get the brightness setting of the `GXITR <geosoft.gxapi.GXITR>`
        

        :returns:    The brightness setting of the `GXITR <geosoft.gxapi.GXITR>`
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Brightness can range from -1.0 (black) to 1.0 (white).
        This brightness control is relative to the normal color
        when the `GXITR <geosoft.gxapi.GXITR>` is created.

        .. seealso::

            `change_brightness <geosoft.gxapi.GXITR.change_brightness>`, `GXAGG.get_brightness <geosoft.gxapi.GXAGG.get_brightness>`, `GXAGG.change_brightness <geosoft.gxapi.GXAGG.change_brightness>`
        """
        ret_val = self._get_brightness()
        return ret_val




    def get_zone_value(self, zone):
        """
        Get the value in a zone of the `GXITR <geosoft.gxapi.GXITR>`
        
        :param zone:  Number of the zone to set.
        :type  zone:  int

        :returns:     The value of the specified zone.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Valid indices are 0 to N-2, where N is the size of the `GXITR <geosoft.gxapi.GXITR>`.
        """
        ret_val = self._get_zone_value(zone)
        return ret_val




    def save_a(self, file):
        """
        Save to an ASCII file, ZON, TBL or ER-Mapper LUT
        
        :param file:  File name
        :type  file:  str

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save_a(file.encode())
        




    def save_file(self, file):
        """
        Save to any type (based on the extension of the input file name).
        
        :param file:  File name
        :type  file:  str

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save_file(file.encode())
        




    def serial(self, bf):
        """
        Serialize an `GXITR <geosoft.gxapi.GXITR>` to a `GXBF <geosoft.gxapi.GXBF>`
        
        :param bf:   `GXBF <geosoft.gxapi.GXBF>` to serialize to
        :type  bf:   GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(bf)
        



    @classmethod
    def set_agg_map(cls, map, name, itr):
        """
        Set `GXITR <geosoft.gxapi.GXITR>` to an `GXAGG <geosoft.gxapi.GXAGG>` in map
        
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` on which to place the view
        :param name:  `GXAGG <geosoft.gxapi.GXAGG>` group name
        :param itr:   `GXITR <geosoft.gxapi.GXITR>` object to set
        :type  map:   GXMAP
        :type  name:  str
        :type  itr:   GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See the `create_map <geosoft.gxapi.GXITR.create_map>` function
        """
        gxapi_cy.WrapITR._set_agg_map(GXContext._get_tls_geo(), map, name.encode(), itr)
        




    def set_bright_contrast(self, brt, con):
        """
        Set the brightness of the `GXITR <geosoft.gxapi.GXITR>` colors
        
        :param brt:  0.0 - black; 0.5 normal; 1.0 white
        :param con:  0.0 - flat; 1.0 normal
        :type  brt:  float
        :type  con:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Brightness settings:
        0.0   - black
        0.5   - normal (no change)
        1.0   - white

        Contrast
        0.0   - flat
        1.0   - full contrast (normal)
        """
        self._set_bright_contrast(brt, con)
        




    def set_color_model(self, model):
        """
        Set the color model of an `GXITR <geosoft.gxapi.GXITR>`.
        
        :param model:  :ref:`ITR_COLOR_MODEL`
        :type  model:  int

        .. versionadded:: 5.0.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_color_model(model)
        



    @classmethod
    def default_color_method(cls):
        """
        Return the user-defined global default color method.
        

        :returns:    One of `ITR_ZONE_EQUALAREA <geosoft.gxapi.ITR_ZONE_EQUALAREA>`, `ITR_ZONE_LINEAR <geosoft.gxapi.ITR_ZONE_LINEAR>`, `ITR_ZONE_NORMAL <geosoft.gxapi.ITR_ZONE_NORMAL>` or `ITR_ZONE_LOGLINEAR <geosoft.gxapi.ITR_ZONE_LOGLINEAR>`
        :rtype:      int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapITR._default_color_method(GXContext._get_tls_geo())
        return ret_val




    def set_data_limits(self, min, max):
        """
        Set `GXITR <geosoft.gxapi.GXITR>` max/min data limits.
        
        :param min:  Data minimum value
        :param max:  Data maximum value
        :type  min:  float
        :type  max:  float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_data_limits(min, max)
        




    def set_size(self, zones):
        """
        Set the number of zones in an `GXITR <geosoft.gxapi.GXITR>`
        
        :param zones:  Number of zones to set `GXITR <geosoft.gxapi.GXITR>` to.
        :type  zones:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_size(zones)
        




    def set_zone_color(self, zone, color):
        """
        Set the color in a zone of the `GXITR <geosoft.gxapi.GXITR>`
        
        :param zone:   Number of the zone to set.
        :param color:  :ref:`MVIEW_COLOR`
        :type  zone:   int
        :type  color:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Valid indices are 0 to N-1, where N is the size of the `GXITR <geosoft.gxapi.GXITR>`.
        """
        self._set_zone_color(zone, color)
        




    def set_zone_value(self, zone, value):
        """
        Set the value in a zone of the `GXITR <geosoft.gxapi.GXITR>`
        
        :param zone:   Number of the zone to set.
        :param value:  The value to set
        :type  zone:   int
        :type  value:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Valid indices are 0 to N-2, where N is the size of the `GXITR <geosoft.gxapi.GXITR>`.
        """
        self._set_zone_value(zone, value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer