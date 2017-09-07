import geosoft.gxpy.gx as gx
import geosoft.gxpy.coordinate_system as gxcs
import numpy as np

gxc = gx.GXpy()

cs_utm = gxcs.Coordinate_system('NAD83 / UTM zone 15N')
cs_nad27 = gxcs.Coordinate_system('NAD27')

cs_transform = gxcs.Coordinate_translate(cs_utm, cs_nad27)
lon_lat = cs_transform.convert((345000, 64250000))

print('(lon, lat): {}'.format(lon_lat))

print('(lon, lat, elevation): {}'.format(cs_transform.convert((345000, 64250000, 50))))

locations = [(345000, 64250000, 50), (345500, 64250000, 60), (346000, 64250000, 70)]
nad27_locations = cs_transform.convert(locations)
for xyz in nad27_locations:
    print(xyz)

data = np.array([[345000, 64250000, 50, 55000],
                 [345500, 64250000, 60, 55150],
                 [346000, 64250000, 70, 56000]],
                dtype=float)
nad27_locations = cs_transform.convert(data, in_place=True)
for xyz in data:
    print(xyz)

print(cs_utm == cs_nad27)
print(gxcs.Coordinate_system('GDA94 [geodetic]') == gxcs.Coordinate_system('GDA94 [geoid]'))