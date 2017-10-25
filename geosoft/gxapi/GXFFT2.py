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
class GXFFT2:
    """
    GXFFT2 class.

    2-D Fast Fourier Transforms
    These methods now work with an `GXIMG` object, instead of creating
    their own `GXFFT2` object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapFFT2(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXFFT2`
        
        :returns: A null `GXFFT2`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXFFT2` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXFFT2`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def fft2_in(cls, p1, p2, p3):
        """
        `GXFFT2` transform
        """
        gxapi_cy.WrapFFT2.fft2_in(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def filter_pg(cls, p1, p2, p3, p4, p5, p6):
        """
        Apply 2D `GXFFT` filters to data in pager
        """
        gxapi_cy.WrapFFT2.filter_pg(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5, p6)
        



    @classmethod
    def flt(cls, p1, p2, p3):
        """
        `GXFFT2` filter
        """
        gxapi_cy.WrapFFT2.flt(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def flt_inv(cls, p1, p2, p3):
        """
        `GXFFT2` filter and inverse
        """
        gxapi_cy.WrapFFT2.flt_inv(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def pow_spc(cls, p1, p2):
        """
        `GXFFT2` transform power spectrum
        """
        gxapi_cy.WrapFFT2.pow_spc(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def rad_spc(cls, p1, p2):
        """
        `GXFFT2` transform Radially averaged power spectrum
        """
        gxapi_cy.WrapFFT2.rad_spc(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def rad_spc1(cls, p1, p2):
        """
        `GXFFT2` transform Radially averaged power spectrum for one `GXIMG`
        """
        gxapi_cy.WrapFFT2.rad_spc1(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def rad_spc2(cls, p1, p2, p3, p4, p5):
        """
        `GXFFT2` transform Radially averaged power spectrum for two IMGs
        """
        gxapi_cy.WrapFFT2.rad_spc2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def td_xd_y(cls, p1, p2, p3, p4):
        """
        `GXFFT2` filter (calculate T from the derivatives Tx and Ty)
        """
        gxapi_cy.WrapFFT2.td_xd_y(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4)
        



    @classmethod
    def trans_pg(cls, p1, p2):
        """
        Apply 2D `GXFFT` transform to data in pager
        """
        gxapi_cy.WrapFFT2.trans_pg(GXContext._get_tls_geo(), p1._wrapper, p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer