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
class GX3DV(gxapi_cy.Wrap3DV):
    """
    GX3DV class.

    TODO...
    """

    def __init__(self, handle=0):
        super(GX3DV, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GX3DV <geosoft.gxapi.GX3DV>`
        
        :returns: A null `GX3DV <geosoft.gxapi.GX3DV>`
        :rtype:   GX3DV
        """
        return GX3DV()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def open_mview(self, mode):
        """
        Open `GX3DV <geosoft.gxapi.GX3DV>`'s 3D `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        
        :param mode:  :ref:`GEO3DV_OPEN`
        :type  mode:  int

        :returns:     `GXMVIEW <geosoft.gxapi.GXMVIEW>`, aborts on failure
        :rtype:       GXMVIEW

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._open_mview(mode)
        return GXMVIEW(ret_val)




    def copy_to_map(self, map, mview, min_x, min_y, max_x, max_y, force_overwrite, new_view, problem_files):
        """
        Copy the `GX3DV <geosoft.gxapi.GX3DV>`'s 3D `GXMVIEW <geosoft.gxapi.GXMVIEW>` into a map.
        
        :param map:              `GXMAP <geosoft.gxapi.GXMAP>` Object
        :param mview:            Desired new view name
        :param min_x:            X minimum in mm
        :param min_y:            Y minimun in mm
        :param max_x:            X maximum in mm
        :param max_y:            Y maximum in mm
        :param force_overwrite:  (0 - Produce errors for conflicting unpacked files, 1 - Force overwrites of conflicting unpacked files)
        :param new_view:         New view name created
        :param problem_files:    List of files that are problematic returned
        :type  map:              GXMAP
        :type  mview:            str
        :type  min_x:            float
        :type  min_y:            float
        :type  max_x:            float
        :type  max_y:            float
        :type  force_overwrite:  int
        :type  new_view:         str_ref
        :type  problem_files:    str_ref

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A `GX3DV <geosoft.gxapi.GX3DV>` packs all source files. This functions creates an unpacked map and
        unpacks the packed files in the same way that UnPackFilesEx in the `GXMAP <geosoft.gxapi.GXMAP>` class does.
        """
        new_view.value, problem_files.value = self._copy_to_map(map, mview.encode(), min_x, min_y, max_x, max_y, force_overwrite, new_view.value.encode(), problem_files.value.encode())
        



    @classmethod
    def create_new(cls, file_name, mview):
        """
        Create a new `GX3DV <geosoft.gxapi.GX3DV>`.
        
        :param file_name:  `GX3DV <geosoft.gxapi.GX3DV>` file name
        :param mview:      3D `GXMVIEW <geosoft.gxapi.GXMVIEW>` to create new `GX3DV <geosoft.gxapi.GX3DV>` from
        :type  file_name:  str
        :type  mview:      GXMVIEW

        :returns:          `GX3DV <geosoft.gxapi.GX3DV>` Object
        :rtype:            GX3DV

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.Wrap3DV._create_new(GXContext._get_tls_geo(), file_name.encode(), mview)
        return GX3DV(ret_val)



    @classmethod
    def open(cls, file_name):
        """
        Open an existing `GX3DV <geosoft.gxapi.GX3DV>`.
        
        :param file_name:  `GX3DV <geosoft.gxapi.GX3DV>` file name
        :type  file_name:  str

        :returns:          `GX3DV <geosoft.gxapi.GX3DV>` Object
        :rtype:            GX3DV

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.Wrap3DV._open(GXContext._get_tls_geo(), file_name.encode())
        return GX3DV(ret_val)



    @classmethod
    def from_map(cls, map):
        """
        Get an `GX3DV <geosoft.gxapi.GX3DV>` from `GXMAP <geosoft.gxapi.GXMAP>` handle (e.g. from `GXEMAP.lock <geosoft.gxapi.GXEMAP.lock>` on open geosoft_3dv document in project)
        
        :param map:  `GXMAP <geosoft.gxapi.GXMAP>` Object
        :type  map:  GXMAP

        :returns:    `GX3DV <geosoft.gxapi.GX3DV>` Object
        :rtype:      GX3DV

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.Wrap3DV._from_map(GXContext._get_tls_geo(), map)
        return GX3DV(ret_val)




    def crc_3dv(self, crc, file):
        """
        Generate an XML CRC of a `GX3DV <geosoft.gxapi.GX3DV>`
        
        :param crc:   CRC returned
        :param file:  Name of xml to generate (.zip added)
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        crc.value = self._crc_3dv(crc.value, file.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer