#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
gxc = gx.GXpy()
url = 'https://github.com/GeosoftInc/gxpy/raw/9.3/examples/tutorial/Geosoft%20modules%20-%20gxapi%20and%20gxpy/'
gxu.url_retrieve(url + 'test.grd')
gxu.url_retrieve(url + 'test.grd.gi')