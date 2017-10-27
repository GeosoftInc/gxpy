### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXREG import GXREG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXITR:
    """
    GXITR class.

    The `GXITR` class provides access to `GXITR` files. An `GXITR` file maps
    ranges of values to specific colors. The `GXITR` object is typically
    used in conjunction with `GXMVIEW` objects (see `GXMVIEW` and `GXMVU`).

    **Note:**

    Histogram ranges and color zone ranges
    
    Histogram bins are defined with inclusive minima and exclusive maxima;
    for instance if Min = 0 and Inc = 1, then the second bin would include
    all values z such that  0 <= z < 1 (the first bin has all values < 0).
    
    Color zones used in displaying grids (`GXITR`, ZON etc...) are the
    opposite, with exclusive minima and inclusive maxima.
    For instance, if a zone is defined from 0 to 1, then it would
    contain all values of z such that 0 < z <= 1.
    
    These definitions mean that it is impossible to perfectly assign
    `GXITR` colors to individual bars of a histogram. The best work-around
    when the data values are integers is to define the color zones using
    0.5 values between the integers. A general work-around is to make the
    number of histogram bins much larger than the number of color zones.
    
    The `ITR_NULL` is used to hold a NULL handle to an `GXITR` class.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapITR(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXITR`
        
        :returns: A null `GXITR`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXITR` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXITR`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def change_brightness(self, brt):
        """
        Change the brightness.

        **Note:**

        0.0 brightness does nothing.
        -1.0 to 0.0 makes colors darker, -1.0 is black
        0.0 to 1.0 makes colors lighter, 1.0 is white
        """
        self._wrapper.change_brightness(brt)
        




    def color_vv(self, vv_d, vv_c):
        """
        Get color transform of a `GXVV`.

        **Note:**

        If the input value is a dummy, then the output color
        is 0 (no color).
        """
        self._wrapper.color_vv(vv_d._wrapper, vv_c._wrapper)
        




    def copy(self, it_rs):
        """
        Copies ITRs
        """
        self._wrapper.copy(it_rs._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create an `GXITR` object
        """
        ret_val = gxapi_cy.WrapITR.create(GXContext._get_tls_geo())
        return GXITR(ret_val)



    @classmethod
    def create_file(cls, file):
        """
        Create an `GXITR` object from an itr, tbl, zon, lut file.
        """
        ret_val = gxapi_cy.WrapITR.create_file(GXContext._get_tls_geo(), file.encode())
        return GXITR(ret_val)



    @classmethod
    def create_img(cls, img, tbl, zone, contour):
        """
        Create an `GXITR` for an image.

        **Note:**

        The `ITR_ZONE_DEFAULT` model will ask the `GXIMG` to provide
        a model if it can.
        
        If a shaded relief model is selected, a shaded image
        will be created and a shaded image file will be created with
        the same name as the original grid but with the suffux "_s"
        added to the name part of the grid.
        """
        ret_val = gxapi_cy.WrapITR.create_img(GXContext._get_tls_geo(), img._wrapper, tbl.encode(), zone, contour)
        return GXITR(ret_val)



    @classmethod
    def create_map(cls, map, name):
        """
        Create `GXITR` from Map with `GXAGG` Group name.
        """
        ret_val = gxapi_cy.WrapITR.create_map(GXContext._get_tls_geo(), map._wrapper, name.encode())
        return GXITR(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create an `GXITR` object from a `GXBF`
        """
        ret_val = gxapi_cy.WrapITR.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXITR(ret_val)






    def equal_area(self, st, contour):
        """
        Calculate an equal area transform.
        """
        self._wrapper.equal_area(st._wrapper, contour)
        




    def get_data_limits(self, min, max):
        """
        Get `GXITR` max/min data limits.

        **Note:**

        In some ITRs, especially those defined and
        embedded inside grid (`GXIMG`) objects, the
        actual data minimum and maximum values are
        stored. This function retrieves those values.
        This is NOT true of all `GXITR` objects, and in
        those cases dummy values will be returned.
        """
        min.value, max.value = self._wrapper.get_data_limits(min.value, max.value)
        




    def get_reg(self):
        """
        Get the `GXITR`'s `GXREG`
        """
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_zone_color(self, zone, color):
        """
        Get the color in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-1, where N is the size of the `GXITR`.
        """
        color.value = self._wrapper.get_zone_color(zone, color.value)
        




    def color_value(self, val):
        """
        Transform single data value to color
        """
        ret_val = self._wrapper.color_value(val)
        return ret_val




    def get_size(self):
        """
        Get the number of zones in an `GXITR`
        """
        ret_val = self._wrapper.get_size()
        return ret_val




    def get_zone_model_type(self):
        """
        Get the `GXITR` zone model (e.g. Linear, LogLin, Equal Area).

        **Note:**

        This function may be used to determine if a color
        transform is included in an `GXITR`.
        """
        ret_val = self._wrapper.get_zone_model_type()
        return ret_val




    def linear(self, min, max, contour):
        """
        Calculate a linear transform.
        """
        self._wrapper.linear(min, max, contour)
        




    def load_a(self, file):
        """
        Load to an ASCII file, ZON, TBL or ER-Mapper LUT
        """
        self._wrapper.load_a(file.encode())
        




    def log_linear(self, min, max, contour):
        """
        Calculate a log transform.

        **Note:**

        The function name is a misnomer. This is a pure log transform.
        """
        self._wrapper.log_linear(min, max, contour)
        




    def normal(self, std_dev, mean, exp, contour):
        """
        Calculate a normal distribution transform.
        """
        self._wrapper.normal(std_dev, mean, exp, contour)
        




    def power_zone(self, pow):
        """
        Modified `GXITR` zone values to 10 (or e) raized to the power of the values
        """
        self._wrapper.power_zone(pow)
        




    def get_brightness(self):
        """
        Get the brightness setting of the `GXITR`

        **Note:**

        Brightness can range from -1.0 (black) to 1.0 (white).
        This brightness control is relative to the normal color
        when the `GXITR` is created.

        .. seealso::

            `change_brightness`, `GXAGG.get_brightness`, `GXAGG.change_brightness`
        """
        ret_val = self._wrapper.get_brightness()
        return ret_val




    def get_zone_value(self, zone):
        """
        Get the value in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-2, where N is the size of the `GXITR`.
        """
        ret_val = self._wrapper.get_zone_value(zone)
        return ret_val




    def save_a(self, file):
        """
        Save to an ASCII file, ZON, TBL or ER-Mapper LUT
        """
        self._wrapper.save_a(file.encode())
        




    def save_file(self, file):
        """
        Save to any type (based on the extension of the input file name).
        """
        self._wrapper.save_file(file.encode())
        




    def serial(self, bf):
        """
        Serialize an `GXITR` to a `GXBF`
        """
        self._wrapper.serial(bf._wrapper)
        



    @classmethod
    def set_agg_map(cls, map, name, itr):
        """
        Set `GXITR` to an `GXAGG` in map

        **Note:**

        See the `create_map` function
        """
        gxapi_cy.WrapITR.set_agg_map(GXContext._get_tls_geo(), map._wrapper, name.encode(), itr._wrapper)
        




    def set_bright_contrast(self, brt, con):
        """
        Set the brightness of the `GXITR` colors

        **Note:**

        Brightness settings:
        0.0   - black
        0.5   - normal (no change)
        1.0   - white
        
        Contrast
        0.0   - flat
        1.0   - full contrast (normal)
        """
        self._wrapper.set_bright_contrast(brt, con)
        




    def set_color_model(self, model):
        """
        Set the color model of an `GXITR`.
        """
        self._wrapper.set_color_model(model)
        




    def set_data_limits(self, min, max):
        """
        Set `GXITR` max/min data limits.
        """
        self._wrapper.set_data_limits(min, max)
        




    def set_size(self, zones):
        """
        Set the number of zones in an `GXITR`
        """
        self._wrapper.set_size(zones)
        




    def set_zone_color(self, zone, color):
        """
        Set the color in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-1, where N is the size of the `GXITR`.
        """
        self._wrapper.set_zone_color(zone, color)
        




    def set_zone_value(self, zone, value):
        """
        Set the value in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-2, where N is the size of the `GXITR`.
        """
        self._wrapper.set_zone_value(zone, value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer