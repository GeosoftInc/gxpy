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

    The `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` class handles user style metadata tied to real
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
        A null (undefined) instance of `GXUSERMETA`
        
        :returns: A null `GXUSERMETA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXUSERMETA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXUSERMETA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, format):
        """
        Creates an empty `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` object
        """
        ret_val = gxapi_cy.WrapUSERMETA.create(GXContext._get_tls_geo(), format)
        return GXUSERMETA(ret_val)



    @classmethod
    def create_s(cls, file):
        """
        Create a `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` from a file
        """
        ret_val = gxapi_cy.WrapUSERMETA.create_s(GXContext._get_tls_geo(), file.encode())
        return GXUSERMETA(ret_val)






    def get_data_creation_date(self, date):
        """
        Get the Data Creation Date
        """
        date.value = self._wrapper.get_data_creation_date(date.value)
        




    def get_extents2d(self, min_x, min_y, max_x, max_y):
        """
        Get the 2d Extents
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.get_extents2d(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_extents3d(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the 3d Extents
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._wrapper.get_extents3d(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_ipj(self, ipj):
        """
        Get the `GXIPJ <geosoft.gxapi.GXIPJ>`
        """
        self._wrapper.get_ipj(ipj._wrapper)
        




    def get_meta_creation_date(self, date):
        """
        Get the Meta Creation Date
        """
        date.value = self._wrapper.get_meta_creation_date(date.value)
        




    def get_xml_format(self, format):
        """
        Get the XML Format
        """
        format.value = self._wrapper.get_xml_format(format.value)
        




    def compare(self, usermeta2):
        """
        Compare 2 `GXUSERMETA <geosoft.gxapi.GXUSERMETA>`'s
        """
        ret_val = self._wrapper.compare(usermeta2._wrapper)
        return ret_val




    def get_data_creator(self, data_creator):
        """
        Get the Data Creator
        """
        data_creator.value = self._wrapper.get_data_creator(data_creator.value.encode())
        




    def get_format(self, format):
        """
        Get the File Format
        """
        format.value = self._wrapper.get_format(format.value.encode())
        




    def get_meta_creator(self, meta_creator):
        """
        Get the Meta Creator
        """
        meta_creator.value = self._wrapper.get_meta_creator(meta_creator.value.encode())
        




    def get_project(self, project):
        """
        Get the File Project
        """
        project.value = self._wrapper.get_project(project.value.encode())
        




    def get_title(self, title):
        """
        Get the Title
        """
        title.value = self._wrapper.get_title(title.value.encode())
        




    def serial(self, save_geo, file):
        """
        Serialize `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` to a `GXBF <geosoft.gxapi.GXBF>`.
        """
        self._wrapper.serial(save_geo, file.encode())
        




    def set_data_creation_date(self, date):
        """
        Set the Data Creation Date
        """
        self._wrapper.set_data_creation_date(date)
        




    def set_data_creator(self, data_creator):
        """
        Set the Data Creator
        """
        self._wrapper.set_data_creator(data_creator.encode())
        




    def set_extents2d(self, min_x, min_y, max_x, max_y):
        """
        Set the 2d Extents
        """
        self._wrapper.set_extents2d(min_x, min_y, max_x, max_y)
        




    def set_extents3d(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Set the 3d Extents
        """
        self._wrapper.set_extents3d(min_x, min_y, min_z, max_x, max_y, max_z)
        




    def set_format(self, format):
        """
        Set the File Format
        """
        self._wrapper.set_format(format.encode())
        




    def set_ipj(self, ipj):
        """
        Set the `GXIPJ <geosoft.gxapi.GXIPJ>`
        """
        self._wrapper.set_ipj(ipj._wrapper)
        




    def set_meta_creation_date(self, date):
        """
        Set the Meta Creation Date
        """
        self._wrapper.set_meta_creation_date(date)
        




    def set_meta_creator(self, meta_creator):
        """
        Set the Meta Creator
        """
        self._wrapper.set_meta_creator(meta_creator.encode())
        




    def set_project(self, project):
        """
        Set the File Project
        """
        self._wrapper.set_project(project.encode())
        




    def set_title(self, title):
        """
        Set the Title
        """
        self._wrapper.set_title(title.encode())
        



    @classmethod
    def update_extents2_d(cls, filename, ipj, min_x, min_y, max_x, max_y):
        """
        Edit an existing XML metadata file by
        changing the extents and projection data
        """
        gxapi_cy.WrapUSERMETA.update_extents2_d(GXContext._get_tls_geo(), filename.encode(), ipj._wrapper, min_x, min_y, max_x, max_y)
        



    @classmethod
    def update_file_type(cls, file_name, new_file_type):
        """
        Edit an existing XML metadata file by
        changing the file type
        """
        gxapi_cy.WrapUSERMETA.update_file_type(GXContext._get_tls_geo(), file_name.encode(), new_file_type.encode())
        



    @classmethod
    def save_file_lineage(cls, file_name, save_geo):
        """
        Add lineage to XML
        """
        gxapi_cy.WrapUSERMETA.save_file_lineage(GXContext._get_tls_geo(), file_name.encode(), save_geo)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer