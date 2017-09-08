# -*- coding: utf-8 -*-
r""""""
__all__ = ['GeosoftGridImport', 'GeosoftMapImport']
__alias__ = 'geosoftarcpy'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('GeosoftGridImport_geosoft', None)
def GeosoftGridImport(in_grid=None, out_raster=None, raster_format=None):
    """GeosoftGridImport_geosoft(in_grid, out_raster, raster_format)

     INPUTS:
      in_grid (File)
      raster_format (String)

     OUTPUTS:
      out_raster (Raster Dataset)"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GeosoftGridImport_geosoft(*gp_fixargs((in_grid, out_raster, raster_format), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('GeosoftMapImport_geosoft', None)
def GeosoftMapImport(in_geosoft_map=None, output_file=None):
    """GeosoftMapImport_geosoft(in_geosoft_map, output_file)

     INPUTS:
      in_geosoft_map (File)

     OUTPUTS:
      output_file (Raster Dataset)"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GeosoftMapImport_geosoft(*gp_fixargs((in_geosoft_map, output_file), True)))
        return retval
    except Exception as e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject