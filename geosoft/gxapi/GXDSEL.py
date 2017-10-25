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
class GXDSEL:
    """
    GXDSEL class.

    The :class:`GXDSEL` object is used to select subsets of data from the DATA object
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDSEL(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXDSEL':
        """
        A null (undefined) instance of :class:`GXDSEL`
        
        :returns: A null :class:`GXDSEL`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDSEL` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDSEL`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls) -> 'GXDSEL':
        ret_val = gxapi_cy.WrapDSEL.create(GXContext._get_tls_geo())
        return GXDSEL(ret_val)




    def data_significant_figures(self, p2: float) -> None:
        self._wrapper.data_significant_figures(p2)
        






    def meta_query(self, p2: str) -> None:
        self._wrapper.meta_query(p2.encode())
        




    def picture_quality(self, p2: int) -> None:
        self._wrapper.picture_quality(p2)
        




    def request_all_info(self, p2: int) -> None:
        self._wrapper.request_all_info(p2)
        




    def select_area(self, p2: 'GXPLY') -> None:
        self._wrapper.select_area(p2._wrapper)
        




    def select_rect(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.select_rect(p2, p3, p4, p5)
        




    def select_resolution(self, p2: float, p3: int) -> None:
        self._wrapper.select_resolution(p2, p3)
        




    def select_size(self, p2: int, p3: int) -> None:
        self._wrapper.select_size(p2, p3)
        




    def set_extract_as_document(self, p2: int) -> None:
        self._wrapper.set_extract_as_document(p2)
        




    def set_ipj(self, p2: 'GXIPJ', p3: int) -> None:
        self._wrapper.set_ipj(p2._wrapper, p3)
        




    def spatial_accuracy(self, p2: float) -> None:
        self._wrapper.spatial_accuracy(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer