import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
gxc = gx.GXpy()
url = 'https://github.com/GeosoftInc/gxpy/raw/9.3/examples/tutorial/Geosoft%20Databases/'
gxu.url_retrieve(url + 'mag_data.csv')