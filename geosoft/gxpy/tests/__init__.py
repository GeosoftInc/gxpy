import os
import shutil
import glob

import geosoft.gxpy.gx as gx
import geosoft.gxapi as gxapi
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.viewer as gxvwr
import geosoft.gxpy.utility as gxu

global_update_result = False


class TestWithCRC(object):
    def __init__(self):
        self._result_dir = None

    @classmethod
    def setUpClass(cls, test_py_file):
        os.environ['GEOSOFT_TEST_MODE'] = '1'
        os.environ['GEOSOFT_TESTSYSTEM_MODE'] = '1'
        cls.gx = gx.GXpy(log=print, parent_window=-1, max_warnings=8)
        os.chdir(os.path.dirname(os.path.realpath(test_py_file)))
        pass

    @classmethod
    def tearDownClass(cls):
        del cls.gx

    @classmethod
    def _map_to_xml_and_bmp(cls, map_file, xml_file, bmp_file, pix_width):
        m = gxapi.GXMAP.create(map_file, gxmap.WRITE_OLD)
        m.export_all_raster(bmp_file, '',
                            pix_width, 0, gxapi.rDUMMY,
                            gxapi.MAP_EXPORT_BITS_24,
                            gxapi.MAP_EXPORT_METHOD_NONE,
                            'BMP', '')
        crc = gxapi.int_ref()
        m.crc_map(crc, xml_file)
        try:
            os.remove(bmp_file + '.gi')
            os.remove(bmp_file + '.xml')
        except FileNotFoundError:
            pass

    @classmethod
    def report_mismatch_files(cls, result, master):
        if not os.path.exists(result):
            return '{} does not exist\r\n'.format(result)
        if not os.path.exists(master):
            return '{} does not exist\r\n'.format(master)
        if not gxu.crc32_file(result) == gxu.crc32_file(master):
            return '{} and {} differ\r\n'.format(result, master)
        else:
            return ''

    @property
    def result_dir(self):
        # Do something if you want
        return self._result_dir

    @result_dir.setter
    def result_dir(self, value):
        # Do something if you want
        self._result_dir = value
        if self._result_dir and global_update_result and os.path.exists(self._result_dir):
            shutil.rmtree(self._result_dir)

    def crc_map(self, map_file, display=False, pix_width=1024, update_result=False):

        if display:
            if map_file.lower().endswith('.geosoft_3dv'):
                gxvwr.v3d(map_file)
            else:
                gxvwr.map(map_file)

        result_dir = os.path.join(self.result_dir, 'result')
        master_dir = os.path.join(self.result_dir, 'master')
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        if not os.path.exists(master_dir):
            os.makedirs(master_dir)

        file_part = os.path.split(map_file)[1]
        bmp_result_file = os.path.join(result_dir, "{}.bmp".format(file_part))
        xml_result_file = os.path.join(result_dir, "{}.xml".format(file_part))
        TestWithCRC._map_to_xml_and_bmp(map_file, xml_result_file, bmp_result_file, pix_width)

        bmp_master_file = os.path.join(master_dir, "{}.bmp".format(file_part))
        xml_master_file = os.path.join(master_dir, "{}.xml".format(file_part))

        xml_result_part = os.path.join('result', os.path.split(xml_result_file)[1])
        xml_master_part = os.path.join('master', os.path.split(xml_master_file)[1])
        xml_result_files = glob.glob(xml_result_file + '*')
        if update_result or global_update_result:
            shutil.copyfile(bmp_result_file, bmp_master_file)
            for xml_result in xml_result_files:
                if not xml_result.endswith('.catalog.xml'):
                    xml_master = xml_result.replace(xml_result_part, xml_master_part)
                    shutil.copyfile(xml_result, xml_master)
        else:
            report = TestWithCRC.report_mismatch_files(bmp_result_file, bmp_master_file)
            for xml_result in xml_result_files:
                if not xml_result.endswith('.catalog.xml'):
                    xml_master = xml_result.replace(xml_result_part, xml_master_part)
                    report += TestWithCRC.report_mismatch_files(xml_result, xml_master)
            if len(report) > 0:
                self.fail(report)
