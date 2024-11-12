#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrd

gxc = gx.GXpy()

# create a memory grid as an example of a spatial object for this exercise
grid = gxgrd.Grid.new(properties=({'nx': 10, 'ny': 10}))
print(grid.coordinate_system)

# define by a Geosoft-style coordinate system name. Parameters are derived from internal Geosoft tables.
grid.coordinate_system = "NAD83 / UTM zone 17N"
print(grid.coordinate_system)
print(grid.coordinate_system.gxf)
print(grid.coordinate_system.coordinate_dict())

# example use of GXF strings to change the datum to NAD27. Here we remove the name and local datum transform
# and allow the Coordinate_system class to complete parameters for NAD27 from the tables.
gxf = grid.coordinate_system.gxf
gxf[0] = ''
gxf[1] = "NAD27"
gxf[4] = ''
grid.coordinate_system = gxf
print('gxf:', grid.coordinate_system.gxf)

# fully explicit definition of UTM zone 17N on NAD27 datum using GXF string.
grid.coordinate_system = ['',
                          'NAD27',
                          '"Transverse Mercator",0,-87,0.9996,500000,0',
                          'm,1',
                          '"*local_datum",-8,160,176,0,0,0,0']
print('gxf:', grid.coordinate_system.gxf)

# ... from a json string. Note how to properly escape a string embedded in a string.
js = '{"units": "m,1", "datum": "NAD27", "projection": "\\"Transverse Mercator\\",0,-87,0.9996,500000,0"}'
grid.coordinate_system = js
print('json:', grid.coordinate_system.gxf)

# ... from an ESRI WKT string
wkt = 'PROJCS["NAD_1927_UTM_Zone_16N",' + \
          'GEOGCS["GCS_North_American_1927",' + \
          'DATUM["D_North_American_1927",' + \
          'SPHEROID["Clarke_1866",6378206.4,294.9786982]],' + \
          'PRIMEM["Greenwich",0.0],' + \
          'UNIT["Degree",0.0174532925199433]],' + \
          'PROJECTION["Transverse_Mercator"],' + \
          'PARAMETER["False_Easting",500000.0],' + \
          'PARAMETER["False_Northing",0.0],' + \
          'PARAMETER["Central_Meridian",-87.0],' + \
          'PARAMETER["Scale_Factor",0.9996],' + \
          'PARAMETER["Latitude_Of_Origin",0.0],' + \
          'UNIT["Meter",1.0],' + \
          'AUTHORITY["EPSG",26716]]'
grid.coordinate_system = wkt
print('from wkt:', grid.coordinate_system.esri_wkt)
