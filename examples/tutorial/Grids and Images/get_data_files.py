#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
gxc = gx.GXpy()
url = 'https://github.com/GeosoftInc/gxpy/raw/9.3/examples/tutorial/Grids%20and%20Images/'
gxu.url_retrieve(url + 'elevation_surfer.GRD')
gxu.url_retrieve(url + 'elevation')
gxu.url_retrieve(url + 'elevation.ers')
gxu.url_retrieve(url + 'elevation.ers.gi')
gxu.url_retrieve(url + 'elevation.ers.xml')