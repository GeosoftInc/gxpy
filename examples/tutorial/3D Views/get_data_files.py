#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
gxc = gx.GXpy()
url = 'https://github.com/GeosoftInc/gxpy/raw/9.3/examples/tutorial/3D%20Views/'
gxu.url_retrieve(url + 'Wittichica Creek Residual Total Field.grd')
gxu.url_retrieve(url + 'Wittichica Creek Residual Total Field.grd.gi')
gxu.url_retrieve(url + 'Wittichica Creek Residual Total Field.grd.xml')
gxu.url_retrieve(url + 'Wittichica DEM.grd')
gxu.url_retrieve(url + 'Wittichica DEM.grd.gi')
gxu.url_retrieve(url + 'Wittichica DEM.grd.xml')