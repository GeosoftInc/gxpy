import unittest
import os
import numpy as np

import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys
import geosoft.gxpy.surface as gxsurf
import geosoft.gxpy.vox as gxvox
import geosoft.gxpy.group as gxgrp
import geosoft.gxpy.spatialdata as gxspd
import geosoft.gxpy.view as gxview
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.viewer as gxviewer
import geosoft.gxpy.coordinate_system as gxcs

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testvoxset.zip'),
                                       folder=cls._gx.temp_folder())
        cls.vox_file = os.path.join(cls.folder, 'test.geosoft_voxel')
        cls.sfile = gxsurf.SurfaceDataset.vox_surface(gxvox.Vox.open(cls.vox_file),
                                                      (0.005, 0.01, 0.02), overwrite=True).file_name

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()
        pass #gxsurf.delete_files(cls.surface_file)

    def test_surfaceProperties(self):
        self.start()

        try:
            with gxsurf.SurfaceDataset.open(self.sfile) as surfdataset:
                self.assertEqual(surfdataset.name, 'test')
                self.assertEqual(surfdataset.file_name, 'test.geosoft_surface')
                self.assertEqual(surfdataset.surface_count, 3)
                self.assertEqual(str(surfdataset.coordinate_system), 'NAD83 / UTM zone 20N')
                surface_name_list = surfdataset.surface_name_list
                self.assertTrue('Isosurface 0.02' in surface_name_list)
                self.assertTrue('Isosurface 0.005'in surface_name_list)
                self.assertTrue('Isosurface 0.01' in surface_name_list)
                self.assertEqual(surfdataset.surface_guid('Isosurface 0.02'), '{ABCDEF02-2345-6789-6945-2301E0BC0A89}')
                self.assertEqual(surfdataset.surface_dict[surfdataset.surface_guid('Isosurface 0.02')],
                                 'Isosurface 0.02')

                for surf in surfdataset:
                    self.assertTrue(surf.verticies_count > 0)
                surf = surfdataset[2]
                self.assertEqual(surf.name, 'Isosurface 0.02')
                self.assertEqual(surf.verticies_count, 21)
                self.assertEqual(surf.faces_count, 26)
                self.assertEqual(surf.component_count, 1)
                self.assertEqual(surf.render_color.rgb, (255, 255, 0))
                self.assertEqual(surf.render_opacity, 1.)
                self.assertEqual(surf.render_style, gxsurf.STYLE_SMOOTH)

        finally:
            gxsurf.delete_files('test')

    def test_new(self):
        self.start()

        with gxsurf.SurfaceDataset.open(self.sfile) as surfdataset:
            with gxsurf.SurfaceDataset.new('new', temp=True) as newsurf:
                nfn = newsurf.file_name
                for surf in surfdataset:
                    newsurf.add_surface(surf)

        with gxsurf.SurfaceDataset.open(nfn) as surfdataset:
            self.assertEqual(surfdataset.surface_count, 3)
            self.assertEqual(str(surfdataset.coordinate_system), 'NAD83 / UTM zone 20N')
            surface_name_list = surfdataset.surface_name_list
            self.assertTrue('Isosurface 0.01' in surface_name_list)
            self.assertTrue('Isosurface 0.02' in surface_name_list)
            self.assertEqual(surfdataset.surface_dict[surfdataset.surface_guid('Isosurface 0.02')], 'Isosurface 0.02')

            for surf in surfdataset:
                self.assertTrue(surf.verticies_count > 0)
            surf = surfdataset['Isosurface 0.02']
            self.assertEqual(surf.name, 'Isosurface 0.02')
            self.assertEqual(surf.verticies_count, 21)
            self.assertEqual(surf.faces_count, 26)
            self.assertEqual(surf.component_count, 1)
            self.assertEqual(surf.render_color.rgb, (255, 255, 0))
            self.assertEqual(surf.render_opacity, 1.)
            self.assertEqual(surf.render_style, gxsurf.STYLE_SMOOTH)

            comp = surf.computed_properties()
            self.assertEqual(comp['components'], 1)
            self.assertEqual(comp['verticies'], 21)
            self.assertEqual(comp['edges'], 46)
            self.assertEqual(comp['triangles'], 26)
            self.assertEqual(comp['inconsistent'], 0)
            self.assertEqual(comp['invalid'], 0)
            self.assertEqual(comp['intersect'], 0)

            f, v = surf.get_mesh_vv()
            f1, f2, f3 = f
            vx, vy, vz = v
            
            self.assertEqual(len(vx), surf.verticies_count)
            self.assertEqual(len(vy), surf.verticies_count)
            self.assertEqual(len(vz), surf.verticies_count)
            self.assertEqual(len(f1), surf.faces_count)
            self.assertEqual(len(f2), surf.faces_count)
            self.assertEqual(len(f3), surf.faces_count)

            f, v = surf.get_mesh_np()
            self.assertEqual(len(f), surf.faces_count)
            self.assertEqual(len(v), surf.verticies_count)

    def test_new_named(self):
        self.start()

        try:
            with gxsurf.SurfaceDataset.open(self.sfile) as surfdataset:
                with gxsurf.SurfaceDataset.new('new') as newsurf:
                    self.assertEqual(newsurf.name, 'new')
                    for surf in surfdataset:
                        newsurf.add_surface(surf)

        finally:
            gxsurf.delete_files('new')

        with gxsurf.SurfaceDataset.open('billy', file_name=self.sfile) as surfdataset:
            self.assertEqual(surfdataset.name, 'billy')


    def test_temp(self):
        self.start()

        fn = gxsurf.SurfaceDataset.vox_surface(gxvox.Vox.open(self.vox_file),
                                               0.01, color=gxgrp.C_GREY, opacity=0.5,
                                               temp=True).file_name

        with gxsurf.SurfaceDataset.open(fn) as surfdataset:
            with gxsurf.SurfaceDataset.new('new', temp=True) as newsurf:
                self.assertEqual(newsurf.name, 'new')
                temp_fn = newsurf.file_name
                for surf in surfdataset:
                    newsurf.add_surface(surf)

        with gxsurf.SurfaceDataset.open(temp_fn) as surfdataset:
            self.assertEqual(surfdataset.surface_count, 1)
            self.assertEqual(str(surfdataset.coordinate_system), 'NAD83 / UTM zone 20N')
            surface_name_list = surfdataset.surface_name_list
            self.assertEqual(surface_name_list[0], 'Isosurface 0.01')
            self.assertEqual(surfdataset.surface_guid('Isosurface 0.01'), '{ABCDEF00-2345-6789-6745-2301DEBC0A89}')
            self.assertEqual(surfdataset.surface_dict[surfdataset.surface_guid('Isosurface 0.01')], 'Isosurface 0.01')
            self.assertEqual(surfdataset.surface_guid('{ABCDEF00-2345-6789-6745-2301DEBC0A89}'),
                                                      '{ABCDEF00-2345-6789-6745-2301DEBC0A89}')

            for surf in surfdataset:
                self.assertTrue(surf.verticies_count > 0)
            surf = surfdataset['Isosurface 0.01']
            self.assertEqual(surf.name, 'Isosurface 0.01')
            self.assertEqual(surf.verticies_count, 482)
            self.assertEqual(surf.faces_count, 855)
            self.assertEqual(surf.component_count, 1)
            self.assertEqual(surf.render_color.rgb, (128, 128, 128))
            self.assertEqual(surf.render_opacity, 0.5)
            self.assertEqual(surf.render_style, gxsurf.STYLE_SMOOTH)
            self.assertEqual(surf.extent, (440718.65079365077,
                                           6129015.476190476,
                                           -954.3756313323975,
                                           441475.0,
                                           6129475.0,
                                           512.5))

    def test_copy(self):
        self.start()

        # make a copy by copying each surface
        with gxsurf.SurfaceDataset.new() as new_sd:
            sd_fn = new_sd.file_name
            with gxsurf.SurfaceDataset.open(self.sfile) as sd:
                for s in sd:
                    new_sd.add_surface(s)

        with gxsurf.SurfaceDataset.open(sd_fn) as sd:
            self.assertEqual(sd.surface_count, 3)
            self.assertTrue('Isosurface 0.005' in sd.surface_name_list)
            self.assertTrue('Isosurface 0.01' in sd.surface_name_list)
            self.assertTrue('Isosurface 0.02' in sd.surface_name_list)
            self.assertAlmostEqual(sd['Isosurface 0.01'].render_opacity, 0.6666666666666666)

            surf = sd['Isosurface 0.01']
            self.assertEqual(surf.extent, (440718.65079365077,
                                           6129015.476190476,
                                           -954.3756313323975,
                                           441475.0,
                                           6129475.0,
                                           512.5))

            with gxsurf.Surface('maki') as s:
                f, t = surf.get_mesh_vv()
                s.add_mesh_vv(f, t)
                self.assertEqual(s.extent, (440718.65079365077,
                                            6129015.476190476,
                                            -954.3756313323975,
                                            441475.0,
                                            6129475.0,
                                            512.5))

    def test_new_mesh(self):
        self.start()

        # make a copy by copying each surface
        with gxsurf.SurfaceDataset.new() as new_sd:
            sd_fn = new_sd.file_name
            with gxsurf.SurfaceDataset.open(self.sfile) as sd:
                for s in sd:
                    f, v = s.get_mesh_np()
                    snew = gxsurf.Surface(s.name)
                    snew.add_mesh(f, v, (gxgrp.C_MAGENTA, 0.25, gxsurf.STYLE_FLAT))
                    new_sd.add_surface(snew)

        with gxsurf.SurfaceDataset.open(sd_fn) as sd:
            self.assertEqual(sd.surface_count, 3)
            self.assertTrue('Isosurface 0.005' in sd.surface_name_list)
            self.assertTrue('Isosurface 0.01' in sd.surface_name_list)
            self.assertTrue('Isosurface 0.02' in sd.surface_name_list)
            self.assertEqual(sd['Isosurface 0.01'].render_opacity, 0.25)
            self.assertEqual(sd['Isosurface 0.02'].render_color.cmy, (0, 255, 0))
            self.assertEqual(sd['Isosurface 0.01'].render_style, gxsurf.STYLE_FLAT)

        with gxview.View_3d.new() as v3d:
            v3d_file = v3d.file_name
            gxsurf.render(v3d, sd_fn, group_name='billy')
        self.crc_map(v3d_file)


    def test_exceptions(self):
        self.start()

        verts = np.array([[0, 0, 0],
                          [5, 0, 0],
                          [5, 5, 0],
                          [0, 3, 5],
                          [2.5, 2, 10]], dtype=np.float64)
        faces = np.array([[0, 1, 2],
                          [0, 2, 3],
                          [3, 2, 4]], dtype=np.int32)

        fn = 'except.geosoft_surface'
        try:
            with open(fn, '+w') as f:
                f.write('maki')
            self.assertRaises(gxsurf.SurfaceException, gxsurf.SurfaceDataset.new, 'except')

        finally:
            gxsurf.delete_files(fn)

        with gxsurf.SurfaceDataset.new('test', temp=True, coordinate_system='WGS 84') as sd:
            s = gxsurf.Surface('maki')
            s.coordinate_system = 'NAD83'
            self.assertEqual(str(s.coordinate_system), 'NAD83')
            self.assertRaises(gxsurf.SurfaceException, sd.add_surface, s)

        fn = gxsurf.SurfaceDataset.vox_surface(gxvox.Vox.open(self.vox_file), 0.01, temp=True).file_name
        with gxsurf.SurfaceDataset.open(self.sfile) as sd:
            self.assertFalse(sd.is_new)
            self.assertTrue(sd.has_surface('Isosurface 0.01'))
            self.assertRaises(gxsurf.SurfaceException, gxsurf.Surface, 'Isosurface 0.01', 'none', sd)
            self.assertRaises(gxsurf.SurfaceException, sd.add_surface, gxsurf.Surface('Isosurface 0.01'))
            self.assertFalse(sd.has_surface('billy'))
            self.assertRaises(gxsurf.SurfaceException, sd.add_surface, gxsurf.Surface('billy', mesh=(faces, verts)))

            with gxsurf.SurfaceDataset.new() as new_sd:
                new_sd.add_surface_dataset(sd)
                self.assertTrue(new_sd.has_surface('Isosurface 0.01'))
                self.assertRaises(gxsurf.SurfaceException, gxsurf.Surface, 'Isosurface 0.01', 'none', new_sd)
                self.assertRaises(gxsurf.SurfaceException, new_sd.add_surface, gxsurf.Surface('Isosurface 0.01'))
                self.assertFalse(new_sd.has_surface('billy'))
                s = gxsurf.Surface('billy', mesh=(faces, verts))
                new_sd.add_surface(s)
                self.assertTrue(new_sd.has_surface('billy'))

        with gxsurf.SurfaceDataset.new() as new_sd:
            new_sd.unit_of_measure = 'nT'
            new_sd.add_surface_dataset(fn)
            self.assertTrue(new_sd.has_surface('Isosurface 0.01'))
            s = new_sd['Isosurface 0.01']
            self.assertEqual(s.surface_type, 'ISOSURFACE')
            self.assertTrue(bool(s.source_dataset))
            self.assertEqual(s.unit_of_measure, 'nT')
            self.assertEqual(s.component_count, 1)

            new_sd.add_surface(gxsurf.Surface('billy', surface_type='maki', mesh=(faces, verts)))
            self.assertTrue(new_sd.has_surface('billy'))
            self.assertEqual(new_sd.surface_guid('billy'), new_sd['billy'].guid)
            s = new_sd['billy']
            self.assertEqual(s.surface_type, 'maki')
            self.assertEqual(s.source_dataset, '')
            self.assertEqual(s.unit_of_measure, 'nT')
            self.assertEqual(s.component_count, 1)
            self.assertEqual(s.render_color, gxgrp.Color(gxgrp.C_GREY))

        with gxsurf.SurfaceDataset.new() as new_sd:
            new_sd.add_surface_dataset(fn)
            self.assertTrue(new_sd.has_surface('Isosurface 0.01'))
            gxsurf.Surface('billy', surface_dataset=new_sd, mesh=(faces, verts))
            self.assertTrue(new_sd.has_surface('billy'))

    def test_render(self):
        self.start()

        with gxview.View_3d.new() as v3d:
            v3d_file = v3d.file_name
            gxsurf.render(v3d, self.sfile)
            self.assertRaises(gxsurf.SurfaceException, gxsurf.render, v3d, self.sfile)
            gxsurf.render(v3d, self.sfile, overwrite=True)
            gxsurf.render(v3d, self.sfile, group_name='maki')
        self.crc_map(v3d_file)

    def test_render_1(self):
        self.start()

        with gxsurf.SurfaceDataset.open(self.sfile) as sd:
            with gxview.View_3d.new() as v3d:
                v3d_file = v3d.file_name
                gxsurf.render(v3d, sd, group_name='sdataset')
        self.crc_map(v3d_file)

    def test_render_2(self):
        self.start()

        with gxsurf.SurfaceDataset.open(self.sfile) as sd:
            surface = sd['Isosurface 0.01']
            with gxview.View_3d.new() as v3d:
                v3d_file = v3d.file_name
                gxsurf.render(v3d, surface, group_name='surface')
        self.crc_map(v3d_file)

    def test_make_my_own(self):
        self.start()

        verts = np.array([[0, 0, 0],
                          [5, 0, 0],
                          [5, 5, 0],
                          [0, 3, 5],
                          [2.5, 2, 10]], dtype=np.float64)
        faces = np.array([[0, 1, 2],
                          [0, 2, 3],
                          [3, 2, 4]], dtype=np.int32)

        with gxsurf.Surface('maki') as s:
            s.add_mesh(faces, verts)

            s.render_color = gxgrp.C_GREEN
            s.render_style = gxsurf.STYLE_FLAT
            with gxview.View_3d.new() as v3d:
                v3d_file = v3d.file_name
                gxsurf.render(v3d, s)
        self.crc_map(v3d_file)

    def test_make_my_own_1(self):
        self.start()

        verts = np.array([[0, 0, 0],
                          [5, 0, 0],
                          [5, 5, 0],
                          [0, 3, 5],
                          [2.5, 2, 10]], dtype=np.float64)
        faces = np.array([[0, 1, 2],
                          [0, 2, 3],
                          [3, 2, 4]], dtype=np.int32)

        with gxsurf.Surface('maki') as s:
            s.add_mesh(faces, verts)
            s.render_color = gxgrp.C_BLUE
            s.render_style = gxsurf.STYLE_SMOOTH
            s.render_opacity = 0.25
            with gxview.View_3d.new() as v3d:
                v3d_file = v3d.file_name
                gxsurf.render(v3d, s)
        self.crc_map(v3d_file)
        # gxviewer.view_document(v3d_file, wait_for_close=True)

    def test_make_my_own_2(self):
        self.start()

        verts = np.array([[0, 0, 0],
                          [5, 0, 0],
                          [5, 5, 0],
                          [0, 3, 5],
                          [2.5, 2, 10]], dtype=np.float64)
        faces = np.array([[0, 1, 2],
                          [0, 2, 3],
                          [3, 2, 4]], dtype=np.int32)

        with gxsurf.Surface('maki') as s:
            s.add_mesh(faces, verts)
            s.render_color = gxgrp.C_RED
            s.render_style = gxsurf.STYLE_EDGE
            s.render_opacity = 1
            with gxview.View_3d.new() as v3d:
                v3d_file = v3d.file_name
                gxsurf.render(v3d, s)
        self.crc_map(v3d_file)
        # gxviewer.view_document(v3d_file, wait_for_close=True)

    def test_fig_map(self):
        self.start()

        verts = np.array([[0, 0, 0],
                          [5, 0, 0],
                          [5, 5, 0],
                          [0, 3, 5],
                          [2.5, 2, 10]], dtype=np.float64)
        faces = np.array([[0, 1, 2],
                          [0, 2, 3],
                          [3, 2, 4]], dtype=np.int32)

        with gxsurf.SurfaceDataset.new() as sd:
            with gxsurf.Surface('maki', surface_dataset=sd) as s:
                s.add_mesh(faces, verts)
                s.render_color = gxgrp.C_RED
                s.render_style = gxsurf.STYLE_FLAT
                s.render_opacity = 1
            fig_map = sd.figure_map().file_name
        self.crc_map(fig_map)
        # gxviewer.view_document(fig_map, wait_for_close=True)

    def test_fig_map_cs(self):
        self.start()

        verts = np.array([[0, 0, 0],
                          [5, 0, 0],
                          [5, 5, 0],
                          [0, 3, 5],
                          [2.5, 2, 10]], dtype=np.float64)
        faces = np.array([[0, 1, 2],
                          [0, 2, 3],
                          [3, 2, 4]], dtype=np.int32)

        with gxsurf.SurfaceDataset.new() as sd:
            sd.coordinate_system = {'type': 'local', 'lon_lat': (-96., 43.), 'azimuth':0}
            with gxsurf.Surface('maki', surface_dataset=sd) as s:
                cs = gxcs.Coordinate_system({'type': 'local', 'lon_lat': (-96., 43.), 'azimuth':20})
                s.add_mesh(faces, verts, coordinate_system=cs)
                s.render_color = gxgrp.C_RED
                s.render_style = gxsurf.STYLE_FLAT
                s.render_opacity = 1
            fig_map = sd.figure_map().file_name
        #self.crc_map(fig_map)
        # gxviewer.view_document(fig_map, wait_for_close=True)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
