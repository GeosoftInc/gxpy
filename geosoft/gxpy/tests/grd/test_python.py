import sys
import geosoft.gxpy as gxpy
import geosoft.gxpy.utility as gxu
gxc = gxpy.gx.GXpy()
d = gxu.get_shared_dict()
gxpy.utility.set_shared_dict({'a':'letter a', 'b':'letter b', 'c':[1,2,3], 'argv': sys.argv, 'input':d})
