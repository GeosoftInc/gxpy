import arcpy
import os  
import sys

import geosoft.gxpy.grid as gxgrd
from geosoft.gxpy.gx import GXpy


def ValidateRasterPath(name, path):  
    dsname = arcpy.ValidateTableName(name, path)  
    # Truncate to 13 characters to prevent errors (this is probably a hangover
    # from ArcInfo days)
    dsname = dsname[:13]  
    return os.path.join(path,dsname)


class GeosoftGridImport(object):
    '''
    Converts a Geosoft Grid into
    a raster supported in ArcGIS Products.
    '''
    def __init__(self):
        self.label = "Import Geosoft Grid"
        self.description = "Geoprocessing tool that converts a Geosoft grid (.grd) into  a raster supported in ArcGIS Products."
        self.out_formats = {
            'TIFF': 'TIFF',
            'ERDAS IMAGINE': 'IMAGINE Image',
            'BMP': 'BMP',
            'GIF': 'GIF',
            'PNG': 'PNG',
            'JPEG': 'JPEG',
            'JPEG 2000': 'JP2',
            'Esri Grid': 'GRID',
            'Esri BIL': 'BIL',
            'Esri BSQ': 'BSQ',
            'ESRI BIP': 'BIP',
            'ENVI': 'ENVI'
        }
        
    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_grid = arcpy.Parameter(displayName="Input Grid",
            name="in_grid",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")

        # Define a file filter that includes .grd only for now.
        # TODO: We could support others here that we support but which is not
        # in ESRI's GDAL build
        in_grid.filter.list = ['grd']

        out_raster = arcpy.Parameter(displayName="Output Raster",
            name="out_raster",
            datatype="DERasterDataset",
            parameterType="Required",
            direction="Output")    
        
        raster_format = arcpy.Parameter(displayName='Raster Format',
                name='raster_format',
                datatype='GPString',
                parameterType='Required',
                direction='Input')
        raster_format.filter.type = 'ValueList'
        raster_format.filter.list = sorted(list(self.out_formats.keys()))
        raster_format.value = 'Esri Grid'
        raster_format.parameterDependencies = [out_raster.name]

        parameters = [in_grid, out_raster, raster_format]
        
        return parameters

    def isLicensed(self): #optional
        return True

    def updateParameters(self, parameters): #optional
        if parameters[1].valueAsText:
            out_raster = parameters[1].valueAsText
            out_name, out_ext = os.path.splitext(os.path.basename(out_raster))
            out_path = os.path.dirname(out_raster)
            out_raster = ValidateRasterPath(out_name, out_path) + '.' + out_ext            
            parameters[2].enabled = not out_path.endswith('.gdb') # If destination is inside a file geodatabase this parameter has no effect
        return

    def updateMessages(self, parameters): #optional
        return

    def execute(self, parameters, messages):
        in_grid = parameters[0].valueAsText
        out_raster = parameters[1].valueAsText

        temp_gxf = arcpy.CreateScratchName("tmp", ".gxf",
            data_type="RasterDataset",
            workspace=arcpy.env.scratchFolder)

        with GXpy() as gxp:
            with gxgrd.Grid.open(in_grid) as grd:
                gxf_out_name = gxgrd.Grid.decorate_name(temp_gxf, 'GXF,Comp=0')
        
                with gxgrd.Grid.copy(grd, file_name=gxf_out_name) as gxf_grd:
                    del gxf_grd
            try:
                out_path = os.path.dirname(out_raster)
                if out_path.endswith('.gdb'):
                    arcpy.CopyRaster_management(temp_gxf, out_raster, nodata_value=-1e32)
                else:
                    raster_format = parameters[2].valueAsText
                    arcpy.CopyRaster_management(temp_gxf, out_raster, nodata_value=-1e32, format=self.out_formats[raster_format])
            finally:             
                with gxgrd.Grid.open(gxf_out_name) as gxf_grd:
                    gxf_grd.delete_files()

