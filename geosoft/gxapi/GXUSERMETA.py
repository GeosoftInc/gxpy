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
class GXUSERMETA(gxapi_cy.WrapUSERMETA):
    """
    GXUSERMETA class.

    The `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` class handles user style metadata tied to real
    data.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXUSERMETA <geosoft.gxapi.GXUSERMETA>`
        
        :returns: A null `GXUSERMETA <geosoft.gxapi.GXUSERMETA>`
        :rtype:   GXUSERMETA
        """
        return GXUSERMETA()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, format):
        """
        Creates an empty `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` object
        
        :param format:  :ref:`USERMETA_FORMAT` Type of Meta to create
        :type  format:  int

        :returns:       `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` Object
        :rtype:         GXUSERMETA

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapUSERMETA._create(GXContext._get_tls_geo(), format)
        return GXUSERMETA(ret_val)



    @classmethod
    def create_s(cls, file):
        """
        Create a `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` from a file
        
        :param file:  File Name
        :type  file:  str

        :returns:     `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` Object
        :rtype:       GXUSERMETA

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapUSERMETA._create_s(GXContext._get_tls_geo(), file.encode())
        return GXUSERMETA(ret_val)






    def get_data_creation_date(self, date):
        """
        Get the Data Creation Date
        
        :param date:      Date
        :type  date:      float_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        date.value = self._get_data_creation_date(date.value)
        




    def get_extents2d(self, min_x, min_y, max_x, max_y):
        """
        Get the 2d Extents
        
        :param min_x:     MinX
        :param min_y:     MinY
        :param max_x:     MaxX
        :param max_y:     MaxY
        :type  min_x:     float_ref
        :type  min_y:     float_ref
        :type  max_x:     float_ref
        :type  max_y:     float_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._get_extents2d(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_extents3d(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the 3d Extents
        
        :param min_x:     MinX
        :param min_y:     MinY
        :param min_z:     MinZ
        :param max_x:     MaxX
        :param max_y:     MaxY
        :param max_z:     MaxZ
        :type  min_x:     float_ref
        :type  min_y:     float_ref
        :type  min_z:     float_ref
        :type  max_x:     float_ref
        :type  max_y:     float_ref
        :type  max_z:     float_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_extents3d(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_ipj(self, ipj):
        """
        Get the `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :param ipj:       Date
        :type  ipj:       GXIPJ

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def get_meta_creation_date(self, date):
        """
        Get the Meta Creation Date
        
        :param date:      Date
        :type  date:      float_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        date.value = self._get_meta_creation_date(date.value)
        




    def get_xml_format(self, format):
        """
        Get the XML Format
        
        :param format:    :ref:`USERMETA_FORMAT`
        :type  format:    int_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        format.value = self._get_xml_format(format.value)
        




    def set_xml_format(self, format):
        """
        Get the XML Format
        
        :param format:    :ref:`USERMETA_FORMAT`
        :type  format:    int

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_xml_format(format)
        




    def compare(self, usermeta2):
        """
        Compare 2 `GXUSERMETA <geosoft.gxapi.GXUSERMETA>`'s
        
        :param usermeta2:  Second UERMETA
        :type  usermeta2:  GXUSERMETA

        :returns:          0 - No
                           1 - Yes
        :rtype:            int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._compare(usermeta2)
        return ret_val




    def get_data_creator(self, data_creator):
        """
        Get the Data Creator
        
        :param data_creator:  DataCreator returned
        :type  data_creator:  str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        data_creator.value = self._get_data_creator(data_creator.value.encode())
        




    def get_format(self, format):
        """
        Get the File Format
        
        :param format:    Title returned
        :type  format:    str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        format.value = self._get_format(format.value.encode())
        




    def get_meta_creator(self, meta_creator):
        """
        Get the Meta Creator
        
        :param meta_creator:  MetaCreator returned
        :type  meta_creator:  str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        meta_creator.value = self._get_meta_creator(meta_creator.value.encode())
        




    def get_project(self, project):
        """
        Get the File Project
        
        :param project:   Title returned
        :type  project:   str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        project.value = self._get_project(project.value.encode())
        




    def get_title(self, title):
        """
        Get the Title
        
        :param title:     Title returned
        :type  title:     str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        title.value = self._get_title(title.value.encode())
        




    def serial(self, save_geo, file):
        """
        Serialize `GXUSERMETA <geosoft.gxapi.GXUSERMETA>` to a `GXBF <geosoft.gxapi.GXBF>`.
        
        :param save_geo:  Output Geosoft Metadata?
        :param file:      File name to save to
        :type  save_geo:  bool
        :type  file:      str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(save_geo, file.encode())
        




    def set_data_creation_date(self, date):
        """
        Set the Data Creation Date
        
        :param date:      Date
        :type  date:      float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_data_creation_date(date)
        




    def set_data_creator(self, data_creator):
        """
        Set the Data Creator
        
        :param data_creator:  DataCreator
        :type  data_creator:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_data_creator(data_creator.encode())
        




    def set_extents2d(self, min_x, min_y, max_x, max_y):
        """
        Set the 2d Extents
        
        :param min_x:     MinX
        :param min_y:     MinY
        :param max_x:     MaxX
        :param max_y:     MaxY
        :type  min_x:     float
        :type  min_y:     float
        :type  max_x:     float
        :type  max_y:     float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_extents2d(min_x, min_y, max_x, max_y)
        




    def set_extents3d(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Set the 3d Extents
        
        :param min_x:     MinX
        :param min_y:     MinY
        :param min_z:     MinZ
        :param max_x:     MaxX
        :param max_y:     MaxY
        :param max_z:     MaxZ
        :type  min_x:     float
        :type  min_y:     float
        :type  min_z:     float
        :type  max_x:     float
        :type  max_y:     float
        :type  max_z:     float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_extents3d(min_x, min_y, min_z, max_x, max_y, max_z)
        




    def set_format(self, format):
        """
        Set the File Format
        
        :param format:    Format
        :type  format:    str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_format(format.encode())
        




    def set_ipj(self, ipj):
        """
        Set the `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :param ipj:       Date
        :type  ipj:       GXIPJ

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_ipj(ipj)
        




    def set_meta_creation_date(self, date):
        """
        Set the Meta Creation Date
        
        :param date:      Date
        :type  date:      float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta_creation_date(date)
        




    def set_meta_creator(self, meta_creator):
        """
        Set the Meta Creator
        
        :param meta_creator:  MetaCreator
        :type  meta_creator:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta_creator(meta_creator.encode())
        




    def set_project(self, project):
        """
        Set the File Project
        
        :param project:   Project
        :type  project:   str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_project(project.encode())
        




    def set_title(self, title):
        """
        Set the Title
        
        :param title:     Title
        :type  title:     str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_title(title.encode())
        



    @classmethod
    def update_extents_2d(cls, filename, ipj, min_x, min_y, max_x, max_y):
        """
        Edit an existing XML metadata file by
        changing the extents and projection data
        
        :param filename:  Filename of existing metadata to update
        :param ipj:       New projection
        :param min_x:     New MinX value
        :param min_y:     New MinY value
        :param max_x:     New MaxX value
        :param max_y:     New MaxY value
        :type  filename:  str
        :type  ipj:       GXIPJ
        :type  min_x:     float
        :type  min_y:     float
        :type  max_x:     float
        :type  max_y:     float

        .. versionadded:: 7.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapUSERMETA._update_extents_2d(GXContext._get_tls_geo(), filename.encode(), ipj, min_x, min_y, max_x, max_y)
        



    @classmethod
    def update_file_type(cls, file_name, new_file_type):
        """
        Edit an existing XML metadata file by
        changing the file type
        
        :param file_name:      Filename of existing metadata to update
        :param new_file_type:  New file type
        :type  file_name:      str
        :type  new_file_type:  str

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapUSERMETA._update_file_type(GXContext._get_tls_geo(), file_name.encode(), new_file_type.encode())
        



    @classmethod
    def save_file_lineage(cls, file_name, save_geo):
        """
        Add lineage to XML
        
        :param file_name:  Filename of existing metadata to update
        :param save_geo:   Output Geosoft Metadata?
        :type  file_name:  str
        :type  save_geo:   bool

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapUSERMETA._save_file_lineage(GXContext._get_tls_geo(), file_name.encode(), save_geo)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer