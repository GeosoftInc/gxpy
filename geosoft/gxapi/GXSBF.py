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
class GXSBF(gxapi_cy.WrapSBF):
    """
    GXSBF class.

    The `GXSBF <geosoft.gxapi.GXSBF>` class provides a means of storing data in a
    file-type directory structure within a workspace, database
    or map. Each of these three objects contains its own `GXSBF <geosoft.gxapi.GXSBF>` object,
    which may be accessed using the `h_get_sys <geosoft.gxapi.GXSBF.h_get_sys>`, `h_get_db <geosoft.gxapi.GXSBF.h_get_db>` and
    `h_get_map <geosoft.gxapi.GXSBF.h_get_map>` functions. To access data in a file, or create a
    new file in the `GXSBF <geosoft.gxapi.GXSBF>` object, call the CreatSBF_BF function (see `GXBF <geosoft.gxapi.GXBF>`),
    which will return a `GXBF <geosoft.gxapi.GXBF>` object to use.
    """

    def __init__(self, handle=0):
        super(GXSBF, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSBF <geosoft.gxapi.GXSBF>`
        
        :returns: A null `GXSBF <geosoft.gxapi.GXSBF>`
        :rtype:   GXSBF
        """
        return GXSBF()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def create(self, file, status):
        """
        Create a child `GXSBF <geosoft.gxapi.GXSBF>` object inside an `GXSBF <geosoft.gxapi.GXSBF>`.
        
        :param file:    Directory name to open / create
        :param status:  :ref:`SBF_OPEN`
        :type  file:    str
        :type  status:  int

        :returns:       `GXSBF <geosoft.gxapi.GXSBF>` object, terminates if fails.
        :rtype:         GXSBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create(file.encode(), status)
        return GXSBF(ret_val)




    def create_obj_list(self, lst, type):
        """
        Fills an `GXLST <geosoft.gxapi.GXLST>` with embedded storage names of an `GXSBF <geosoft.gxapi.GXSBF>`.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` handle
        :param type:  :ref:`SBF_TYPE`
        :type  lst:   GXLST
        :type  type:  int

        .. versionadded:: 5.0.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Function will populate an `GXLST <geosoft.gxapi.GXLST>` object with embedded files (`SBF_TYPE_FILES <geosoft.gxapi.SBF_TYPE_FILES>`),
        directories (`SBF_TYPE_DIRS <geosoft.gxapi.SBF_TYPE_DIRS>`), or both (pass `SBF_TYPE_BOTH <geosoft.gxapi.SBF_TYPE_BOTH>`) in an `GXSBF <geosoft.gxapi.GXSBF>`.
        Along with the Name of the file or directory, a constant "dir" or "file" string is written
        to the `GXLST <geosoft.gxapi.GXLST>` also.
        """
        self._create_obj_list(lst, type)
        




    def del_dir(self, dir):
        """
        Delete a directory (storage) from this storage.
        
        :param dir:  Dir/Storage Name
        :type  dir:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._del_dir(dir.encode())
        




    def del_file(self, file):
        """
        Delete a file from this storage.
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._del_file(file.encode())
        





    @classmethod
    def h_get_db(cls, db):
        """
        Get the embedded file storage from a database.
        
        :param db:  Database
        :type  db:  GXDB

        :returns:    `GXSBF <geosoft.gxapi.GXSBF>` Object
        :rtype:      GXSBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSBF._h_get_db(GXContext._get_tls_geo(), db)
        return GXSBF(ret_val)



    @classmethod
    def h_get_map(cls, map):
        """
        Get the embedded file storage from a map.
        
        :param map:  `GXMAP <geosoft.gxapi.GXMAP>` object
        :type  map:  GXMAP

        :returns:    `GXSBF <geosoft.gxapi.GXSBF>` Object
        :rtype:      GXSBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSBF._h_get_map(GXContext._get_tls_geo(), map)
        return GXSBF(ret_val)



    @classmethod
    def h_get_sys(cls):
        """
        Get the main embedded file storage (in workspace).
        

        :returns:    `GXSBF <geosoft.gxapi.GXSBF>` Object
        :rtype:      GXSBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSBF._h_get_sys(GXContext._get_tls_geo())
        return GXSBF(ret_val)




    def exist_dir(self, dir):
        """
        Check to see if a directory (storage) exists inside this storage.
        
        :param dir:  Dir/Storage Name
        :type  dir:  str

        :returns:    0 - Does not exist
                     1 - Exists
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._exist_dir(dir.encode())
        return ret_val




    def exist_file(self, file):
        """
        Check to see if a file exists inside this storage.
        
        :param file:  File Name
        :type  file:  str

        :returns:     0 - Does not exist
                      1 - Exists
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._exist_file(file.encode())
        return ret_val




    def save_log(self, dir, file, file_save, p5):
        """
        Save an embedded file to an ASCII file.
        
        :param dir:        Directory name in the Parent `GXSBF <geosoft.gxapi.GXSBF>`
        :param file:       File name in the directory
        :param file_save:  File to save as (as an ASCII file)
        :param p5:         Append Mode: 0 - New file, 1 - Append file
        :type  dir:        str
        :type  file:       str
        :type  file_save:  str
        :type  p5:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save_log(dir.encode(), file.encode(), file_save.encode(), p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer