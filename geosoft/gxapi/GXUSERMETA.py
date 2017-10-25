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
class GXUSERMETA:
    """
    GXUSERMETA class.

    The :class:`geosoft.gxapi.GXUSERMETA` class handles user style metadata tied to real
    data.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapUSERMETA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXUSERMETA`
        
        :returns: A null :class:`geosoft.gxapi.GXUSERMETA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXUSERMETA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXUSERMETA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1):
        """
        Creates an empty :class:`geosoft.gxapi.GXUSERMETA` object
        """
        ret_val = gxapi_cy.WrapUSERMETA.create(GXContext._get_tls_geo(), p1)
        return GXUSERMETA(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create a :class:`geosoft.gxapi.GXUSERMETA` from a file
        """
        ret_val = gxapi_cy.WrapUSERMETA.create_s(GXContext._get_tls_geo(), p1.encode())
        return GXUSERMETA(ret_val)






    def get_data_creation_date(self, p2):
        """
        Get the Data Creation Date
        """
        p2.value = self._wrapper.get_data_creation_date(p2.value)
        




    def get_extents2d(self, p2, p3, p4, p5):
        """
        Get the 2d Extents
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_extents2d(p2.value, p3.value, p4.value, p5.value)
        




    def get_extents3d(self, p2, p3, p4, p5, p6, p7):
        """
        Get the 3d Extents
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents3d(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_ipj(self, p2):
        """
        Get the :class:`geosoft.gxapi.GXIPJ`
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_meta_creation_date(self, p2):
        """
        Get the Meta Creation Date
        """
        p2.value = self._wrapper.get_meta_creation_date(p2.value)
        




    def get_xml_format(self, p2):
        """
        Get the XML Format
        """
        p2.value = self._wrapper.get_xml_format(p2.value)
        




    def compare(self, p2):
        """
        Compare 2 :class:`geosoft.gxapi.GXUSERMETA`'s
        """
        ret_val = self._wrapper.compare(p2._wrapper)
        return ret_val




    def get_data_creator(self, p2):
        """
        Get the Data Creator
        """
        p2.value = self._wrapper.get_data_creator(p2.value.encode())
        




    def get_format(self, p2):
        """
        Get the File Format
        """
        p2.value = self._wrapper.get_format(p2.value.encode())
        




    def get_meta_creator(self, p2):
        """
        Get the Meta Creator
        """
        p2.value = self._wrapper.get_meta_creator(p2.value.encode())
        




    def get_project(self, p2):
        """
        Get the File Project
        """
        p2.value = self._wrapper.get_project(p2.value.encode())
        




    def get_title(self, p2):
        """
        Get the Title
        """
        p2.value = self._wrapper.get_title(p2.value.encode())
        




    def serial(self, p2, p3):
        """
        Serialize :class:`geosoft.gxapi.GXUSERMETA` to a :class:`geosoft.gxapi.GXBF`.
        """
        self._wrapper.serial(p2, p3.encode())
        




    def set_data_creation_date(self, p2):
        """
        Set the Data Creation Date
        """
        self._wrapper.set_data_creation_date(p2)
        




    def set_data_creator(self, p2):
        """
        Set the Data Creator
        """
        self._wrapper.set_data_creator(p2.encode())
        




    def set_extents2d(self, p2, p3, p4, p5):
        """
        Set the 2d Extents
        """
        self._wrapper.set_extents2d(p2, p3, p4, p5)
        




    def set_extents3d(self, p2, p3, p4, p5, p6, p7):
        """
        Set the 3d Extents
        """
        self._wrapper.set_extents3d(p2, p3, p4, p5, p6, p7)
        




    def set_format(self, p2):
        """
        Set the File Format
        """
        self._wrapper.set_format(p2.encode())
        




    def set_ipj(self, p2):
        """
        Set the :class:`geosoft.gxapi.GXIPJ`
        """
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_meta_creation_date(self, p2):
        """
        Set the Meta Creation Date
        """
        self._wrapper.set_meta_creation_date(p2)
        




    def set_meta_creator(self, p2):
        """
        Set the Meta Creator
        """
        self._wrapper.set_meta_creator(p2.encode())
        




    def set_project(self, p2):
        """
        Set the File Project
        """
        self._wrapper.set_project(p2.encode())
        




    def set_title(self, p2):
        """
        Set the Title
        """
        self._wrapper.set_title(p2.encode())
        



    @classmethod
    def update_extents2_d(cls, p1, p2, p3, p4, p5, p6):
        """
        Edit an existing XML metadata file by
        changing the extents and projection data
        """
        gxapi_cy.WrapUSERMETA.update_extents2_d(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6)
        



    @classmethod
    def update_file_type(cls, p1, p2):
        """
        Edit an existing XML metadata file by
        changing the file type
        """
        gxapi_cy.WrapUSERMETA.update_file_type(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def save_file_lineage(cls, p1, p2):
        """
        Add lineage to XML
        """
        gxapi_cy.WrapUSERMETA.save_file_lineage(GXContext._get_tls_geo(), p1.encode(), p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer