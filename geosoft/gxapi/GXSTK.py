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
class GXSTK:
    """
    GXSTK class.

    The :class:`geosoft.gxapi.GXSTK` class is used for plotting a single data profile in
    an :class:`geosoft.gxapi.GXMVIEW`. The :class:`geosoft.gxapi.GXMSTK` class (see :class:`geosoft.gxapi.GXMSTK`) is used to plot
    multiple :class:`geosoft.gxapi.GXSTK` objects to a single map.
    
    Use AddSTK_MSTK fuction to create a :class:`geosoft.gxapi.GXSTK` object before
    using functions in this file
    
    SEE :class:`geosoft.gxapi.GXMSTK` FILE FOR DETAILED DESCRIPTIONS OF ALL FUNCTION PARAMETERS.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSTK(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXSTK`
        
        :returns: A null :class:`geosoft.gxapi.GXSTK`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXSTK` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXSTK`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_trans_parms(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Get transformation parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See above full description of each parameters
        :class:`geosoft.gxapi.GXVV`'s for X channel transformation can be NULL if the
        transformation is log or loglinear. The same for Y channel.
        
        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        p2.value, p3.value, p6.value, p7.value = self._wrapper.get_trans_parms(p2.value, p3.value, p4._wrapper, p5._wrapper, p6.value, p7.value, p8._wrapper, p9._wrapper)
        




    def get_axis_format(self, p2):
        """
        Get axis number display format.

        **Note:**

        By default, :attr:`geosoft.gxapi.DB_CHAN_FORMAT_NORMAL`
        """
        ret_val = self._wrapper.get_axis_format(p2)
        return ret_val




    def get_axis_parms(self, p2, p3, p4, p5, p6, p8, p9, p10, p11, p12):
        """
        Get parameters in :class:`geosoft.gxapi.GXSTK` object relating drawing X/Y axis

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_axis_parms(p2.value, p3.value, p4.value, p5.value, p6.value.encode(), p8.value, p9.value, p10.value, p11.value, p12)
        




    def get_fid_parms(self, p2, p3, p4, p5, p7, p8):
        """
        Get parameters in :class:`geosoft.gxapi.GXSTK` object relating drawing fid ticks

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        p2.value, p3.value, p4.value, p5.value, p7.value, p8.value = self._wrapper.get_fid_parms(p2.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value.encode())
        




    def get_flag(self, p2):
        """
        Get flag indicating part of :class:`geosoft.gxapi.GXSTK` object is to be drawn or not
        """
        ret_val = self._wrapper.get_flag(p2)
        return ret_val




    def get_gen_parms(self, p2, p4, p6, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Get general parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        p2.value, p4.value, p6.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value = self._wrapper.get_gen_parms(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value)
        




    def get_grid_parms(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p13):
        """
        Get background grid parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_grid_parms(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value.encode(), p13)
        




    def get_label_parms(self, p2, p3, p4, p5, p6, p7, p8, p10, p11, p13, p14):
        """
        Get parameters in :class:`geosoft.gxapi.GXSTK` object relating X/Y axis labels

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        Sets the label format to GSF_NORMAL. To override this,
        use the SetAxisFormat_STK function AFTER calling this.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p10.value, p11.value, p13.value = self._wrapper.get_label_parms(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value.encode(), p10.value, p11.value.encode(), p13.value, p14)
        




    def get_profile(self, p2, p3, p4, p5, p7, p8, p9, p10, p11, p13, p14, p16, p17, p19):
        """
        Get profile parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        p2.value, p3.value, p4.value, p5.value, p7.value, p8.value, p9.value, p11.value, p13.value, p14.value, p16.value, p17.value, p19.value = self._wrapper.get_profile(p2.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value, p9.value, p10._wrapper, p11.value.encode(), p13.value, p14.value.encode(), p16.value, p17.value.encode(), p19.value)
        




    def get_profile_ex(self, p2, p3, p4, p5, p7, p8, p9, p10, p11, p12, p14, p15, p17, p18, p20):
        """
        Get profile parameters in :class:`geosoft.gxapi.GXSTK` object (added Break on dummy option)

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        p2.value, p3.value, p4.value, p5.value, p7.value, p8.value, p9.value, p10.value, p12.value, p14.value, p15.value, p17.value, p18.value, p20.value = self._wrapper.get_profile_ex(p2.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value, p9.value, p10.value, p11._wrapper, p12.value.encode(), p14.value, p15.value.encode(), p17.value, p18.value.encode(), p20.value)
        




    def get_symb_parms(self, p2, p4, p5, p7, p9, p10, p11, p12, p13, p14, p15, p16, p18, p19):
        """
        Get parameters in :class:`geosoft.gxapi.GXSTK` object relating drawing symbols

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        p2.value, p4.value, p5.value, p7.value, p9.value, p10.value, p11.value, p12.value, p15.value, p16.value, p18.value, p19.value = self._wrapper.get_symb_parms(p2.value.encode(), p4.value, p5.value.encode(), p7.value.encode(), p9.value, p10.value, p11.value, p12.value, p13._wrapper, p14._wrapper, p15.value, p16.value.encode(), p18.value, p19.value.encode())
        




    def get_title_parms(self, p2, p4, p6, p7, p8, p9, p10, p11, p12, p14, p15, p17):
        """
        Get parameters in :class:`geosoft.gxapi.GXSTK` object relating X/Y axis titles

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        p2.value, p4.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p14.value, p15.value = self._wrapper.get_title_parms(p2.value.encode(), p4.value.encode(), p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value.encode(), p14.value, p15.value.encode(), p17)
        




    def set_flag(self, p2, p3):
        """
        Set flag indicating part of :class:`geosoft.gxapi.GXSTK` object is to be drawn or not
        """
        self._wrapper.set_flag(p2, p3)
        




    def set_array_colors(self, p2):
        """
        Set colors for individual channels in a :class:`geosoft.gxapi.GXVA`, via an :class:`geosoft.gxapi.GXITR`

        **Note:**

        The :class:`geosoft.gxapi.GXITR` is consulted by taking the channel index and dividing
        by the number of channels; hence the :class:`geosoft.gxapi.GXITR` maximum values should
        be in the range: 0 > values >= 1.0.
        """
        self._wrapper.set_array_colors(p2._wrapper)
        




    def set_axis_format(self, p2, p3):
        """
        Set axis number display format.

        **Note:**

        By default, :attr:`geosoft.gxapi.DB_CHAN_FORMAT_NORMAL` is used to display the values,
        or for values > 1.e7, :attr:`geosoft.gxapi.DB_CHAN_FORMAT_EXP`.
        """
        self._wrapper.set_axis_format(p2, p3)
        




    def set_axis_parms(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Set parameters in :class:`geosoft.gxapi.GXSTK` object relating drawing X/Y axis

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._wrapper.set_axis_parms(p2, p3, p4, p5, p6.encode(), p7, p8, p9, p10, p11)
        




    def set_fid_parms(self, p2, p3, p4, p5, p6, p7):
        """
        Set parameters in :class:`geosoft.gxapi.GXSTK` object relating drawing fid ticks

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_fid_parms(p2, p3, p4, p5.encode(), p6, p7.encode())
        




    def set_gen_parms(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Set general parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_gen_parms(p2.encode(), p3.encode(), p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12)
        




    def set_grid_parms(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Set background grid parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._wrapper.set_grid_parms(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11.encode(), p12)
        




    def set_label_parms(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Set parameters in :class:`geosoft.gxapi.GXSTK` object relating X/Y axis labels

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        Sets the label format to GSF_NORMAL. To override this,
        use the SetAxisFormat_STK function AFTER calling this.
        """
        self._wrapper.set_label_parms(p2, p3, p4, p5, p6, p7, p8.encode(), p9, p10.encode(), p11, p12)
        




    def set_line_parm(self, p2):
        """
        Set line parameter (of Y Chan) in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_line_parm(p2)
        




    def set_profile(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Set profile parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_profile(p2, p3, p4, p5.encode(), p6, p7, p8, p9._wrapper, p10.encode(), p11, p12.encode(), p13, p14.encode(), p15)
        




    def set_profile_ex(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Set profile parameters in :class:`geosoft.gxapi.GXSTK` object (added Break on dummy option)

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_profile_ex(p2, p3, p4, p5.encode(), p6, p7, p8, p9, p10._wrapper, p11.encode(), p12, p13.encode(), p14, p15.encode(), p16)
        




    def set_symb_parms(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Set parameters in :class:`geosoft.gxapi.GXSTK` object relating drawing symbols

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_symb_parms(p2.encode(), p3, p4.encode(), p5.encode(), p6, p7, p8, p9, p10._wrapper, p11._wrapper, p12, p13.encode(), p14, p15.encode())
        




    def set_title_parms(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Set parameters in :class:`geosoft.gxapi.GXSTK` object relating X/Y axis titles

        **Note:**

        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        ? mark in the note represent either X and Y
        """
        self._wrapper.set_title_parms(p2.encode(), p3.encode(), p4, p5, p6, p7, p8, p9, p10.encode(), p11, p12.encode(), p13)
        




    def set_trans_parms(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Set transformation parameters in :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        See above full description of each parameters
        :class:`geosoft.gxapi.GXVV`'s for X channel transformation can be NULL if the
        transformation is log or loglinear. The same for Y channel.
        See :class:`geosoft.gxapi.GXMSTK` for detailed description of all function parameters
        """
        self._wrapper.set_trans_parms(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_va_index_start(self, p2):
        """
        Start array profile index labels at 0 or 1.

        **Note:**

        By default, the index labels for array channel profiles
        begin at 0. Use this function to start them at either 0
        or 1.
        """
        self._wrapper.set_va_index_start(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer