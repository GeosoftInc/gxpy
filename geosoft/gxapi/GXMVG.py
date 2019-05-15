### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMVIEW import GXMVIEW


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMVG(gxapi_cy.WrapMVG):
    """
    GXMVG class.

    The `GXMVG <geosoft.gxapi.GXMVG>` class provides the ability to create view graphs.
    """

    def __init__(self, handle=0):
        super(GXMVG, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMVG <geosoft.gxapi.GXMVG>`
        
        :returns: A null `GXMVG <geosoft.gxapi.GXMVG>`
        :rtype:   GXMVG
        """
        return GXMVG()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def axis_x(self, d_y, d_lx, d_rx, d_maj_int, d_min_int, d_size):
        """
        Draw an X axis
        
        :param d_y:        Y location in plot units (mm)
        :param d_lx:       Left  X (rescaling unit)
        :param d_rx:       Right X (rescaling unit)
        :param d_maj_int:  Major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale
        :param d_min_int:  Minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR
        :param d_size:     Tick size in view units (mm) (negative for down ticks)
        :type  d_y:        float
        :type  d_lx:       float
        :type  d_rx:       float
        :type  d_maj_int:  float
        :type  d_min_int:  float
        :type  d_size:     float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** When Log annotation is applied, nice tick intervals will be
        calculated

        Obsolete
        """
        self._axis_x(d_y, d_lx, d_rx, d_maj_int, d_min_int, d_size)
        




    def axis_y(self, d_x, d_by, d_ty, d_maj_int, d_min_int, d_size):
        """
        Draw a  Y axis
        
        :param d_x:        X location in plot units (mm)
        :param d_by:       Bottom Y (rescaling unit)
        :param d_ty:       Top Y (rescaling unit)
        :param d_maj_int:  Major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale
        :param d_min_int:  Minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR
        :param d_size:     Tick size in plot units (mm)(negative for left ticks)
        :type  d_x:        float
        :type  d_by:       float
        :type  d_ty:       float
        :type  d_maj_int:  float
        :type  d_min_int:  float
        :type  d_size:     float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** When Log annotation is applied, nice tick intervals will be
        calculated

        Obsolete
        """
        self._axis_y(d_x, d_by, d_ty, d_maj_int, d_min_int, d_size)
        



    @classmethod
    def create(cls, map, name, xmin_m, ymin_m, xmax_m, ymax_m, xmin_u, ymin_u, xmax_u, ymax_u):
        """
        Create a `GXMVG <geosoft.gxapi.GXMVG>` object
        
        :param map:     H_MAP handle
        :param name:    View Name
        :param xmin_m:  Minimum X in map unit (mm)
        :param ymin_m:  Minimum Y in map unit (mm)
        :param xmax_m:  Maximum X in map unit (mm)
        :param ymax_m:  Maximum Y in map unit (mm)
        :param xmin_u:  Minimum X in view unit (m for example)
        :param ymin_u:  Minimum Y in view unit
        :param xmax_u:  Maximum X in view unit
        :param ymax_u:  Maximum Y in view unit
        :type  map:     GXMAP
        :type  name:    str
        :type  xmin_m:  float
        :type  ymin_m:  float
        :type  xmax_m:  float
        :type  ymax_m:  float
        :type  xmin_u:  float
        :type  ymin_u:  float
        :type  xmax_u:  float
        :type  ymax_u:  float

        :returns:       `GXMVG <geosoft.gxapi.GXMVG>` handle (NULL if error)
        :rtype:         GXMVG

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Obsolete
        """
        ret_val = gxapi_cy.WrapMVG._create(GXContext._get_tls_geo(), map, name.encode(), xmin_m, ymin_m, xmax_m, ymax_m, xmin_u, ymin_u, xmax_u, ymax_u)
        return GXMVG(ret_val)






    def get_mview(self):
        """
        Get the `GXMVIEW <geosoft.gxapi.GXMVIEW>` Handle of the Object.
        

        :returns:    `GXMVIEW <geosoft.gxapi.GXMVIEW>` Handle
        :rtype:      GXMVIEW

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Obsolete
        """
        ret_val = self._get_mview()
        return GXMVIEW(ret_val)




    def grid(self, d1st_x, d1st_y, d_x, d_y, d_dx, d_dy, l_type):
        """
        Draw a grid in the current `GXMVG <geosoft.gxapi.GXMVG>`
        
        :param d1st_x:  X position of 1st vertical grid line to draw (in rescaling unit)
        :param d1st_y:  Y position of 1st horizontal grid line to draw (in rescaling unit)
        :param d_x:     X grid increment of rescaled map unit (see above Rescaling functions)
        :param d_y:     Y grid increment of rescaled map unit (see above Rescaling functions)
        :param d_dx:    X dot increment/cross X size of rescaled map unit
        :param d_dy:    Y dot increment/cross Y size of rescaled map unit
        :param l_type:  :ref:`MVG_GRID`
        :type  d1st_x:  float
        :type  d1st_y:  float
        :type  d_x:     float
        :type  d_y:     float
        :type  d_dx:    float
        :type  d_dy:    float
        :type  l_type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The grid will be drawn in the current window.

        In the LOG and LOGLINEAR rescaling modes, grids will be
        drawn in decades and the X/Y grid increments will be
        ignored.  In addition, grid lines at 0 (zero) and LOGMIN will be drawn.

        Obsolete
        """
        self._grid(d1st_x, d1st_y, d_x, d_y, d_dx, d_dy, l_type)
        




    def label_x(self, y, lx, rx, maj_int, just, bound, orient):
        """
        Label annotations on the X axis
        
        :param y:        Y location in plot units (mm)
        :param lx:       Left  X (rescaling unit)
        :param rx:       Right X (rescaling unit)
        :param maj_int:  Major tick interval (ignored if in LOG or LOGLINEAR rescaling)
        :param just:     Label justification :ref:`MVG_LABEL_JUST`
        :param bound:    Edge label bounding :ref:`MVG_LABEL_BOUND`
        :param orient:   Label orientation   :ref:`MVG_LABEL_ORIENT`
        :type  y:        float
        :type  lx:       float
        :type  rx:       float
        :type  maj_int:  float
        :type  just:     int
        :type  bound:    int
        :type  orient:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Label bounding will justify edge labels to be inside
        the bar limits.

        When Log annotation is applied, labels will be drawn in decades.

        Obsolete

        .. seealso::

            sAxisX_MVG
        """
        self._label_x(y, lx, rx, maj_int, just, bound, orient)
        




    def label_y(self, x, by, ty, maj_int, just, bound, orient):
        """
        Label annotations on the Y axis
        
        :param x:        X location in plot units (mm)
        :param by:       Bottom  Y (rescaling unit)
        :param ty:       Top Y (rescaling unit)
        :param maj_int:  Label interval (ignored if in LOG or LOGLINEAR rescaling)
        :param just:     Label justification :ref:`MVG_LABEL_JUST`
        :param bound:    Edge label bounding :ref:`MVG_LABEL_BOUND`
        :param orient:   Label orientation   :ref:`MVG_LABEL_ORIENT`
        :type  x:        float
        :type  by:       float
        :type  ty:       float
        :type  maj_int:  float
        :type  just:     int
        :type  bound:    int
        :type  orient:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Label bounding will justify edge labels to be inside
        the bar limits.

        When Log annotation is applied, labels will be drawn in decades.

        Obsolete

        .. seealso::

            sAxisY_MVG
        """
        self._label_y(x, by, ty, maj_int, just, bound, orient)
        




    def poly_line_va(self, draw, wrap, vv_x, va, vv_array):
        """
        Creates PolyLines/polygons from `GXVV <geosoft.gxapi.GXVV>` and `GXVA <geosoft.gxapi.GXVA>`.
        
        :param draw:      :ref:`MVG_DRAW`
        :param wrap:      :ref:`MVG_WRAP`
        :param vv_x:      X `GXVV <geosoft.gxapi.GXVV>`
        :param va:        Y VAs
        :param vv_array:  `GXVV <geosoft.gxapi.GXVV>` containing list of `GXVA <geosoft.gxapi.GXVA>` ranges, such as 1,2 40 ... Entire `GXVA <geosoft.gxapi.GXVA>` is drawn if this `GXVV <geosoft.gxapi.GXVV>` is empty.
        :type  draw:      int
        :type  wrap:      int
        :type  vv_x:      GXVV
        :type  va:        GXVA
        :type  vv_array:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the `GXVV <geosoft.gxapi.GXVV>` contains dummies, the polylines
        will break at the dummies; the polygons
        will skip the dummies.

        If wrapping is applied, POLYGON parameter is ignored and
        only POLYLINES are drawn.

        Obsolete
        """
        self._poly_line_va(draw, wrap, vv_x, va, vv_array)
        




    def poly_line_vv(self, draw, wrap, vv_x, vv_y):
        """
        Creates PolyLines/polygons from `GXVV <geosoft.gxapi.GXVV>` and `GXVV <geosoft.gxapi.GXVV>`.
        
        :param draw:  :ref:`MVG_DRAW`
        :param wrap:  :ref:`MVG_WRAP`
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`
        :type  draw:  int
        :type  wrap:  int
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the `GXVV <geosoft.gxapi.GXVV>` contains dummies, the polylines
        will break at the dummies; the polygons
        will skip the dummies.

        If wrapping is applied, POLYGON parameter is ignored and
        only POLYLINES are drawn.

        Obsolete
        """
        self._poly_line_vv(draw, wrap, vv_x, vv_y)
        




    def rescale_x_range(self, scale, min, max, log_min):
        """
        Re-scale horizontal axis
        
        :param scale:    :ref:`MVG_SCALE`
        :param min:      Scale information: new minimum X
        :param max:      Scale information: new maximum X
        :param log_min:  Scale information: minimum X to apply log10, it is defined only for LOGLINEAR scale
        :type  scale:    int
        :type  min:      float
        :type  max:      float
        :type  log_min:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** When RescaleX_MVG is used, only the scaling information
        related to X axis will be considered

        Obsolete
        """
        self._rescale_x_range(scale, min, max, log_min)
        




    def rescale_y_range(self, scale, min, max, log_min):
        """
        Re-scale vertical axis
        
        :param scale:    :ref:`MVG_SCALE`
        :param min:      Scale information: new minimum Y
        :param max:      Scale information: new maximum Y
        :param log_min:  Scale information: minimum Y to apply log10, it is defined only for LOGLINEAR scale
        :type  scale:    int
        :type  min:      float
        :type  max:      float
        :type  log_min:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** When RescaleY_MVG is used, only the scaling information
        related to Y axis will be considered

        Obsolete
        """
        self._rescale_y_range(scale, min, max, log_min)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer