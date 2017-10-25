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
class GXST:
    """
    GXST class.

    Mono-variate statistics. The :class:`GXST` class is used to accumulate statistical
    information about a set of data. This class is usually used in conjunction
    with others. For instance, Stat_DU (see :class:`GXDU`) will add a channel's
    data to the :class:`GXST` object, and sComputeST_IMG (see :class:`GXIMG`) will compute
    statistics for a grid.

    **Note:**

    *** Histogram ranges and color zone ranges ***
    
    Histogram bins are defined with inclusive minima and exclusive maxima;
    for instance if Min = 0 and Inc = 1, then the second bin would include
    all values z such that  0 >= z > 1 (the first bin has all values < 0).
    
    Color zones used in displaying grids (:class:`GXITR`, ZON etc...) are the
    opposite, with exclusive minima and inclusive maxima.
    For instance, if a zone is defined from 0 to 1, then it would
    contain all values of z such that 0 > z >= 1.
    
    These definitions mean that it is impossible to perfectly assign
    :class:`GXITR` colors to individual bars of a histogram. The best work-around
    when the data values are integers is to define the color zones using
    0.5 values between the integers. A general work-around is to make the
    number of histogram bins much larger than the number of color zones.
    
    See also  :class:`GXST2` (bi-variate statistics)
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapST(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXST':
        """
        A null (undefined) instance of :class:`GXST`
        
        :returns: A null :class:`GXST`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXST` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXST`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls) -> 'GXST':
        ret_val = gxapi_cy.WrapST.create(GXContext._get_tls_geo())
        return GXST(ret_val)



    @classmethod
    def create_exact(cls) -> 'GXST':
        ret_val = gxapi_cy.WrapST.create_exact(GXContext._get_tls_geo())
        return GXST(ret_val)




    def data(self, p2: float) -> None:
        self._wrapper.data(p2)
        




    def data_vv(self, p2: 'GXVV') -> None:
        self._wrapper.data_vv(p2._wrapper)
        






    def get_histogram_bins(self, p2: 'GXVV') -> None:
        self._wrapper.get_histogram_bins(p2._wrapper)
        




    def get_histogram_info(self, p2: int_ref, p3: float_ref, p4: float_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_histogram_info(p2.value, p3.value, p4.value)
        




    def histogram(self, p2: int) -> None:
        self._wrapper.histogram(p2)
        




    def histogram2(self, p2: int, p3: float, p4: float) -> None:
        self._wrapper.histogram2(p2, p3, p4)
        




    def equivalent_percentile(self, p2: float) -> float:
        ret_val = self._wrapper.equivalent_percentile(p2)
        return ret_val




    def equivalent_value(self, p2: float) -> float:
        ret_val = self._wrapper.equivalent_value(p2)
        return ret_val




    def reset(self) -> None:
        self._wrapper.reset()
        




    def get_info(self, p2: int) -> float:
        ret_val = self._wrapper.get_info(p2)
        return ret_val



    @classmethod
    def get_norm_prob(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapST.get_norm_prob(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def get_norm_prob_x(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapST.get_norm_prob_x(GXContext._get_tls_geo(), p1)
        return ret_val




    def normal_test(self) -> float:
        ret_val = self._wrapper.normal_test()
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer