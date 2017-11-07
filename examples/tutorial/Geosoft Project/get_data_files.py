import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
gxc = gx.GXpy()
url = 'https://github.com/GeosoftInc/gxpy/raw/9.3/examples/tutorial/Geosoft%20Project/'
gxu.url_retrieve(url, 'example.gpf')
gxu.url_retrieve(url, 'geosoft_project.gpf')
gxu.url_retrieve(url, 'TMI.GRD')
gxu.url_retrieve(url, 'TMI.GRD.gi')
gxu.url_retrieve(url, 'TMI.GRD.xml')