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
class GXDXFI:
    """
    GXDXFI class.

    The `GXDXFI <geosoft.gxapi.GXDXFI>` class is used for importing AutoCAD® dxf files into Geosoft maps.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDXFI(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDXFI`
        
        :returns: A null `GXDXFI`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDXFI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDXFI`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        Create `GXDXFI <geosoft.gxapi.GXDXFI>`.
        
        :param name:  DXF file name
        :type  name:  str

        :returns:     `GXDXFI <geosoft.gxapi.GXDXFI>` Object
        :rtype:       GXDXFI

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapDXFI.create(GXContext._get_tls_geo(), name.encode())
        return GXDXFI(ret_val)





    @classmethod
    def dxf2_ply(cls, ply, dxfi):
        """
        Convert a DXF file to a `GXPLY <geosoft.gxapi.GXPLY>` object
        
        :param ply:   `GXPLY <geosoft.gxapi.GXPLY>` handle
        :param dxfi:  `GXDXFI <geosoft.gxapi.GXDXFI>` handle
        :type  ply:   GXPLY
        :type  dxfi:  GXDXFI

        .. versionadded:: 5.1.6
        """
        gxapi_cy.WrapDXFI.dxf2_ply(GXContext._get_tls_geo(), ply._wrapper, dxfi._wrapper)
        




    def dxf2_view_ex(self, view, max_pen, pb_group, group, pb_one_color, color):
        """
        Draw entities in a DXF file to a view in a map
        
        :param max_pen:       User defined number of pens to use (can be `iDUMMY <geosoft.gxapi.iDUMMY>`)
        :param pb_group:      TRUE to place entire DXF in one group
        :param group:         Group name for one group (can be "" if above is FALSE)
        :param pb_one_color:  TRUE to force one color
        :param color:         :ref:`MVIEW_COLOR` (ignored if above is FALSE)
        :type  view:          GXMVIEW
        :type  max_pen:       int
        :type  pb_group:      int
        :type  group:         str
        :type  pb_one_color:  int
        :type  color:         int

        .. versionadded:: 6.2
        """
        self._wrapper.dxf2_view_ex(view._wrapper, max_pen, pb_group, group.encode(), pb_one_color, color)
        




    def get_range(self, min_x, max_x, min_y, max_y, min_z, max_z):
        """
        Get DXF data range
        
        :param min_x:  X min
        :param max_x:  X max
        :param min_y:  Y min
        :param max_y:  Y max
        :param min_z:  Z min
        :param max_z:  Z max
        :type  min_x:  float_ref
        :type  max_x:  float_ref
        :type  min_y:  float_ref
        :type  max_y:  float_ref
        :type  min_z:  float_ref
        :type  max_z:  float_ref

        .. versionadded:: 6.2
        """
        min_x.value, max_x.value, min_y.value, max_y.value, min_z.value, max_z.value = self._wrapper.get_range(min_x.value, max_x.value, min_y.value, max_y.value, min_z.value, max_z.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer