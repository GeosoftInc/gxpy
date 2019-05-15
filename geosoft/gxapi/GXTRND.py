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
class GXTRND(gxapi_cy.WrapTRND):
    """
    GXTRND class.

    The `GXTRND <geosoft.gxapi.GXTRND>` methods are used to determine trend directions in database data by locating
    maxima and minima along lines and joining them in a specified direction.
    The resulting trend lines are appended to the database and used by gridding methods
    such as Bigrid and Rangrid to enforce features in the specified direction.
    """

    def __init__(self, handle=0):
        super(GXTRND, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTRND <geosoft.gxapi.GXTRND>`
        
        :returns: A null `GXTRND <geosoft.gxapi.GXTRND>`
        :rtype:   GXTRND
        """
        return GXTRND()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def get_max_min(cls, vv_x, vv_y, vv_z, vv_xm, v_vym, v_vzm, window, trnd):
        """
        Find the max/min nodes in a line.
        
        :param vv_x:    X Channel
        :param vv_y:    Y Channel
        :param vv_z:    Data Channel
        :param vv_xm:   X MaxMin (returned)
        :param v_vym:   Y MaxMin (returned)
        :param v_vzm:   Data MaxMin (returned)
        :param window:  MaxMin Window
        :param trnd:    :ref:`TRND_NODE`
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV
        :type  vv_xm:   GXVV
        :type  v_vym:   GXVV
        :type  v_vzm:   GXVV
        :type  window:  float
        :type  trnd:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Trend lines positions consist of X and Y VVs
        """
        gxapi_cy.WrapTRND._get_max_min(GXContext._get_tls_geo(), vv_x, vv_y, vv_z, vv_xm, v_vym, v_vzm, window, trnd)
        



    @classmethod
    def get_mesh(cls, db, chan, window, max_length, mesh_vv, trnd):
        """
        Get the lines in a trend mesh.
        
        :param db:          Database
        :param chan:        Selected channel
        :param window:      MaxMin Window
        :param max_length:  Maximum join length
        :param mesh_vv:     `GXVV <geosoft.gxapi.GXVV>` of type GS_D2POINT (returned)
        :param trnd:        :ref:`TRND_NODE`
        :type  db:          GXDB
        :type  chan:        str
        :type  window:      float
        :type  max_length:  float
        :type  mesh_vv:     GXVV
        :type  trnd:        int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapTRND._get_mesh(GXContext._get_tls_geo(), db, chan.encode(), window, max_length, mesh_vv, trnd)
        



    @classmethod
    def trnd_db(cls, db, chan, window, angle, deviation, max_length, deflection, min_length, resample, br_angle):
        """
        Uses a selected channel to find data trends in a database.
        
        :param db:          Database handle
        :param chan:        Selected channel
        :param window:      MaxMin Window
        :param angle:       Preferred angle, degrees CCW from X
        :param deviation:   Allowed deviation
        :param max_length:  Longest join
        :param deflection:  Maximum deflection in join (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param min_length:  Minimum length for trend lines (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param resample:    Resampling distance (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param br_angle:    Breaking angle, degrees CCW from X (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :type  db:          GXDB
        :type  chan:        str
        :type  window:      float
        :type  angle:       float
        :type  deviation:   float
        :type  max_length:  float
        :type  deflection:  float
        :type  min_length:  float
        :type  resample:    float
        :type  br_angle:    float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapTRND._trnd_db(GXContext._get_tls_geo(), db, chan.encode(), window, angle, deviation, max_length, deflection, min_length, resample, br_angle)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer