#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.

### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
import warnings
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXBIGRID(gxapi_cy.WrapBIGRID):
    """
    GXBIGRID class.

    The Bigrid class is used to grid data using a optimized algorithm that
    assumes data is collected in semi-straight lines.
    """

    def __init__(self, handle=0):
        super(GXBIGRID, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXBIGRID <geosoft.gxapi.GXBIGRID>`
        
        :returns: A null `GXBIGRID <geosoft.gxapi.GXBIGRID>`
        :rtype:   GXBIGRID
        """
        return GXBIGRID()

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
        
        Clears all the parameters in a `GXBIGRID <geosoft.gxapi.GXBIGRID>` object
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        
        self._clear()
        



    @classmethod
    def create(cls):
        """
        
        Create a handle to a Bigrid object
        

        :returns:    `GXBIGRID <geosoft.gxapi.GXBIGRID>` Object
        :rtype:      GXBIGRID

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The Bigrid object is initially empty. It will store the
        control file parameters which the Bigrid program needs
        to execute. Use the LoadParms_BIGRID method to get the
        control file parameters into the `GXBIGRID <geosoft.gxapi.GXBIGRID>` object.
        """
        
        ret_val = gxapi_cy.WrapBIGRID._create(GXContext._get_tls_geo())
        return GXBIGRID(ret_val)






    def load_parms(self, file):
        """
        
        Retrieves a Bigrid object's control parameters from a file,
        or sets the parameters to default if the file doesn't exist.
        
        :param file:    Name of file to get the parameter settings from
        :type  file:    str

        :returns:       0 - Ok
                        1 - Error
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the control file name passed into this function is a file
        which does not exist, then the defaults for a Bigrid control
        file will be generated and put into the `GXBIGRID <geosoft.gxapi.GXBIGRID>` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the `GXBIGRID <geosoft.gxapi.GXBIGRID>` object.
        """
        
        ret_val = self._load_parms(file.encode())
        return ret_val




    def load_warp(self, title, cell, warp):
        """
        
        Load a warp projection.
        
        :param title:   New grid title
        :param cell:    New grid cell size as a string, blank for default
        :param warp:    Warp projection file name
        :type  title:   str
        :type  cell:    str
        :type  warp:    str

        :returns:       0 - Ok
                        1 - Error
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        
        ret_val = self._load_warp(title.encode(), cell.encode(), warp.encode())
        return ret_val




    def run(self, zchan, in_dat, out_dat):
        """
        
        Executes the Bigrid program, using the input channel and
        output file parameters.
        
        :param zchan:    Not used, pass as ""
        :param in_dat:   Handle to source `GXDAT <geosoft.gxapi.GXDAT>` object (from database)
        :param out_dat:  Handle to output grid file `GXDAT <geosoft.gxapi.GXDAT>`
        :type  zchan:    str
        :type  in_dat:   GXDAT
        :type  out_dat:  GXDAT

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        
        self._run(zchan.encode(), in_dat, out_dat)
        




    def run2(self, zchan, in_dat, out_dat, ipj):
        """
        
        Executes the Bigrid program, using the input channel and
        output file parameters with a projection handle.
        
        :param zchan:    Not used, pass as ""
        :param in_dat:   Handle to source `GXDAT <geosoft.gxapi.GXDAT>` object (from database)
        :param out_dat:  Handle to output grid file `GXDAT <geosoft.gxapi.GXDAT>`
        :param ipj:      `GXIPJ <geosoft.gxapi.GXIPJ>` handle of the projection system
        :type  zchan:    str
        :type  in_dat:   GXDAT
        :type  out_dat:  GXDAT
        :type  ipj:      GXIPJ

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        
        self._run2(zchan.encode(), in_dat, out_dat, ipj)
        




    def save_parms(self, name):
        """
        
        Puts the Bigrid object's control parameters back into
        its control file.
        
        :param name:    Name of file to put the parameter settings into
        :type  name:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the control file did not previously exist, it will be
        created. Otherwise, the old file will be overwritten.
        """
        
        self._save_parms(name.encode())
        



    @classmethod
    def get_defaults(cls, db, x, y, z, cell, maxLineSeparation, maxPointSeparation, trendAngle, lowPassWavelength, highPass, noneLinear, preFilter):
        """
        
        Get default values for max line separation, max point separation and trend angle.
        
        :param db:                  Handle to a database
        :param x:                   Y Channel
        :param y:                   X Channel
        :param z:                   Data channel
        :param cell:                cell size
        :param maxLineSeparation:   max line separation
        :param maxPointSeparation:  max point separation
        :param trendAngle:          trend angle
        :param lowPassWavelength:   low-pass filter wavelength
        :param highPass:            high-pass filter wavelength
        :param noneLinear:          non-linear filter tolerance
        :param preFilter:           pre-filter sample increment
        :type  db:                  GXDB
        :type  x:                   str
        :type  y:                   str
        :type  z:                   str
        :type  cell:                float
        :type  maxLineSeparation:   float_ref
        :type  maxPointSeparation:  float_ref
        :type  trendAngle:          float_ref
        :type  lowPassWavelength:   float_ref
        :type  highPass:            float_ref
        :type  noneLinear:          float_ref
        :type  preFilter:           float_ref

        :returns:                   0 - Ok
                                    1 - Error
        :rtype:                     int

        .. versionadded:: 2021.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        
        ret_val, maxLineSeparation.value, maxPointSeparation.value, trendAngle.value, lowPassWavelength.value, highPass.value, noneLinear.value, preFilter.value = gxapi_cy.WrapBIGRID._get_defaults(GXContext._get_tls_geo(), db, x.encode(), y.encode(), z.encode(), cell, maxLineSeparation.value, maxPointSeparation.value, trendAngle.value, lowPassWavelength.value, highPass.value, noneLinear.value, preFilter.value)
        return ret_val



    @classmethod
    def get_default_cell_size(cls, db, x, y, z, cell):
        """
        
        Get default cell size value.
        
        :param db:    Handle to a database
        :param x:     Y Channel
        :param y:     X Channel
        :param z:     Data channel
        :param cell:  cell size
        :type  db:    GXDB
        :type  x:     str
        :type  y:     str
        :type  z:     str
        :type  cell:  float_ref

        :returns:     0 - Ok
                      1 - Error
        :rtype:       int

        .. versionadded:: 2023.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        
        ret_val, cell.value = gxapi_cy.WrapBIGRID._get_default_cell_size(GXContext._get_tls_geo(), db, x.encode(), y.encode(), z.encode(), cell.value)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer