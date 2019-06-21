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
class GXDAT(gxapi_cy.WrapDAT):
    """
    GXDAT class.

    The `GXDAT <geosoft.gxapi.GXDAT>` object is used to access data from an variety of data sources
    using the same access functions. The `GXDAT <geosoft.gxapi.GXDAT>` interface supports data access
    on a point-by-point, of line-by-line basis.  For example,
    the `GXBIGRID.run <geosoft.gxapi.GXBIGRID.run>` function uses 2 `GXDAT <geosoft.gxapi.GXDAT>` objects - one `GXDAT <geosoft.gxapi.GXDAT>` associated with the
    input data source, which is read line-by-line, and a second associated with
    the output grid file output grid file.

    Use a specific `GXDAT <geosoft.gxapi.GXDAT>` creation method for an associated
    information source in order to make a `GXDAT <geosoft.gxapi.GXDAT>` as required
    by a specific processing function.  The gridding methods all use DATs.
    """

    def __init__(self, handle=0):
        super(GXDAT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDAT <geosoft.gxapi.GXDAT>`
        
        :returns: A null `GXDAT <geosoft.gxapi.GXDAT>`
        :rtype:   GXDAT
        """
        return GXDAT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create_db(cls, db, x_ch, y_ch, z_ch):
        """
        Create a handle to a database `GXDAT <geosoft.gxapi.GXDAT>` object
        
        :param db:    Handle to database which `GXDAT <geosoft.gxapi.GXDAT>` is connected with
        :param x_ch:  Name of X channel in database
        :param y_ch:  Name of Y channel in database
        :param z_ch:  Name of Z channel in database
        :type  db:    GXDB
        :type  x_ch:  str
        :type  y_ch:  str
        :type  z_ch:  str

        :returns:     `GXDAT <geosoft.gxapi.GXDAT>` Object
        :rtype:       GXDAT

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapDAT._create_db(GXContext._get_tls_geo(), db, x_ch.encode(), y_ch.encode(), z_ch.encode())
        return GXDAT(ret_val)



    @classmethod
    def create_xgd(cls, name, mode):
        """
        Create a handle to a grid file `GXDAT <geosoft.gxapi.GXDAT>` object
        
        :param name:  Name of grid file to associate `GXDAT <geosoft.gxapi.GXDAT>` with
        :param mode:  :ref:`DAT_XGD`
        :type  name:  str
        :type  mode:  int

        :returns:     `GXDAT <geosoft.gxapi.GXDAT>` Object
        :rtype:       GXDAT

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapDAT._create_xgd(GXContext._get_tls_geo(), name.encode(), mode)
        return GXDAT(ret_val)





    @classmethod
    def get_lst(cls, lst, interface_name, flags, mode):
        """
        Put available `GXDAT <geosoft.gxapi.GXDAT>` filters and qualifiers in a `GXLST <geosoft.gxapi.GXLST>`
        
        :param lst:             `GXLST <geosoft.gxapi.GXLST>` object to populate
        :param interface_name:  `GXDAT <geosoft.gxapi.GXDAT>` interface name ("XGD" only support option currently)
        :param flags:           :ref:`DAT_FILE`
        :param mode:            :ref:`DAT_FILE_FORM`
        :type  lst:             GXLST
        :type  interface_name:  str
        :type  flags:           int
        :type  mode:            int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The filters displayed in the Grid/Image file browse dialog are put
        in the "Name" of the `GXLST <geosoft.gxapi.GXLST>`, while the file qualifiers are stored in
        the "Value".
        """
        gxapi_cy.WrapDAT._get_lst(GXContext._get_tls_geo(), lst, interface_name.encode(), flags, mode)
        




    def range_xyz(self, min_x, min_y, min_z, max_x, max_y, max_z, num_non_dummy):
        """
        Determine the range in X, Y and Z in the `GXDAT <geosoft.gxapi.GXDAT>` source
        
        :param min_x:          Minimum X (`rMAX <geosoft.gxapi.rMAX>` if none)
        :param min_y:          Minimum Y (`rMAX <geosoft.gxapi.rMAX>` if none)
        :param min_z:          Minimum Z (`rMAX <geosoft.gxapi.rMAX>` if none)
        :param max_x:          Maximum X (`rMIN <geosoft.gxapi.rMIN>` if none)
        :param max_y:          Maximum Y (`rMIN <geosoft.gxapi.rMIN>` if none)
        :param max_z:          Maximum Z (`rMIN <geosoft.gxapi.rMIN>` if none)
        :param num_non_dummy:  Number of non-dummy XYZ.
        :type  min_x:          float_ref
        :type  min_y:          float_ref
        :type  min_z:          float_ref
        :type  max_x:          float_ref
        :type  max_y:          float_ref
        :type  max_z:          float_ref
        :type  num_non_dummy:  int_ref

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Terminates if unable to open an RPT `GXDAT <geosoft.gxapi.GXDAT>` interface.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value, num_non_dummy.value = self._range_xyz(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value, num_non_dummy.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer