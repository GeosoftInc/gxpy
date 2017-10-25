### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMVIEW import GXMVIEW


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMVG:
    """
    GXMVG class.

    The :class:`geosoft.gxapi.GXMVG` class provides the ability to create view graphs.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMVG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXMVG`
        
        :returns: A null :class:`geosoft.gxapi.GXMVG`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMVG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMVG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def axis_x(self, p2, p3, p4, p5, p6, p7):
        """
        Draw an X axis

        **Note:**

        When Log annotation is applied, nice tick intervals will be
        calculated
        
        Obsolete
        """
        self._wrapper.axis_x(p2, p3, p4, p5, p6, p7)
        




    def axis_y(self, p2, p3, p4, p5, p6, p7):
        """
        Draw a  Y axis

        **Note:**

        When Log annotation is applied, nice tick intervals will be
        calculated
        
        Obsolete
        """
        self._wrapper.axis_y(p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def create(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Create a :class:`geosoft.gxapi.GXMVG` object

        **Note:**

        Obsolete
        """
        ret_val = gxapi_cy.WrapMVG.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10)
        return GXMVG(ret_val)






    def get_mview(self):
        """
        Get the :class:`geosoft.gxapi.GXMVIEW` Handle of the Object.

        **Note:**

        Obsolete
        """
        ret_val = self._wrapper.get_mview()
        return GXMVIEW(ret_val)




    def grid(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Draw a grid in the current :class:`geosoft.gxapi.GXMVG`

        **Note:**

        The grid will be drawn in the current window.
        
        In the LOG and LOGLINEAR rescaling modes, grids will be
        drawn in decades and the X/Y grid increments will be
        ignored.  In addition, grid lines at 0 (zero) and LOGMIN will be drawn.
        
        Obsolete
        """
        self._wrapper.grid(p2, p3, p4, p5, p6, p7, p8)
        




    def label_x(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Label annotations on the X axis

        **Note:**

        Label bounding will justify edge labels to be inside
        the bar limits.
        
        When Log annotation is applied, labels will be drawn in decades.
        
        Obsolete
        """
        self._wrapper.label_x(p2, p3, p4, p5, p6, p7, p8)
        




    def label_y(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Label annotations on the Y axis

        **Note:**

        Label bounding will justify edge labels to be inside
        the bar limits.
        
        When Log annotation is applied, labels will be drawn in decades.
        
        Obsolete
        """
        self._wrapper.label_y(p2, p3, p4, p5, p6, p7, p8)
        




    def poly_line_va(self, p2, p3, p4, p5, p6):
        """
        Creates PolyLines/polygons from :class:`geosoft.gxapi.GXVV` and :class:`geosoft.gxapi.GXVA`.

        **Note:**

        If the :class:`geosoft.gxapi.GXVV` contains dummies, the polylines
        will break at the dummies; the polygons
        will skip the dummies.
        
        If wrapping is applied, POLYGON parameter is ignored and
        only POLYLINES are drawn.
        
        Obsolete
        """
        self._wrapper.poly_line_va(p2, p3, p4._wrapper, p5._wrapper, p6._wrapper)
        




    def poly_line_vv(self, p2, p3, p4, p5):
        """
        Creates PolyLines/polygons from :class:`geosoft.gxapi.GXVV` and :class:`geosoft.gxapi.GXVV`.

        **Note:**

        If the :class:`geosoft.gxapi.GXVV` contains dummies, the polylines
        will break at the dummies; the polygons
        will skip the dummies.
        
        If wrapping is applied, POLYGON parameter is ignored and
        only POLYLINES are drawn.
        
        Obsolete
        """
        self._wrapper.poly_line_vv(p2, p3, p4._wrapper, p5._wrapper)
        




    def rescale_x_range(self, p2, p3, p4, p5):
        """
        Re-scale horizontal axis

        **Note:**

        When RescaleX_MVG is used, only the scaling information
        related to X axis will be considered
        
        Obsolete
        """
        self._wrapper.rescale_x_range(p2, p3, p4, p5)
        




    def rescale_y_range(self, p2, p3, p4, p5):
        """
        Re-scale vertical axis

        **Note:**

        When RescaleY_MVG is used, only the scaling information
        related to Y axis will be considered
        
        Obsolete
        """
        self._wrapper.rescale_y_range(p2, p3, p4, p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer