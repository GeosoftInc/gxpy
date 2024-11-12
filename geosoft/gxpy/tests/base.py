#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import os
import shutil
import glob
import unittest
import inspect
import subprocess
import numpy as np

np.seterr(all='raise')

os.environ['GEOSOFT_FORCE_MESA_3D'] = '1'
os.environ['GEOSOFT_TEST_MODE'] = '1'
os.environ['GEOSOFT_TESTSYSTEM_MODE'] = '1'

import geosoft.gxpy.gx as gx
import geosoft.gxapi as gxapi
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.viewer as gxvwr
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gxsys

# set to True to show viewer for each CRC call
SHOW_TEST_VIEWERS = False

_external_result_base_dir = os.environ.get('GEOSOFT_GXPY_DEV_RESULT_DIR', None)
_dev_test_run = os.environ.get('GEOSOFT_GXPY_DEV_TEST_RUN', 0) == '1'
if _dev_test_run:
    SHOW_TEST_VIEWERS = False

import win32gui
import win32con

if win32gui.SystemParametersInfo(win32con.SPI_GETFONTSMOOTHING):
    import atexit

    def restore_font_smoothing():
        win32gui.SystemParametersInfo(win32con.SPI_SETFONTSMOOTHING, True)
    atexit.register(restore_font_smoothing)
    win32gui.SystemParametersInfo(win32con.SPI_SETFONTSMOOTHING, False)

# do not accidentally block automated runs if these variables are set
_prevent_interactive = _dev_test_run or os.environ.get('GEOSOFT_PREVENT_INTERACTIVE', 0) == '1'
if _prevent_interactive:
    SHOW_TEST_VIEWERS = False


# Make root window for UI methods
root_window = None
if SHOW_TEST_VIEWERS:
    from tkinter import Tk, messagebox

    # We import these here to properly initialize common controls
    import win32gui
    import win32con

    root_window = Tk()
    root_window.overrideredirect(1)
    root_window.withdraw()

def _t(s):
    return s

def _verify_no_gx_context():
    loc_gx = None
    try:
        loc_gx = gxapi.GXContext.current()
    except:
        loc_gx = None
        pass
    if loc_gx is not None:
        raise Exception(_t("We have a GXContext but should not!"))


class GXPYTest(unittest.TestCase):
    maxDiff = None
    _test_case_py = None
    _test_case_filename = None
    _result_base_dir = None
    _cls_unique_id_count = 0
    _gx = None

    @classmethod
    def _cls_uuid(cls):
        cls._cls_unique_id_count = cls._cls_unique_id_count + 1
        return 'uuid_{}_{}'.format(cls._test_case_filename, cls._cls_unique_id_count)

    @classmethod
    def setUpGXPYTest(cls, res_stack=6, context_name=__name__, parent_window=0, per_user_key=False):
        _verify_no_gx_context()

        cls._cls_unique_id_count = 0
        cls._test_case_py = os.path.join(os.getcwd(), inspect.getfile(cls))
        cls._test_case_filename = os.path.split(cls._test_case_py)[1]
        if cls._test_case_filename == os.path.split(__file__)[1]:
            raise Exception(_t("GXPYTest base class incorrectly detected as test case!"))

        cur_dir = os.path.dirname(cls._test_case_py)
        cls._result_base_dir = os.path.join(cur_dir, 'results', cls._test_case_filename) if  _external_result_base_dir is None else _external_result_base_dir
        os.makedirs(cls._result_base_dir, exist_ok=True)
        os.chdir(cls._result_base_dir)

        gxu._temp_folder_override = os.path.join(cls._result_base_dir, '__tmp__')
        if os.path.exists(gxu._temp_folder_override):
            shutil.rmtree(gxu._temp_folder_override)
        os.makedirs(gxu._temp_folder_override, exist_ok=True)

        gxu._uuid_callable = cls._cls_uuid

        if not _dev_test_run:
            # This ensures clean global and other settings for consistent test runs
            _, user_dir, _ = gxapi.GXContext.get_key_based_product_dirs(per_user_key=per_user_key)
            if os.path.exists(user_dir):
                shutil.rmtree(user_dir)
            os.makedirs(user_dir, exist_ok=True)

        cls._gx = gx.GXpy(name=context_name, log=print, res_stack=res_stack, max_warnings=12,
                          suppress_progress=True, parent_window=parent_window, per_user_key=per_user_key)

    @classmethod
    def tearDownGXPYTest(cls):
        cls._gx.__del__()
        cls._gx = None

        gxu._temp_folder_override = None
        gxu._uuid_callable = None

        cls._test_case_py = None
        cls._test_case_filename = None
        cls._result_base_dir = None
        cls._cls_unique_id_count = 0

        _verify_no_gx_context()

    @classmethod
    def setUpClass(cls, res_stack=6):
        if cls is GXPYTest:
            raise unittest.SkipTest("Skip GXPYTest tests, it's a base class")
        cls.setUpGXPYTest()

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()

    def _uuid(self):
        self._unique_id_count = self._unique_id_count + 1
        return 'uuid_{}_{}'.format(self._func, self._unique_id_count)

    def start(self):
        self._func = self.id().split('.')[-1]
        gx.gx().log('\n' + self._func)
        self._result_dir = os.path.join(self._result_base_dir, self._func)
        result_run_dir = os.path.join(self._result_dir, 'result')
        if os.path.exists(result_run_dir):
            shutil.rmtree(result_run_dir)

        gxu._uuid_callable = self._uuid
        self._unique_id_count = 0

    @property
    def gx(self):
        return self.__class__._gx

    @property
    def result_dir(self):
        return self._result_dir

    @result_dir.setter
    def result_dir(self, value):
        self._result_dir = value

    @classmethod
    def _remove_time_chunk_from_png(cls, png_file):
        file_length = os.stat(png_file).st_size
        with open(png_file, 'rb') as f:
            bytes = f.read(file_length)
        with open(png_file, 'wb') as f:
            f.write(bytes[:8])

            pos = 8
            while pos < len(bytes):
                buf_length = bytes[pos:pos + 4]
                length = buf_length[0] * 256 * 256 * 256 + \
                         buf_length[1] * 256 * 256 + \
                         buf_length[2] * 256 + buf_length[3]
                buf_type = bytes[pos + 4:pos + 12]
                chunk_type = buf_type.decode('ascii', 'ignore')
                if not (chunk_type.startswith('tIME') or chunk_type.startswith('tEXtdate')):
                    f.write(bytes[pos:pos + length + 12])
                pos = pos + length + 12

    def _map_to_results(self, map_file, xml_file, image_file, map_result, format, pix_width):
        m = gxapi.GXMAP.create(map_file, gxapi.MAP_WRITEOLD)
        m_res = gxapi.GXMAP.create(map_result, gxapi.MAP_WRITENEW)
        m.dup_map(m_res, gxapi.DUPMAP_COPY)
        #m_res.pack_files()
        m_res = None
        os.remove(map_result + '.xml')

        m.export_all_raster(image_file, '',
                            pix_width, 0, gxapi.rDUMMY,
                            gxapi.MAP_EXPORT_BITS_24,
                            gxapi.MAP_EXPORT_METHOD_NONE,
                            format, '')

        if format == 'PNG':
            GXPYTest._remove_time_chunk_from_png(image_file)

        crc = gxapi.int_ref()
        m.crc_map(crc, xml_file)
        m = None
        try:
            os.remove(image_file + '.gi')
            os.remove(image_file + '.xml')
        except FileNotFoundError:
            pass

    @classmethod
    def _agnosticize_and_ensure_consistent_line_endings(cls, xml_file, file_name_part, alt_crc_name):
        with open(xml_file) as f:
            lines = f.read().splitlines()

        with open(xml_file, 'wb') as f:
            for line in lines:
                line = line.replace(file_name_part, alt_crc_name)
                f.write('{}\r\n'.format(line).encode('UTF-8'))

    def crc_map(self, map_file, *, format='PNG', pix_width=2048, alt_crc_name=None):
        """ 
        Run Geosoft crc testing protocol on Geosoft maps.
        
        :param pix_width:       pixel width, increase if achieve higher fidelity in the bitmap test
        :param alt_crc_name:    test name.  The default is the name of the calling function.  The name
                                must be unique within this test suite, which it will be if there is
                                only one test per test function.  If you have more than one test in a single
                                testing function use this parameter to create unique names.
        """

        result_dir = os.path.join(self.result_dir, 'result') if _external_result_base_dir is None else self.result_dir
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        
        master_dir = os.path.join(self.result_dir, 'master')
        if not os.path.exists(master_dir):
            os.makedirs(master_dir)

        file_part = os.path.split(map_file)[1]
        image_result_file = os.path.join(result_dir, "{}.png".format(file_part))
        xml_result_file = os.path.join(result_dir, "{}.xml".format(file_part))

        map_result_file = os.path.join(result_dir, "{}".format(file_part))
        self._map_to_results(map_file, xml_result_file, image_result_file, map_result_file, format, pix_width)

        xml_result_file_catalog = xml_result_file + '.catalog.xml'
        if os.path.exists(xml_result_file_catalog):
            os.remove(xml_result_file_catalog)

        file_name_part = file_part.split('.')[0]

        if alt_crc_name is None:
            alt_crc_name = gxsys.func_name(1)

        result_files = glob.glob(xml_result_file + '*')
        for result in result_files:
            self._agnosticize_and_ensure_consistent_line_endings(result, file_name_part, alt_crc_name)

        if alt_crc_name:
            alt_file_part = file_part.replace(file_name_part, alt_crc_name)
            alt_image_result_file = os.path.join(result_dir, "{}.png".format(alt_file_part))
            alt_xml_result_file = os.path.join(result_dir, "{}.xml".format(alt_file_part))
            alt_map_result_file = os.path.join(result_dir, "{}".format(alt_file_part))

            shutil.move(image_result_file, alt_image_result_file)
            shutil.move(map_result_file, alt_map_result_file)

            result_files = glob.glob(xml_result_file + '*')
            for result in result_files:
                result_file_part = os.path.split(result)[1]
                alt_result = os.path.join(result_dir, result_file_part.replace(file_name_part, alt_crc_name))
                shutil.move(result, alt_result)

            image_result_file = alt_image_result_file
            map_result_file = alt_map_result_file
            xml_result_file = alt_xml_result_file
            image_master_file = os.path.join(master_dir, "{}.png".format(alt_file_part))
            map_master_file = os.path.join(master_dir, "{}".format(alt_file_part))
            xml_master_file = os.path.join(master_dir, "{}.xml".format(alt_file_part))
        else:
            image_master_file = os.path.join(master_dir, "{}.png".format(file_part))
            map_master_file = os.path.join(master_dir, "{}".format(file_part))
            xml_master_file = os.path.join(master_dir, "{}.xml".format(file_part))

        if _external_result_base_dir is not None:
            return

        xml_result_part = os.path.join('result', os.path.split(xml_result_file)[1])
        xml_master_part = os.path.join('master', os.path.split(xml_master_file)[1])
        xml_result_files = glob.glob(map_result_file + '*')
        xml_master_files = glob.glob(map_master_file + '*')

        if SHOW_TEST_VIEWERS:
            gxvwr.view_document(map_file, env={'GEOSOFT_FORCE_MESA_3D': '0'})

    @classmethod
    def pause(cls):
        if not _prevent_interactive:
            print("\n\nHit Return key to continue...")
            input()

    def assertSpatialRefWKT(self, expected_wkt, spatial_ref):
        wkt_actual = spatial_ref.exportToString() if spatial_ref is not None else "[*unknown]"

        # strip precision strings
        expected_wkt = expected_wkt[:expected_wkt.rindex(']') + 1]
        wkt_actual = wkt_actual[:wkt_actual.rindex(']')+1]
        self.assertEqual(expected_wkt, wkt_actual)

    def npAssertAlmostEqual(self, expected, actual, decimal=7, err_msg='', verbose=True):
        np.testing.assert_almost_equal(actual, expected, decimal, err_msg, verbose)

    def npAssertEqual(self, expected, actual, err_msg='', verbose=True):
        np.testing.assert_equal(actual, expected, err_msg, verbose)

