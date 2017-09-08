import arcpy
import os  
import sys
import shutil

import geosoft.gxpy.map as gxmap
from geosoft.gxpy.gx import GXpy


class GeosoftMapImport(object):
    '''
    Imports a 2D view or individual group from a Geosoft map as a GeoTIFF.
    '''
    def __init__(self):
        self.label = "Import Geosoft Map as GeoTIFF"
        self.description = "Geoprocessing tool that imports a 2D view or individual group from a Geosoft map as a GeoTIFF."
        
    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_geosoft_map = arcpy.Parameter(displayName="Input Geosoft Map",
            name="in_geosoft_map",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")

        in_geosoft_map.filter.list = ['map']

        output_tif = arcpy.Parameter(displayName="Output GeoTIFF",
            name="output_tif",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")    
        output_tif.filter.list = ['tif']
        
        parameters = [in_geosoft_map, output_tif]
        
        return parameters

    def isLicensed(self): #optional
        return True


    def updateParameters(self, parameters): #optional
        return

    def updateMessages(self, parameters): #optional
         return

    def execute(self, parameters, messages):
        in_geosoft_map = parameters[0].valueAsText
        output_tif = parameters[1].valueAsText

        with GXpy() as gxp:
            with gxmap.Map.open(in_geosoft_map) as geo_map:
                # TODO Could expose DPI as input parameter but went with normal desktop screen res * 3 for now
                geo_map.export_geotiff(output_tif, dpi=3*96) 

