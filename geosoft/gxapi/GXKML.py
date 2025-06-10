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
class GXKML(gxapi_cy.WrapKML):
    """
    GXKML class.

    `GXKML <geosoft.gxapi.GXKML>` functions provide an interface KML (Keyhole markup language) files.

    **Note:**

    None.
    """

    def __init__(self, handle=0):
        super(GXKML, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXKML <geosoft.gxapi.GXKML>`
        
        :returns: A null `GXKML <geosoft.gxapi.GXKML>`
        :rtype:   GXKML
        """
        return GXKML()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def import_3d_polygon(cls, mview, name, vv_vx, vv_vy, vv_vz, color, extruded):
        """
        
        Imports a KML 3D polygon into a provided view.
        
        :param mview:     `GXMVIEW <geosoft.gxapi.GXMVIEW>` object - the (3d) view to import the polygon into.
        :param name:      The name of the resulting polygon group.
        :param vv_vx:     X Vertex Components - VV of GS_REAL
        :param vv_vy:     Y Vertex Components - VV of GS_REAL
        :param vv_vz:     Z Vertex Components - VV of GS_REAL
        :param color:     The colour of the resulting surface - COL_ANY.
        :param extruded:  Extrude the polygon to the base - BOOL.
        :type  mview:     GXMVIEW
        :type  name:      str
        :type  vv_vx:     GXVV
        :type  vv_vy:     GXVV
        :type  vv_vz:     GXVV
        :type  color:     int
        :type  extruded:  bool
        :rtype:           int

        .. versionadded:: 9.10

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Requirements -- The MVIEW must be 3D and valid (see `GXMVIEW.is_view_3d <geosoft.gxapi.GXMVIEW.is_view_3d>`);- The group name must not be null/empty;- The three VV for vector components must contain vertices, and be of equal length.
        """
        
        ret_val = gxapi_cy.WrapKML._import_3d_polygon(GXContext._get_tls_geo(), mview, name.encode(), vv_vx, vv_vy, vv_vz, color, extruded)
        return ret_val



    @classmethod
    def import_3d_line_path(cls, mview, name, vv_vx, vv_vy, vv_vz, color, extruded):
        """
        
        Imports a KML 3D LinePath into a provided view.
        
        :param mview:     `GXMVIEW <geosoft.gxapi.GXMVIEW>` object - the (3d) view to import the LinePath into.
        :param name:      The name of the resulting LinePath group.
        :param vv_vx:     X Vertex Components - VV of GS_REAL
        :param vv_vy:     Y Vertex Components - VV of GS_REAL
        :param vv_vz:     Z Vertex Components - VV of GS_REAL
        :param color:     The colour of the resulting surface - COL_ANY.
        :param extruded:  Extrude the LinePath to the base - BOOL.
        :type  mview:     GXMVIEW
        :type  name:      str
        :type  vv_vx:     GXVV
        :type  vv_vy:     GXVV
        :type  vv_vz:     GXVV
        :type  color:     int
        :type  extruded:  bool
        :rtype:           int

        .. versionadded:: 9.10

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Requirements -- The MVIEW must be 3D and valid (see `GXMVIEW.is_view_3d <geosoft.gxapi.GXMVIEW.is_view_3d>`);- The group name must not be null/empty;- The three VV for vector components must contain vertices, and be of equal length.
        """
        
        ret_val = gxapi_cy.WrapKML._import_3d_line_path(GXContext._get_tls_geo(), mview, name.encode(), vv_vx, vv_vy, vv_vz, color, extruded)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer