### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIMG import GXIMG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXRGRD(gxapi_cy.WrapRGRD):
    """
    GXRGRD class.

    The `GXRGRD <geosoft.gxapi.GXRGRD>` object is used as a storage place for the control
    parameters which the Rangrid (minimum curvature) program needs to execute. The
    Run_RGRD function executes the Rangrid program using the `GXRGRD <geosoft.gxapi.GXRGRD>` object.
    """

    def __init__(self, handle=0):
        super(GXRGRD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXRGRD <geosoft.gxapi.GXRGRD>`
        
        :returns: A null `GXRGRD <geosoft.gxapi.GXRGRD>`
        :rtype:   GXRGRD
        """
        return GXRGRD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a `GXRGRD <geosoft.gxapi.GXRGRD>` object
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** DLL name `clear <geosoft.gxapi.GXRGRD.clear>`
        """
        self._clear()
        



    @classmethod
    def create(cls):
        """
        Create a handle to a Rangrid object
        

        :returns:    `GXRGRD <geosoft.gxapi.GXRGRD>` Object
        :rtype:      GXRGRD

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The Rangrid object is initially empty. It will store the
        control file parameters which the Rangrid program needs
        to execute. Use the LoadParms_RGRD method to get the
        control file parameters into the `GXRGRD <geosoft.gxapi.GXRGRD>` object.
        """
        ret_val = gxapi_cy.WrapRGRD._create(GXContext._get_tls_geo())
        return GXRGRD(ret_val)



    @classmethod
    def create_img(cls, vv_x, vv_y, vv_z, ipj, ctl, grid):
        """
        Run Rangrid directly on XYZ `GXVV <geosoft.gxapi.GXVV>` data, output to an `GXIMG <geosoft.gxapi.GXIMG>`.
        
        :param vv_x:  X data (any numeric `GXVV <geosoft.gxapi.GXVV>` type)
        :param vv_y:  Y data (any numeric `GXVV <geosoft.gxapi.GXVV>` type)
        :param vv_z:  Z (grid value) data (any numeric `GXVV <geosoft.gxapi.GXVV>` type)
        :param ipj:   Projection to apply to the output `GXIMG <geosoft.gxapi.GXIMG>`
        :param ctl:   RANGRID control file.
        :param grid:  Output grid name (optional)
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  ipj:   GXIPJ
        :type  ctl:   str
        :type  grid:  str

        :returns:     `GXIMG <geosoft.gxapi.GXIMG>` object
        :rtype:       GXIMG

        .. versionadded:: 7.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the grid file name is defined, the `GXIMG <geosoft.gxapi.GXIMG>` is tied to a new output file.
        If the grid file name is not defined, the `GXIMG <geosoft.gxapi.GXIMG>` is memory-based; not
        tied to a file.
        """
        ret_val = gxapi_cy.WrapRGRD._create_img(GXContext._get_tls_geo(), vv_x, vv_y, vv_z, ipj, ctl.encode(), grid.encode())
        return GXIMG(ret_val)






    def default(self, zchan, in_dat):
        """
        Set the defaults.
        
        :param zchan:   Name of Z Channel to perfrom gridding on
        :param in_dat:  Handle to source `GXDAT <geosoft.gxapi.GXDAT>` object (from database)
        :type  zchan:   str
        :type  in_dat:  GXDAT

        :returns:       0 OK, 1 Error.
        :rtype:         int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._default(zchan.encode(), in_dat)
        return ret_val




    def load_parms(self, file):
        """
        Retrieves a Rangrid object's control parameters from a file,
        or sets the parameters to default if the file doesn't exist.
        
        :param file:  Name of file to get the parameter settings from
        :type  file:  str

        :returns:     0 OK, 1 Error.
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the control file name passed into this function is a file
        which does not exist, then the defaults for a Rangrid control
        file will be generated and put into the `GXRGRD <geosoft.gxapi.GXRGRD>` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the `GXRGRD <geosoft.gxapi.GXRGRD>` object.
        """
        ret_val = self._load_parms(file.encode())
        return ret_val




    def run(self, in_dat, out_dat):
        """
        Executes the Rangrid program, using the input channel and
        output file parameters.
        
        :param in_dat:   Handle to source `GXDAT <geosoft.gxapi.GXDAT>` object (from database)
        :param out_dat:  Handle to output grid file `GXDAT <geosoft.gxapi.GXDAT>`
        :type  in_dat:   GXDAT
        :type  out_dat:  GXDAT

        :returns:        0 OK, 1 Error.
        :rtype:          int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._run(in_dat, out_dat)
        return ret_val



    @classmethod
    def run2(cls, db, x, y, z, ctl, grd):
        """
        Executes the Rangrid program directly on a database.
        
        :param db:   Handle to a database
        :param x:    Y Channel
        :param y:    X Channel
        :param z:    Data channel
        :param ctl:  RANGRID control file.
        :param grd:  Output grid name
        :type  db:   GXDB
        :type  x:    str
        :type  y:    str
        :type  z:    str
        :type  ctl:  str
        :type  grd:  str

        :returns:    0, always.
        :rtype:      int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapRGRD._run2(GXContext._get_tls_geo(), db, x.encode(), y.encode(), z.encode(), ctl.encode(), grd.encode())
        return ret_val




    def save_parms(self, name):
        """
        Puts the Rangrid object's control parameters back into
        its control file.
        
        :param name:  Name of file to put the parameter settings into
        :type  name:  str

        :returns:     0 OK, 1 Error.
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the control file did not previously exist, it will be
        created. Otherwise, the old file will be overwritten.
        """
        ret_val = self._save_parms(name.encode())
        return ret_val



    @classmethod
    def run_vv(cls, vv_x, vv_y, vv_z, ipj, ctl, grd):
        """
        Executes the Rangrid program directly on input data VVs.
        
        :param vv_x:  X data
        :param vv_y:  Y data
        :param vv_z:  Z (grid value) data
        :param ipj:   Projection to put into grid
        :param ctl:   RANGRID control file.
        :param grd:   Output grid name
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  ipj:   GXIPJ
        :type  ctl:   str
        :type  grd:   str

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapRGRD._run_vv(GXContext._get_tls_geo(), vv_x, vv_y, vv_z, ipj, ctl.encode(), grd.encode())
        



    @classmethod
    def run_list(cls, dbs, zch, ipj, ctl, grd):
        """
        Executes the Rangrid program from a list of databases.
        
        :param dbs:  List of databases (using | separator)
        :param zch:  Z Channel
        :param ipj:  Projection to put into grid
        :param ctl:  RANGRID control file.
        :param grd:  Output grid name
        :type  dbs:  str
        :type  zch:  str
        :type  ipj:  GXIPJ
        :type  ctl:  str
        :type  grd:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapRGRD._run_list(GXContext._get_tls_geo(), dbs.encode(), zch.encode(), ipj, ctl.encode(), grd.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer