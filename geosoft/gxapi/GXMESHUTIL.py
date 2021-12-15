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
class GXMESHUTIL(gxapi_cy.WrapMESHUTIL):
    """
    GXMESHUTIL class.

    Mesh utility methods.
    """

    def __init__(self, handle=0):
        super(GXMESHUTIL, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMESHUTIL <geosoft.gxapi.GXMESHUTIL>`
        
        :returns: A null `GXMESHUTIL <geosoft.gxapi.GXMESHUTIL>`
        :rtype:   GXMESHUTIL
        """
        return GXMESHUTIL()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def import_grid_to_surface(cls, grid_file_name, geosurface_filename, surface_name):
        """
        Imports a Grid to a Surface
        
        :param grid_file_name:       Grid File Name
        :param geosurface_filename:  Surface File Name
        :param surface_name:         Surface Item Name within the file
        :type  grid_file_name:       str
        :type  geosurface_filename:  str
        :type  surface_name:         str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._import_grid_to_surface(GXContext._get_tls_geo(), grid_file_name.encode(), geosurface_filename.encode(), surface_name.encode())
        



    @classmethod
    def clip_surface_with_grid(cls, inputSurfaceFile, inputSurface, gridSurfaceFileName, gridSurfaceName, outputSurfaceFile, outputSurfaceNameAbove, outputSurfaceNameBelow, surface_clip_mode):
        """
        Clip a Surface with a Grid Surface (grid converted to surface)
        
        :param inputSurfaceFile:        Input Geosurface file
        :param inputSurface:            Input Surface name within Geosurface file
        :param gridSurfaceFileName:     Grid Surface file name
        :param gridSurfaceName:         Grid surface name within file
        :param outputSurfaceFile:       Output Surface file
        :param outputSurfaceNameAbove:  Name of Surface Item above grid - required for mode=CLIP_ABOVE and CLIP_BOTH
        :param outputSurfaceNameBelow:  Name of Surface Item below grid - required for mode=CLIP_BELOW and CLIP_BOTH
        :param surface_clip_mode:       :ref:`SURFACE_CLIP_MODE`
        :type  inputSurfaceFile:        str
        :type  inputSurface:            str
        :type  gridSurfaceFileName:     str
        :type  gridSurfaceName:         str
        :type  outputSurfaceFile:       str
        :type  outputSurfaceNameAbove:  str
        :type  outputSurfaceNameBelow:  str
        :type  surface_clip_mode:       int

        :returns:                       Surface clip status
        :rtype:                         int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESHUTIL._clip_surface_with_grid(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), gridSurfaceFileName.encode(), gridSurfaceName.encode(), outputSurfaceFile.encode(), outputSurfaceNameAbove.encode(), outputSurfaceNameBelow.encode(), surface_clip_mode)
        return ret_val



    @classmethod
    def clip_surface_with_extents(cls, inputSurfaceFile, inputSurface, outputSurfaceFile, outputSurfaceName, min_x, max_x, min_y, max_y, min_z, max_z):
        """
        Clip a Surface with X,Y,Z extents
        
        :param inputSurfaceFile:   Input Geosurface file
        :param inputSurface:       Input Surface name within Geosurface file
        :param outputSurfaceFile:  Output Surface file
        :param outputSurfaceName:  Output Surface name
        :param min_x:              Min value of X
        :param max_x:              Max value of X
        :param min_y:              Min value of Y
        :param max_y:              Max value of Y
        :param min_z:              Min value of Z
        :param max_z:              Max value of Z
        :type  inputSurfaceFile:   str
        :type  inputSurface:       str
        :type  outputSurfaceFile:  str
        :type  outputSurfaceName:  str
        :type  min_x:              float
        :type  max_x:              float
        :type  min_y:              float
        :type  max_y:              float
        :type  min_z:              float
        :type  max_z:              float

        :returns:                  Surface clip status
        :rtype:                    int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESHUTIL._clip_surface_with_extents(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), outputSurfaceFile.encode(), outputSurfaceName.encode(), min_x, max_x, min_y, max_y, min_z, max_z)
        return ret_val



    @classmethod
    def clip_surface_with_polygon2d(cls, inputSurfaceFile, inputSurface, polygonFile, outputSurfaceFile, outputSurfaceName, maskInside):
        """
        Clip a Surface a specified Polygon file
        
        :param inputSurfaceFile:   Input Geosurface file
        :param inputSurface:       Input Surface name within Geosurface file
        :param polygonFile:        Polygon File
        :param outputSurfaceFile:  Output Surface file
        :param outputSurfaceName:  Output Surface name
        :param maskInside:         Set true if the values inside polygon are to be masked
        :type  inputSurfaceFile:   str
        :type  inputSurface:       str
        :type  polygonFile:        str
        :type  outputSurfaceFile:  str
        :type  outputSurfaceName:  str
        :type  maskInside:         bool

        :returns:                  Surface clip status
        :rtype:                    int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESHUTIL._clip_surface_with_polygon2d(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), polygonFile.encode(), outputSurfaceFile.encode(), outputSurfaceName.encode(), maskInside)
        return ret_val



    @classmethod
    def compute_surface_union(cls, primarySurfaceFile, primarySurface, secondarySurfaceFile, secondarySurface, outputSurfaceFile, outputSurface):
        """
        Compute union of two surfaces
        
        :param primarySurfaceFile:    Primary Geosurface file
        :param primarySurface:        Primary Surface Name within Geosurface File
        :param secondarySurfaceFile:  Secondary Geosurface file
        :param secondarySurface:      Secondary Surface Name within Geosurface File
        :param outputSurfaceFile:     Output surface file
        :param outputSurface:         Output surface name
        :type  primarySurfaceFile:    str
        :type  primarySurface:        str
        :type  secondarySurfaceFile:  str
        :type  secondarySurface:      str
        :type  outputSurfaceFile:     str
        :type  outputSurface:         str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._compute_surface_union(GXContext._get_tls_geo(), primarySurfaceFile.encode(), primarySurface.encode(), secondarySurfaceFile.encode(), secondarySurface.encode(), outputSurfaceFile.encode(), outputSurface.encode())
        



    @classmethod
    def compute_surface_clip(cls, primarySurfaceFile, primarySurface, secondarySurfaceFile, secondarySurface, outputSurfaceFile, outputSurface):
        """
        Clip a surface with another surface, and output the clipped surfaces
        
        :param primarySurfaceFile:    Primary Geosurface file
        :param primarySurface:        Primary Surface Name within Geosurface File
        :param secondarySurfaceFile:  Secondary Geosurface file
        :param secondarySurface:      Secondary Surface Name within Geosurface File
        :param outputSurfaceFile:     Output surface file
        :param outputSurface:         Output surface name
        :type  primarySurfaceFile:    str
        :type  primarySurface:        str
        :type  secondarySurfaceFile:  str
        :type  secondarySurface:      str
        :type  outputSurfaceFile:     str
        :type  outputSurface:         str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._compute_surface_clip(GXContext._get_tls_geo(), primarySurfaceFile.encode(), primarySurface.encode(), secondarySurfaceFile.encode(), secondarySurface.encode(), outputSurfaceFile.encode(), outputSurface.encode())
        



    @classmethod
    def compute_surface_intersection(cls, primarySurfaceFile, primarySurface, secondarySurfaceFile, secondarySurface, outputSurfaceFile, outputSurface):
        """
        Computes and outputs the intersection of two closed surfaces
        
        :param primarySurfaceFile:    Primary Geosurface file
        :param primarySurface:        Primary Surface Name within Geosurface File
        :param secondarySurfaceFile:  Secondary Geosurface file
        :param secondarySurface:      Secondary Surface Name within Geosurface File
        :param outputSurfaceFile:     Output surface file
        :param outputSurface:         Output surface name
        :type  primarySurfaceFile:    str
        :type  primarySurface:        str
        :type  secondarySurfaceFile:  str
        :type  secondarySurface:      str
        :type  outputSurfaceFile:     str
        :type  outputSurface:         str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._compute_surface_intersection(GXContext._get_tls_geo(), primarySurfaceFile.encode(), primarySurface.encode(), secondarySurfaceFile.encode(), secondarySurface.encode(), outputSurfaceFile.encode(), outputSurface.encode())
        



    @classmethod
    def compute_surface_simplification(cls, inputSurfaceFile, inputSurface, outputSurfaceFile, outputSurface):
        """
        Simplifies a surface by reducing the number of edges by half
        
        :param inputSurfaceFile:   Input Geosurface file
        :param inputSurface:       Input Surface Name within Geosurface File
        :param outputSurfaceFile:  Output Geosurface file
        :param outputSurface:      Output Surface Name within Geosurface File
        :type  inputSurfaceFile:   str
        :type  inputSurface:       str
        :type  outputSurfaceFile:  str
        :type  outputSurface:      str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._compute_surface_simplification(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), outputSurfaceFile.encode(), outputSurface.encode())
        



    @classmethod
    def compute_surface_subdivision(cls, inputSurfaceFile, inputSurface, outputSurfaceFile, outputSurface):
        """
        Smooths a surface by applying a loop subdivision algorithm
        
        :param inputSurfaceFile:   Input Geosurface file
        :param inputSurface:       Input Surface Name within Geosurface File
        :param outputSurfaceFile:  Output Geosurface file
        :param outputSurface:      Output Surface Name within Geosurface File
        :type  inputSurfaceFile:   str
        :type  inputSurface:       str
        :type  outputSurfaceFile:  str
        :type  outputSurface:      str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._compute_surface_subdivision(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurface.encode(), outputSurfaceFile.encode(), outputSurface.encode())
        



    @classmethod
    def does_surface_intersect(cls, primarySurfaceFile, primarySurface, secondarySurfaceFile, secondarySurface):
        """
        Checks if the two surfaces intersect at all
        
        :param primarySurfaceFile:    Primary Geosurface file
        :param primarySurface:        Primary Surface Name within Geosurface File
        :param secondarySurfaceFile:  Secondary Geosurface file
        :param secondarySurface:      Secondary Surface Name within Geosurface File
        :type  primarySurfaceFile:    str
        :type  primarySurface:        str
        :type  secondarySurfaceFile:  str
        :type  secondarySurface:      str

        :returns:                     Returns 1 if intersects, 0 if surfaces do not intersect
        :rtype:                       int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESHUTIL._does_surface_intersect(GXContext._get_tls_geo(), primarySurfaceFile.encode(), primarySurface.encode(), secondarySurfaceFile.encode(), secondarySurface.encode())
        return ret_val



    @classmethod
    def does_surface_self_intersect(cls, surfaceFile, surfaceName):
        """
        Checks if a surface self-intersects
        
        :param surfaceFile:  Geosurface file
        :param surfaceName:  Primary Surface Name within Geosurface File
        :type  surfaceFile:  str
        :type  surfaceName:  str

        :returns:            Returns 1 if surface self intersects, 0 if surface has no self-intersections
        :rtype:              int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESHUTIL._does_surface_self_intersect(GXContext._get_tls_geo(), surfaceFile.encode(), surfaceName.encode())
        return ret_val



    @classmethod
    def extract_isosurface_from_voxel(cls, voxelFile, surfaceFile, surfaceName, contourMin, contourMax, close):
        """
        Extracts isosurface from a voxel, and saves the voxel to a Geosurface file
        
        :param voxelFile:    Voxel file
        :param surfaceFile:  Geosurface file
        :param surfaceName:  Surface name within geosurface file
        :param contourMin:   Minimum/higher value
        :param contourMax:   Maximum/lower value
        :param close:        Closed option - create a closed surface?
        :type  voxelFile:    str
        :type  surfaceFile:  str
        :type  surfaceName:  str
        :type  contourMin:   float
        :type  contourMax:   float
        :type  close:        bool

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._extract_isosurface_from_voxel(GXContext._get_tls_geo(), voxelFile.encode(), surfaceFile.encode(), surfaceName.encode(), contourMin, contourMax, close)
        



    @classmethod
    def reproject_geosurface_file(cls, input_surface_filename, output_surface_filename, ipj):
        """
        Repoject surface with the coordinate system of the `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param input_surface_filename:   Input Geosurface file name
        :param output_surface_filename:  Output Geosurface file name
        :param ipj:                      `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the new Geosurface coordinate system
        :type  input_surface_filename:   str
        :type  output_surface_filename:  str
        :type  ipj:                      GXIPJ

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._reproject_geosurface_file(GXContext._get_tls_geo(), input_surface_filename.encode(), output_surface_filename.encode(), ipj)
        



    @classmethod
    def project_geosurface_onto_grid(cls, surface_filename, surface_name, input_geometry_grid, projection_method, output_grid):
        """
        Repoject surface with the coordinate system of the `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param surface_filename:     Input Geosurface file name
        :param surface_name:         Geosurface surface name
        :param input_geometry_grid:  Input Geometry grid
        :param projection_method:    :ref:`SURFACE_PROJECTION_METHOD`
        :param output_grid:          Output grid
        :type  surface_filename:     str
        :type  surface_name:         str
        :type  input_geometry_grid:  str
        :type  projection_method:    int
        :type  output_grid:          str

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._project_geosurface_onto_grid(GXContext._get_tls_geo(), surface_filename.encode(), surface_name.encode(), input_geometry_grid.encode(), projection_method, output_grid.encode())
        



    @classmethod
    def copy_mesh_to_geo_surface_file(cls, input_surface_filename, surface_name, output_surface_filename):
        """
        Copy a mesh from one geosurface file to another
        
        :param input_surface_filename:   Input Geosurface file name
        :param surface_name:             Geosurface surface name
        :param output_surface_filename:  Output Geosurface file name
        :type  input_surface_filename:   str
        :type  surface_name:             str
        :type  output_surface_filename:  str

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._copy_mesh_to_geo_surface_file(GXContext._get_tls_geo(), input_surface_filename.encode(), surface_name.encode(), output_surface_filename.encode())
        



    @classmethod
    def apply_transformation(cls, inputSurfaceFile, inputSurfaceName, outputSurfaceFile, outputSurfaceName, transformationMethod, x, y, z):
        """
        Applies a transformation to a surface, see :ref:`SURFACE_TRANSFORMATION_METHOD`for available operations. The existing mesh will be preserved, and a new mesh will be created with the target name in the target file. Reprojection willbe handled automatically in the case that the coordinate systems differ.
        
        :param inputSurfaceFile:      Input surface file name
        :param inputSurfaceName:      Input surface layer (mesh) name
        :param outputSurfaceFile:     Output surface file name
        :param outputSurfaceName:     Output surface layer (mesh) name
        :param transformationMethod:  :ref:`SURFACE_TRANSFORMATION_METHOD`
        :param x:                     X transformation component
        :param y:                     Y transformation component
        :param z:                     Z transformation component
        :type  inputSurfaceFile:      str
        :type  inputSurfaceName:      str
        :type  outputSurfaceFile:     str
        :type  outputSurfaceName:     str
        :type  transformationMethod:  int
        :type  x:                     float
        :type  y:                     float
        :type  z:                     float

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMESHUTIL._apply_transformation(GXContext._get_tls_geo(), inputSurfaceFile.encode(), inputSurfaceName.encode(), outputSurfaceFile.encode(), outputSurfaceName.encode(), transformationMethod, x, y, z)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer