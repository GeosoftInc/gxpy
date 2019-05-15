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
class GXKGRD(gxapi_cy.WrapKGRD):
    """
    GXKGRD class.

    The `GXKGRD <geosoft.gxapi.GXKGRD>` object is used as a storage place for the control
    parameters that the Krigrid program needs to execute. The
    Run_KGRD function executes the Krigrid program using the
    `GXKGRD <geosoft.gxapi.GXKGRD>` object.
    """

    def __init__(self, handle=0):
        super(GXKGRD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXKGRD <geosoft.gxapi.GXKGRD>`
        
        :returns: A null `GXKGRD <geosoft.gxapi.GXKGRD>`
        :rtype:   GXKGRD
        """
        return GXKGRD()

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
        Clears all the parameters in a `GXKGRD <geosoft.gxapi.GXKGRD>` object
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._clear()
        



    @classmethod
    def create(cls):
        """
        Create a handle to a Krigrid object
        

        :returns:    `GXKGRD <geosoft.gxapi.GXKGRD>` Object
        :rtype:      GXKGRD

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The Krigrid object is initially empty. It will store the
        control file parameters which the Krigrid program needs
        to execute. Use the LoadParms_KGRD method to get the
        control file parameters into the `GXKGRD <geosoft.gxapi.GXKGRD>` object.
        """
        ret_val = gxapi_cy.WrapKGRD._create(GXContext._get_tls_geo())
        return GXKGRD(ret_val)






    def load_parms(self, file):
        """
        Retrieves a Krigrid object's control parameters from a file.
        
        :param file:  Name of file to get the parameter settings from
        :type  file:  str

        :returns:     0 OK, 1 Error.
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the control file name passed into this function is a file
        which does not exist, then the defaults for a Krigrid control
        file will be generated and put into the `GXKGRD <geosoft.gxapi.GXKGRD>` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the `GXKGRD <geosoft.gxapi.GXKGRD>` object.
        """
        ret_val = self._load_parms(file.encode())
        return ret_val




    def run(self, zchan, in_dat, out_grd_dat, out_err_dat, in_var_name, out_var_name, vao, vi, vo):
        """
        Executes the Krigrid program, using the input channel and
        output file parameters.
        
        :param zchan:         Name of Z Channel to perfrom gridding on
        :param in_dat:        Handle to source `GXDAT <geosoft.gxapi.GXDAT>` object (from database)
        :param out_grd_dat:   Handle to output grid file `GXDAT <geosoft.gxapi.GXDAT>`
        :param out_err_dat:   Handle to output error grid file `GXDAT <geosoft.gxapi.GXDAT>` ((`GXDAT <geosoft.gxapi.GXDAT>`)0) if no error grid required
        :param in_var_name:   Name of input variogram file
        :param out_var_name:  Name of output variogram file
        :param vao:           Flag of variogram only
        :param vi:            Flag of input variogram
        :param vo:            Flag of output variogram
        :type  zchan:         str
        :type  in_dat:        GXDAT
        :type  out_grd_dat:   GXDAT
        :type  out_err_dat:   GXDAT
        :type  in_var_name:   str
        :type  out_var_name:  str
        :type  vao:           int
        :type  vi:            int
        :type  vo:            int

        :returns:             0 OK, 1 Error.
        :rtype:               int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._run(zchan.encode(), in_dat, out_grd_dat, out_err_dat, in_var_name.encode(), out_var_name.encode(), vao, vi, vo)
        return ret_val



    @classmethod
    def run2(cls, db, x, y, z, ctl, grd, err_grd, in_var, out_var, vao):
        """
        Executes the Krigrid program directly on a database.
        
        :param db:       Handle to a database
        :param x:        Y Channel
        :param y:        X Channel
        :param z:        Data channel
        :param ctl:      KRIGRID control file.
        :param grd:      (output grid name (not required if variogram analysis only))
        :param err_grd:  (output error file, "" for none)
        :param in_var:   (input variogram file, "" for none)
        :param out_var:  (output variogram file, "" for none)
        :param vao:      1 if Variogram Analysis Only, other wise 0
        :type  db:       GXDB
        :type  x:        str
        :type  y:        str
        :type  z:        str
        :type  ctl:      str
        :type  grd:      str
        :type  err_grd:  str
        :type  in_var:   str
        :type  out_var:  str
        :type  vao:      int

        :returns:        0 OK, 1 Error.
        :rtype:          int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapKGRD._run2(GXContext._get_tls_geo(), db, x.encode(), y.encode(), z.encode(), ctl.encode(), grd.encode(), err_grd.encode(), in_var.encode(), out_var.encode(), vao)
        return ret_val



    @classmethod
    def run3(cls, db, x, y, z, ctl, grd, err_grd, in_var, out_var, log_file, vao):
        """
        Executes the Krigrid program directly on a database and specifies the log file
        
        :param db:        Handle to a database
        :param x:         Y Channel
        :param y:         X Channel
        :param z:         Data channel
        :param ctl:       KRIGRID control file.
        :param grd:       (output grid name (not required if variogram analysis only))
        :param err_grd:   (output error file, "" for none)
        :param in_var:    (input variogram file, "" for none)
        :param out_var:   (output variogram file, "" for none)
        :param log_file:  (log file name, "" for default)
        :param vao:       1 if Variogram Analysis Only, other wise 0
        :type  db:        GXDB
        :type  x:         str
        :type  y:         str
        :type  z:         str
        :type  ctl:       str
        :type  grd:       str
        :type  err_grd:   str
        :type  in_var:    str
        :type  out_var:   str
        :type  log_file:  str
        :type  vao:       int

        :returns:         0 OK, 1 Error.
        :rtype:           int

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapKGRD._run3(GXContext._get_tls_geo(), db, x.encode(), y.encode(), z.encode(), ctl.encode(), grd.encode(), err_grd.encode(), in_var.encode(), out_var.encode(), log_file.encode(), vao)
        return ret_val




    def save_parms(self, name):
        """
        Puts the Krigrid object's control parameters back into
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





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer