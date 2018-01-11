import os
import numpy as np

import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.surface as gxsurf
import geosoft.gxpy.vox as gxvox
import geosoft.gxpy.group as gxgrp
import geosoft.gxpy.spatialdata as gxspd
import geosoft.gxpy.view as gxview
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.vv as gxvv

gxc = gx.GXpy()

def t1():
    verts = np.array([[0, 0, 0],
                      [5, 0, 0],
                      [5, 5, 0],
                      [0, 3, 5],
                      [2.5, 2, 10],
                      [-3, 6, 8],
                      [-4, 0, 12]], dtype=np.float64)
    faces = np.array([[0, 1, 2],
                      [0, 2, 3],
                      [3, 2, 4],
                      [1, 2, 4],
                      [3, 4, 5],
                      [6, 4, 5]], dtype=np.int32)

    with gxsurf.Surface('maki') as s:
        s.add_mesh_np(faces, verts)
        s.render_color = gxgrp.C_CYAN
        s.render_style = gxsurf.STYLE_FLAT
        with gxview.View_3d.new() as v3d:
            v3d_file = v3d.file_name
            gxsurf.draw_surface(v3d, s)

def t2():
    with gxvox.Vox.open('C:\\Development\\github\\gxpy\\examples\\tutorial\\Geosoft Voxels\\rjsmith_voxi_density') as vox:
        with gxsurf.SurfaceDataset.vox_surface(vox, (0.01, 0.02), temp=True) as s:
            with gxview.View_3d.new() as v3d:
                v3d_file = v3d.file_name
                gxsurf.draw_surface(v3d, s)

def t3():
    verts = np.array([[0, 0, 0],
                      [5, 0, 0],
                      [5, 5, 0],
                      [0, 3, 5],
                      [2.5, 2, 10],
                      [-3, 6, 8],
                      [-4, 0, 12]], dtype=np.float64)
    faces = np.array([[0, 1, 2],
                      [0, 2, 3],
                      [3, 2, 4],
                      [1, 2, 4],
                      [3, 4, 5],
                      [6, 4, 5]], dtype=np.int32)

    with gxview.View_3d.new() as v3d:
        v3d_file = v3d.file_name
        with gxgrp.Draw_3d(v3d, 'Surface') as g:
            g.surface(faces, verts)
    image_file = gxmap.Map.open(v3d_file).image_file(pix_width=800)
    pass


t3()
pass
