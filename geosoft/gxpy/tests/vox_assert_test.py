import geosoft.gxpy.gx as gx
import geosoft.gxpy.voxset as gxvox
gx = gx.GXpy()
with gxvox.Voxset.new("test_new", dimension=(35, 50, 12), overwrite=True) as vox:
    print(vox.nx, vox.ny, vox.nz)
