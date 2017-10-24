### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXFFT:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapFFT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXFFT':
        """
        A null (undefined) instance of :class:`GXFFT`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXFFT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXFFT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def app_dens(self, p2: float, p3: float) -> None:
        self._wrapper.app_dens(p2, p3)
        




    def app_susc(self, p2: float) -> None:
        self._wrapper.app_susc(p2)
        




    def band_pass(self, p2: float, p3: float, p4: int) -> None:
        self._wrapper.band_pass(p2, p3, p4)
        




    def b_worth(self, p2: float, p3: float, p4: int) -> None:
        self._wrapper.b_worth(p2, p3, p4)
        




    def rc_filter(self, p2: float, p3: int) -> None:
        self._wrapper.rc_filter(p2, p3)
        




    def contin(self, p2: float) -> None:
        self._wrapper.contin(p2)
        




    def cos_roll(self, p2: float, p3: float, p4: float, p5: int) -> None:
        self._wrapper.cos_roll(p2, p3, p4, p5)
        



    @classmethod
    def create(cls, p1: 'GXVV', p2: float, p3: int) -> 'GXFFT':
        ret_val = gxapi_cy.WrapFFT.create(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return GXFFT(ret_val)



    @classmethod
    def create_ex(cls, p1: 'GXVV', p2: float, p3: int, p4: float) -> 'GXFFT':
        ret_val = gxapi_cy.WrapFFT.create_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        return GXFFT(ret_val)



    @classmethod
    def create_ref(cls, p1: 'GXVV', p2: float, p3: int) -> 'GXFFT':
        ret_val = gxapi_cy.WrapFFT.create_ref(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return GXFFT(ret_val)



    @classmethod
    def create_ref_ex(cls, p1: 'GXVV', p2: float, p3: int, p4: float, p5: float) -> 'GXFFT':
        ret_val = gxapi_cy.WrapFFT.create_ref_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        return GXFFT(ret_val)






    def gaus(self, p2: float, p3: int) -> None:
        self._wrapper.gaus(p2, p3)
        




    def get_vv(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.get_vv(p2._wrapper, p3._wrapper)
        




    def h_drv(self, p2: float) -> None:
        self._wrapper.h_drv(p2)
        




    def high_pass(self, p2: float, p3: float) -> None:
        self._wrapper.high_pass(p2, p3)
        




    def h_int(self) -> None:
        self._wrapper.h_int()
        




    def inverse(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.inverse(p2._wrapper, p3._wrapper)
        




    def low_pass(self, p2: float) -> None:
        self._wrapper.low_pass(p2)
        




    def red_pol(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.red_pol(p2, p3, p4, p5)
        




    def nyquist(self) -> float:
        ret_val = self._wrapper.nyquist()
        return ret_val




    def samp_incr(self) -> float:
        ret_val = self._wrapper.samp_incr()
        return ret_val




    def wave_incr(self) -> float:
        ret_val = self._wrapper.wave_incr()
        return ret_val




    def set_vv(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.set_vv(p2._wrapper, p3._wrapper)
        




    def spectrum(self, p2: 'GXVV') -> None:
        self._wrapper.spectrum(p2._wrapper)
        




    def v_drv(self, p2: float) -> None:
        self._wrapper.v_drv(p2)
        




    def v_int(self) -> None:
        self._wrapper.v_int()
        




    def write_spectrum(self, p2: 'GXVV', p3: str) -> None:
        self._wrapper.write_spectrum(p2._wrapper, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer