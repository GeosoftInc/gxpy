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
class GXTRND:
    """
    GXTRND class.

    The `GXTRND <geosoft.gxapi.GXTRND>` methods are used to determine trend directions in database data by locating
    maxima and minima along lines and joining them in a specified direction.
    The resulting trend lines are appended to the database and used by gridding methods
    such as Bigrid and Rangrid to enforce features in the specified direction.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTRND(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTRND`
        
        :returns: A null `GXTRND`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTRND` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTRND`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


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
        :param trnd:    `TRND_NODE`
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV
        :type  vv_xm:   GXVV
        :type  v_vym:   GXVV
        :type  v_vzm:   GXVV
        :type  window:  float
        :type  trnd:    int

        .. versionadded:: 5.0

        **Note:**

        Trend lines positions consist of X and Y VVs
        """
        gxapi_cy.WrapTRND.get_max_min(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_xm._wrapper, v_vym._wrapper, v_vzm._wrapper, window, trnd)
        



    @classmethod
    def get_mesh(cls, db, chan, window, max_length, mesh_vv, trnd):
        """
        Get the lines in a trend mesh.
        
        :param db:          Database
        :param chan:        Selected channel
        :param window:      MaxMin Window
        :param max_length:  Maximum join length
        :param mesh_vv:     `GXVV <geosoft.gxapi.GXVV>` of type GS_D2POINT (returned)
        :param trnd:        `TRND_NODE`
        :type  db:          GXDB
        :type  chan:        str
        :type  window:      float
        :type  max_length:  float
        :type  mesh_vv:     GXVV
        :type  trnd:        int

        .. versionadded:: 5.0
        """
        gxapi_cy.WrapTRND.get_mesh(GXContext._get_tls_geo(), db._wrapper, chan.encode(), window, max_length, mesh_vv._wrapper, trnd)
        



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
        """
        gxapi_cy.WrapTRND.trnd_db(GXContext._get_tls_geo(), db._wrapper, chan.encode(), window, angle, deviation, max_length, deflection, min_length, resample, br_angle)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer