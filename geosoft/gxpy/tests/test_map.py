import unittest
import os
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxv
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.system as gxsys
import geosoft.gxpy.group as gxg
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.utility as gxu

from base import GXPYTest


class Test(GXPYTest):

    def _new_data_map(self, mapname=None, rescale=1.0):

        if mapname is None:
            mapname = os.path.join(self.gx.temp_folder(), 'test')

        with gxmap.Map.new(mapname, overwrite=True) as map:
            with gxv.View(map, "rectangle_test") as v:
                with gxg.Draw(v, 'rectangle') as g:
                    g.rectangle((gxgm.Point((0, 0)), gxgm.Point((250, 110))), pen=gxg.Pen(line_thick=1))

                    p1 = gxgm.Point((5, 5)) * rescale
                    p2 = gxgm.Point((100, 100)) * rescale
                    poff = gxgm.Point((10, 5)) * rescale
                    g.pen = gxg.Pen(fill_color=gxg.C_LT_GREEN)
                    g.rectangle((p1, p2))

                    g.pen = gxg.Pen(line_style=2, line_pitch=2.0)
                    g.line((p1 + poff, p2 - poff))

            with gxv.View(map, "poly") as v:
                with gxg.Draw(v, 'poly') as g:
                    plinelist = [[110, 5],
                                 [120, 20],
                                 [130, 15],
                                 [150, 50],
                                 [160, 70],
                                 [175, 35],
                                 [190, 65],
                                 [220, 50],
                                 [235, 18.5]]
                    pp = gxgm.PPoint.from_list(plinelist) * rescale
                    g.pen = gxg.Pen(line_style=2, line_pitch=2.0)
                    g.polyline(pp)
                    g.pen = gxg.Pen(line_style=4, line_pitch=2.0, line_smooth=gxg.SMOOTH_AKIMA)
                    g.polyline(pp)

                    ppp = np.array(plinelist)
                    pp = gxgm.PPoint(ppp[3:, :]) * rescale
                    g.pen = gxg.Pen(line_style=5, line_pitch=5.0,
                                    line_smooth=gxg.SMOOTH_CUBIC,
                                    line_color=gxapi.C_RED,
                                    line_thick=0.25,
                                    fill_color=gxapi.C_LT_BLUE)
                    g.polyline(pp, close=True)

                    g.pen = gxg.Pen(fill_color=gxapi.C_LT_GREEN)
                    pp = (pp - (100, 0, 0)) / 2 + (100, 0, 0)
                    g.polyline(pp, close=True)
                    pp += (0, 25, 0)
                    g.pen = gxg.Pen(fill_color=gxapi.C_LT_RED)
                    g.polyline(pp, close=True)

            return map.file_name

    def _data_map(self, name=None, data_area=(1000, 0, 11000, 5000), margins=None, coordinate_system=None):

        if name is None:
            name = os.path.join(self.gx.temp_folder(), "test")
        gxmap.delete_files(name)
        if coordinate_system is None:
            coordinate_system = gxcs.Coordinate_system("WGS 84 / UTM zone 15N")
        if margins is None:
            margins = (1.5, 1.5, 3, 1)
        return gxmap.Map.new(file_name=name,
                             data_area=data_area,
                             coordinate_system=coordinate_system,
                             media="A4",
                             margins=margins,
                             inside_margin=0.5)

    def test_version(self):
        self.start()
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_newmap(self):
        self.start()

        # test map
        name = 'test_newmap'
        gxmap.delete_files(name)
        with gxmap.Map.new(name) as map:
            self.assertEqual(map.name, name)
            mapfile = map.file_name
            self.assertEqual(mapfile, os.path.abspath((name + '.map')))
        self.assertTrue(os.path.isfile(mapfile))

        # verify can't write on a new map
        self.assertRaises(gxmap.MapException, gxmap.Map.new, name)
        self.assertRaises(gxmap.MapException, gxmap.Map.new, mapfile)
        with gxmap.Map.new(name, overwrite=True):
            pass

        # but I can open it
        with gxmap.Map.open(name):
            pass
        with gxmap.Map.open(mapfile):
            pass

        gxmap.delete_files(mapfile)
        self.assertFalse(os.path.isfile(mapfile))

        self.assertRaises(gxmap.MapException, gxmap.Map, 'bogus')

    def test_new_geosoft_map(self):
        self.start()

        # temp map
        with gxmap.Map.new(data_area=(0, 0, 100, 80)) as map:
            views = map.view_list
            self.assertTrue('base' in views)
            self.assertTrue('data' in views)
            self.assertEqual(len(map.aggregate_list()), 0)

        with gxmap.Map.new(data_area=(0, 0, 100, 80),
                             coordinate_system=gxcs.Coordinate_system("DHDN / Okarito 2000 [geodetic]")) as map:
            with gxv.View(map, 'data', mode=gxv.WRITE_OLD) as v:
                self.assertEqual("DHDN / Okarito 2000 [geodetic]", str(v.coordinate_system))

            self.assertEqual(map.current_data_view, 'data')
            self.assertEqual(map.current_base_view, 'base')
            self.assertEqual(map.current_section_view, 'section')

            # the following does not make sense, for testing purposes only
            map.current_data_view = 'base'
            self.assertEqual(map.current_data_view, 'base')
            map.current_base_view = 'data'
            self.assertEqual(map.current_base_view, 'data')
            map.current_section_view = 'data'
            self.assertEqual(map.current_section_view, 'data')

    def test_lists(self):
        self.start()

        mapname = self._new_data_map()
        with gxmap.Map.open(mapname) as map:
            views = map.view_list
            self.assertTrue('rectangle_test' in views)
            self.assertTrue('poly' in views)

            views = map.view_list_2D
            self.assertTrue('rectangle_test' in views)
            self.assertTrue('poly' in views)

            views = map.view_list_3D
            self.assertEqual(len(views), 0)

    def test_map_delete(self):
        self.start()

        with gxmap.Map.new(file_name='test_geosoft', overwrite=True) as map:
            file_name = map.file_name
            self.assertEqual(len(map.view_list), 2)
            self.assertTrue(map.has_view('data'))
            self.assertTrue(map.has_view('base'))
        self.assertTrue(os.path.isfile(file_name))
        with open(file_name, 'rb') as f:
            pass

        with gxmap.Map.new(file_name='test_geosoft',
                             overwrite=True,
                             data_area=(1000, 200, 11000, 5000)) as map:
            file_name = map.file_name
            self.assertEqual(len(map.view_list), 2)
            self.assertTrue(map.has_view('data'))
            self.assertTrue(map.has_view('base'))
        self.assertTrue(os.path.isfile(file_name))
        with open(file_name, 'rb') as f:
            pass

        with gxmap.Map.new(file_name='test_geosoft', overwrite=True) as map:
            file_name = map.file_name
            map.remove_on_close(True)
        self.assertFalse(os.path.isfile(file_name))

        for i in range(3):
            map = gxmap.Map.new(file_name='t{}'.format(i), overwrite=True)
            map.remove_on_close(True)
            map.close()

    def test_map_classes(self):
        self.start()

        with gxmap.Map.new(file_name='test_geosoft', overwrite=True) as map:
            self.assertEqual(map.get_class_name('data'), 'data')
            self.assertEqual(map.get_class_name('base'), 'base')
            self.assertEqual(map.get_class_name('section'), 'section')
            self.assertEqual(map.get_class_name('some_class_name'), 'some_class_name')

            map.set_class_name('base', 'bogus')
            self.assertEqual(map.get_class_name('base'), 'bogus')
            map.set_class_name('data', 'bogus_data')
            #self.assertEqual(map.get_class_name('data'), 'bogus_data')
            map.set_class_name('Section', 'yeah')
            self.assertEqual(map.get_class_name('Section'), 'yeah')
            map.set_class_name('mine', 'boom')
            self.assertEqual(map.get_class_name('mine'), 'boom')

        with gxmap.Map.new(data_area=(0, 0, 100, 80),
                             coordinate_system=gxcs.Coordinate_system("DHDN / Okarito 2000 [geodetic]")) as map:

            self.assertEqual(map.get_class_name('base'), 'base')
            self.assertEqual(map.get_class_name('data'), 'data')

            with gxv.View(map, "copy_data", mode=gxv.WRITE_NEW, copy="data"): pass
            map.set_class_name('data', 'copy_data')
            self.assertEqual(map.get_class_name('data'), 'copy_data')

    def test_current_view(self):
        self.start()

        with gxmap.Map.new() as map:
            self.assertEqual(map.current_data_view, 'data')
            map.current_data_view = 'base'
            self.assertEqual(map.current_data_view, 'base')
            self.assertEqual(map.get_class_name('data'), 'base')
            map.current_data_view = 'data'
            self.assertEqual(map.current_data_view, 'data')
            try:
                map.current_data_view = 'Bogus'
                self.assertTrue(False)
            except gxmap.MapException:
                pass

            map.copy_view('data', 'Bogus')
            map.current_data_view = 'Bogus'
            self.assertEqual(map.current_data_view, 'bogus')
            self.assertRaises(gxmap.MapException, map.copy_view, 'Data', 'bogus')
            self.assertRaises(gxmap.MapException, map.copy_view, 'data', 'bogus')
            map.copy_view('data', 'bogus', overwrite=True)
            self.assertEqual(map.current_data_view, 'bogus')

    def test_media(self):
        self.start()

        def crc_media(map_file, test_number):
            with gxmap.Map.open(map_file) as map:
                with gxv.View(map, "base") as v:
                    with gxg.Draw(v) as g:
                        g.rectangle(v.extent_clip, pen=gxg.Pen(line_thick=0.2, line_color='K'))
                with gxv.View(map, "data") as v:
                    with gxg.Draw(v) as g:
                        g.rectangle(v.extent_clip, pen=gxg.Pen(line_thick=0.2, line_color='R'))
            self.crc_map(map_file,
                         pix_width=256,
                         alt_crc_name='{}_{}'.format(gxsys.func_name(1), test_number))

        test_media_map = os.path.join(gx.gx().temp_folder(), 'test_media')

        test_number = 0
        with gxmap.Map.new(test_media_map + 'scale_800', overwrite=True, scale=800,
                             data_area=(5, 10, 50, 100)) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        with gxmap.Map.new(test_media_map + 'scale_100', overwrite=True, scale=100,
                             data_area=(5, 10, 50, 100)) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        with gxmap.Map.new(test_media_map + 'a4_portrait',
                             overwrite=True,
                             media='A4',
                             layout=gxmap.MAP_PORTRAIT) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        with gxmap.Map.new(test_media_map + 'portrait_a4',
                             overwrite=True,
                             media='a4',
                             fixed_size=True,
                             layout=gxmap.MAP_PORTRAIT) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        with gxmap.Map.new(test_media_map + 'a4_landscape',
                             overwrite=True,
                             media='A4',
                             fixed_size=True,
                             layout=gxmap.MAP_LANDSCAPE) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        with gxmap.Map.new(test_media_map + 'A4_1',
                             overwrite=True, media='A4',
                             fixed_size=True,
                             data_area=(10, 5, 100, 50)) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        with gxmap.Map.new(test_media_map + 'A4_2',
                             overwrite=True, media='A4',
                             fixed_size=True,
                             data_area=(5, 10, 50, 100), layout=gxmap.MAP_LANDSCAPE) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        with gxmap.Map.new(test_media_map + 'A4_3',
                             overwrite=True,
                             media='A4',
                             data_area=(5, 10, 50, 100)) as map:
            file_name = map.file_name
        crc_media(file_name, test_number)
        test_number += 1

        for m in (None, (60, 50), 'unlimited', 'bogus', 'A4', 'A3', 'A2', 'A1', 'A0',
                  'A', 'B', 'C', 'D', 'E'):
            with gxmap.Map.new(media=m) as map: pass

        self.assertRaises(gxmap.MapException,
                          gxmap.Map.new,
                          test_media_map, overwrite=True, media='A4',
                          data_area=(100, 50, 10, 5), layout='landscape')

    def test_multiple_temp_maps(self):
        self.start()

        mapfiles = []
        for i in range(3):
            with gxmap.Map.new() as map:
                mapfiles.append(map.file_name)
                with gxv.View(map, 'data') as v:
                    with gxg.Draw(v) as g:
                        g.rectangle(v.extent_clip)

        for fn in mapfiles:
            self.assertTrue(os.path.isfile(fn))


    def test_north_arrow_0(self):
        self.start()

        with gxmap.Map.new(coordinate_system='ft') as map:
            mapfile = map.file_name

            with gxv.View(map, 'base') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)

            map.north_arrow()

        self.crc_map(mapfile)

    def test_north_arrow_1(self):
        self.start()

        with gxmap.Map.new(coordinate_system='m', data_area=(0,0,20,10), scale=100) as map:
            mapfile = map.file_name

            with gxv.View(map, 'base') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)

            map.north_arrow(location=(2, 0, 3), inclination=-12, declination=74.5,
                            text_def=gxg.Text_def(font='Calibri'))

        self.crc_map(mapfile)


    def test_scale_1(self):
        self.start()

        with gxmap.Map.new(data_area=(350000,7000000,400000,7030000), coordinate_system='ft') as map:
            mapfile = map.file_name
            with gxv.View(map, 'base') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            map.scale_bar()
            map.scale_bar(location=(2, 0, 2), length=10, sections=12)
            map.scale_bar(location=(5, 0, 0), length=8, sections=2, post_scale=True)
            map.scale_bar(location=(3, -3, 1.5), length=4,
                          text_def=gxg.Text_def(height=0.2, italics=True), post_scale=True)

        self.crc_map(mapfile)

    def test_scale_2(self):
        self.start()

        with gxmap.Map.new(data_area=(350000,7000000,400000,7030000), coordinate_system='NAD83 / UTM zone 15N') as map:
            mapfile = map.file_name
            with gxv.View(map, 'base') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            map.scale_bar()
            map.scale_bar(location=(2, 0, 2), length=10, sections=12,
                          pen=gxg.Pen(line_color='R'),
                          text_def=gxg.Text_def(color='B', weight=gxg.FONT_WEIGHT_BOLD))

        self.crc_map(mapfile)

    def test_surround_1(self):
        self.start()

        cs = gxcs.Coordinate_system('NAD83 / UTM zone 15N')
        with gxmap.Map.new(data_area=(350000, 7000000, 400000, 7030000), coordinate_system=cs) as map:
            mapfile = map.file_name
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            map.surround()
        self.crc_map(mapfile)

    def test_surround_2(self):
        self.start()

        cs = gxcs.Coordinate_system('NAD83 / UTM zone 15N')
        with gxmap.Map.new(data_area=(350000, 7000000, 400000, 7030000), coordinate_system=cs) as map:
            mapfile = map.file_name
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            map.surround(gap=0.2, outer_pen=gxg.Pen(line_thick=0.2), inner_pen='bt500')
        self.crc_map(mapfile)

    def test_surround_3(self):
        self.start()

        with gxmap.Map.new(data_area=(350000, 7000000, 400000, 7030000)) as map:
            mapfile = map.file_name
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
            map.surround(gap=0.2,
                         outer_pen='rt500',
                         inner_pen='K16')
        self.crc_map(mapfile)

    def test_annotate_xy_0(self):
        self.start()

        with self._data_map() as map:
            mapfile = map.file_name
            map.annotate_data_xy(x_sep=1500)

        self.crc_map(mapfile)

    def test_annotate_xy_1(self):
        self.start()

        with self._data_map() as map:
            mapfile = map.file_name
            map.annotate_data_xy(x_sep=1500,
                                 grid=gxmap.GRID_DOTTED,
                                 offset=0.5,
                                 text_def=gxg.Text_def(color='R', weight=gxg.FONT_WEIGHT_BOLD))

        self.crc_map(mapfile)

    def test_annotate_xy_2(self):
        self.start()

        with self._data_map() as map:
            mapfile = map.file_name
            map.annotate_data_xy(x_sep=1500,
                                 tick=0.1,
                                 text_def=gxg.Text_def(color='G', weight=gxg.FONT_WEIGHT_ULTRALIGHT),
                                 grid=gxmap.GRID_CROSSES,
                                 grid_pen=gxg.Pen(line_color='b', line_thick=0.015))

        self.crc_map(mapfile)

    def test_annotate_xy_3(self):
        self.start()

        with self._data_map() as map:
            mapfile = map.file_name
            map.annotate_data_xy(x_sep=1500,
                                 tick=0.1,
                                 grid=gxmap.GRID_LINES,
                                 offset=0.2,
                                 edge_pen=gxg.Pen(line_color='k64', line_thick=0.3),
                                 grid_pen=gxg.Pen(line_color='b', line_thick=0.015))

        self.crc_map(mapfile)

    def test_annotate_ll_0(self):
        self.start()

        with self._data_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.file_name
            map.annotate_data_ll()
        self.crc_map(mapfile)

    def test_annotate_ll_1(self):
        self.start()

        with self._data_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.file_name
            map.annotate_data_ll(grid=gxmap.GRID_LINES,
                                 grid_pen=gxg.Pen(line_color='b'),
                                 text_def=gxg.Text_def(color='K127',
                                                       font='cr.gfn',
                                                       weight=gxg.FONT_WEIGHT_BOLD,
                                                       italics=True))
        self.crc_map(mapfile)

    def test_annotate_ll_2(self):
        self.start()
        with self._data_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.file_name
            map.annotate_data_xy()
            map.annotate_data_ll(grid=gxmap.GRID_LINES,
                                  grid_pen=gxg.Pen(line_color='b', line_thick=0.015),
                                  text_def=gxg.Text_def(color='r', height=0.2, italics=True),
                                  top=gxmap.TOP_IN)
        self.crc_map(mapfile)

    def test_annotate_ll_3(self):
        self.start()

        with self._data_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.file_name
            map.annotate_data_xy(tick=0.1, grid=gxmap.GRID_LINES,
                                 text_def=gxg.Text_def(weight=gxg.FONT_WEIGHT_ULTRALIGHT),
                                 grid_pen=gxg.Pen(line_thick=0.01))
            map.annotate_data_ll(grid=gxmap.GRID_LINES,
                                 grid_pen=gxg.Pen(line_color='b', line_thick=0.025),
                                 text_def=gxg.Text_def(height=0.18, italics=True, color='g'))
        self.crc_map(mapfile)

    def test_annotate_ll_4(self):
        self.start()

        with self._data_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.file_name
            map.annotate_data_xy(tick=0.1, grid=gxmap.GRID_LINES,
                                 text_def=gxg.Text_def(weight=gxg.FONT_WEIGHT_BOLD),
                                 top=gxmap.TOP_IN)
            map.annotate_data_ll(grid=gxmap.GRID_LINES,
                                 grid_pen=gxg.Pen(line_color='b', line_thick=0.025),
                                 text_def=gxg.Text_def(height=0.18, italics=True),
                                 top=gxmap.TOP_IN)
        self.crc_map(mapfile)

    def test_annotate_ll_local(self):
        self.start()

        cs = gxcs.Coordinate_system({'type': 'local',
                        'lon_lat': (-96, 45),
                        'datum': 'nad83',
                        'azimuth': -30})
        cs = gxcs.Coordinate_system("NAD27 / UTM zone 15N <425000,6500145,0,0,0,-30>")
        name = os.path.join(gx.gx().temp_folder(), "test")
        with gxmap.Map.new(file_name='mapplot_anoxy_rotated_cs_bug_UTM',
                             overwrite=True,
                             data_area=(0, 0, 5000, 3500),
                             coordinate_system=cs,
                             media="A3",
                             margins=(3,3,4,3)) as map:

            mapfile = map.file_name

            map.scale_bar(location=(2, 0, 2), length=6, sections=5)
            map.surround()
            map.annotate_data_xy(grid=gxmap.GRID_LINES)
            map.annotate_data_ll(grid=gxmap.GRID_LINES,
                                 grid_pen=gxg.Pen(line_color='b', line_thick=0.025),
                                 text_def=gxg.Text_def(height=0.18, italics=True),
                                 top=gxmap.TOP_IN)

            map.surround()

        self.crc_map(mapfile)
        gxmap.delete_files(mapfile)

    def test_view_extents(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.Map.new(testmap, overwrite=True) as gmap:

            gmap.delete_view('data')
            gxv.View(gmap, "my_data_1", map_location=(2, 3), area=(0, 0, 1000, 1500), scale=10000).close()
            gxv.View(gmap, "my_data_2", map_location=(15, 3), area=(0, 0, 1000, 1500), scale=10000).close()
            ex = gmap.extent_data_views()
            self.assertEqual(ex, (2, 3, 25, 18))

            mdf = gmap.mdf()
            self.assertEqual(mdf[0], (36.39513677811551, 39.99513677811551, 3.0, 24.395136778115507, 21.99513677811551, 2.0))
            self.assertEqual(mdf[1], (10000.0, 1.0, 0.0, 0.0))

    def test_metadata(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.Map.new(testmap, overwrite=True) as gmap:

            gmap.delete_view('data')
            gxv.View(gmap, "my_data_1", map_location=(2, 3), area=(0, 0, 1000, 1500), scale=10000).close()
            gxv.View(gmap, "my_data_2", map_location=(15, 3), area=(0, 0, 1000, 1500), scale=10000).close()

            m = gmap.metadata
            gm = m['geosoft']
            self.assertEqual(len(gm), 2)
            self.assertTrue('dataset' in gm)

            newstuff = {'maki': {'a': 1, 'b': (4, 5, 6), 'units': 'nT'}}
            gmap.metadata = newstuff

        with gxmap.Map.open(testmap) as gmap:
            m = gmap.metadata

            gm = m['geosoft']
            self.assertEqual(len(gm), 2)
            self.assertTrue('dataset' in gm)

            maki = m['maki']
            self.assertEqual(maki['b'], ['4', '5', '6'])
            self.assertEqual(maki['units'], 'nT')

    def test_geotiff(self):
        self.start()

        mapname = self._new_data_map()
        with gxmap.Map.open(mapname) as map:
            map.export_geotiff('test_geotiff.tif')
            with gxgrd.Grid.open('test_geotiff.tif(TIF)') as tif:
                tif.delete_files()
                properties = tif.properties()
                self.assertEqual(properties.get('nx'),1376)
                self.assertEqual(properties.get('ny'),1512)
                self.assertEqual(str(properties.get('coordinate_system')),'*unknown')

    def test_figure(self):
        self.start()

        mapfile1 = gxmap.Map.figure((400, -1000, 1400, -200), file_name='test_figure1.map').file_name
        gxmap.crc_map(mapfile1)

        mapfile2 = gxmap.Map.figure((400400, 6000000, 401400, 6000800),
                                    coordinate_system="NAD27 / UTM zone 25N",
                                    title='Test Coordinate System',
                                    features='all', file_name='test_figure2.map').file_name
        gxmap.crc_map(mapfile2)

    def test_from_gxapi(self):
        self.start()
        gxapi_map = gxapi.GXMAP.create('test_from_gxapi.map', gxmap.WRITE_NEW)
        with gxmap.Map.from_gxapi(gxapi_map) as map:
            self.assertEqual('test_from_gxapi', map.name)


if __name__ == '__main__':
    unittest.main()
