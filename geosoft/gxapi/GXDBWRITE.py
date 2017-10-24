### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDBWRITE:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDBWRITE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXDBWRITE':
        """
        A null (undefined) instance of :class:`GXDBWRITE`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDBWRITE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDBWRITE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Create Methods


    @classmethod
    def create(cls, p1: 'GXDB') -> 'GXDBWRITE':
        ret_val = gxapi_cy.WrapDBWRITE.create(GXContext._get_tls_geo(), p1._wrapper)
        return GXDBWRITE(ret_val)



    @classmethod
    def create_xy(cls, p1: 'GXDB') -> 'GXDBWRITE':
        ret_val = gxapi_cy.WrapDBWRITE.create_xy(GXContext._get_tls_geo(), p1._wrapper)
        return GXDBWRITE(ret_val)



    @classmethod
    def create_xyz(cls, p1: 'GXDB') -> 'GXDBWRITE':
        ret_val = gxapi_cy.WrapDBWRITE.create_xyz(GXContext._get_tls_geo(), p1._wrapper)
        return GXDBWRITE(ret_val)






    def add_channel(self, p2: int) -> int:
        ret_val = self._wrapper.add_channel(p2)
        return ret_val




# Data Access Methods



    def get_db(self) -> 'GXDB':
        ret_val = self._wrapper.get_db()
        return GXDB(ret_val)




    def get_vv(self, p2: int) -> 'GXVV':
        ret_val = self._wrapper.get_vv(p2)
        return GXVV(ret_val)




    def get_va(self, p2: int) -> 'GXVA':
        ret_val = self._wrapper.get_va(p2)
        return GXVA(ret_val)




    def get_v_vx(self) -> 'GXVV':
        ret_val = self._wrapper.get_v_vx()
        return GXVV(ret_val)




    def get_v_vy(self) -> 'GXVV':
        ret_val = self._wrapper.get_v_vy()
        return GXVV(ret_val)




    def get_v_vz(self) -> 'GXVV':
        ret_val = self._wrapper.get_v_vz()
        return GXVV(ret_val)




    def get_chan_array_size(self, p2: int) -> int:
        ret_val = self._wrapper.get_chan_array_size(p2)
        return ret_val




# Processing



    def add_block(self, p2: int) -> None:
        self._wrapper.add_block(p2)
        




    def commit(self) -> None:
        self._wrapper.commit()
        




    def test_func(self, p2: 'GXRA') -> None:
        self._wrapper.test_func(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer