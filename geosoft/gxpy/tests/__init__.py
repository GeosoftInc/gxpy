import os
import shutil
import glob

import geosoft.gxpy.gx as gx
import geosoft.gxapi as gxapi
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.viewer as gxvwr
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gxsys

# set to True to update all results
UPDATE_ALL_RESULTS = True

# set to true to only update the first test.
UPDATE_ONE_TEST = False

# set to True to show viewer for each CRC call
SHOW_TEST_VIEWERS = False


class GXPYTest(object):
    def __init__(self):
        self._result_dir = None

    @classmethod
    def setUpClass(cls, sub_class, test_py_file):
        # These 2 variables ensure consistent test results (rendering, date/times, usernames in lineage etc.)
        # This works for single test or suites run from within IDEs but when the entire suite is run it
        # helps to ensure these environment variables are set prior to starting the Python process
        os.environ['GEOSOFT_TEST_MODE'] = '1'
        os.environ['GEOSOFT_TESTSYSTEM_MODE'] = '1'
        sub_class.gx = gx.GXpy(log=print, parent_window=-1, max_warnings=8)
        sub_class.gx.temp_folder()
        os.chdir(os.path.dirname(os.path.realpath(test_py_file)))
        pass

    @classmethod
    def tearDownClass(cls, sub_class):
        del sub_class.gx

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
        if self._result_dir and (UPDATE_ALL_RESULTS or UPDATE_ONE_TEST) and os.path.exists(self._result_dir):
            shutil.rmtree(self._result_dir)

    def _agnosticize_and_ensure_consistent_line_endings(self, xml_file, replacement_dict):
        with open(xml_file) as f:
            lines = f.read().splitlines()

        with open(xml_file, 'wb') as f:
            for line in lines:
                # TODO Also replace known folder matches e.g. temp_folder with '<temp>' etc.
                for k, v in replacement_dict.items():
                    line = line.replace(k, v)
                f.write('{}\r\n'.format(line).encode('UTF-8'))


    def crc_map(self, map_file, *, pix_width=1024, update_result=False, alt_crc_name=None):
        """ 
        Run Geosoft crc testing protocol on Geosoft maps.
        
        :param pix_width:       pixel width, increase if achieve higher fidelity in the bitmap test
        :param update_result:   True to update the reference test to the current results
        :param alt_crc_name:    test name.  The default is the name of the calling function.  The name
                                must be unique within this test suite, which it will be if there is
                                only one test per test function.  If you have more than one test in a single
                                testing function use this parameter to create unique names.
        """

        global UPDATE_ONE_TEST

        if SHOW_TEST_VIEWERS:
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
        GXPYTest._map_to_xml_and_bmp(map_file, xml_result_file, bmp_result_file, pix_width)

        file_name_part = file_part.split('.')[0]

        replacement_dict = {}
        if alt_crc_name is None:
            alt_crc_name = gxsys.func_name(1)
        replacement_dict[file_name_part] = alt_crc_name

        result_files = glob.glob(xml_result_file + '*')
        for result in result_files:
            self._agnosticize_and_ensure_consistent_line_endings(result, replacement_dict)

        if alt_crc_name:
            alt_file_part = file_part.replace(file_name_part, alt_crc_name)
            alt_bmp_result_file = os.path.join(result_dir, "{}.bmp".format(alt_file_part))
            alt_xml_result_file = os.path.join(result_dir, "{}.xml".format(alt_file_part))

            shutil.move(bmp_result_file, alt_bmp_result_file)

            result_files = glob.glob(xml_result_file + '*')
            for result in result_files:
                result_file_part = os.path.split(result)[1]
                alt_result = os.path.join(result_dir, result_file_part.replace(file_name_part, alt_crc_name))
                shutil.move(result, alt_result)

            bmp_result_file = alt_bmp_result_file
            xml_result_file = alt_xml_result_file
            bmp_master_file = os.path.join(master_dir, "{}.bmp".format(alt_file_part))
            xml_master_file = os.path.join(master_dir, "{}.xml".format(alt_file_part))
        else:
            bmp_master_file = os.path.join(master_dir, "{}.bmp".format(file_part))
            xml_master_file = os.path.join(master_dir, "{}.xml".format(file_part))

        xml_result_part = os.path.join('result', os.path.split(xml_result_file)[1])
        xml_master_part = os.path.join('master', os.path.split(xml_master_file)[1])
        xml_result_files = glob.glob(xml_result_file + '*')
        if update_result or (UPDATE_ALL_RESULTS or UPDATE_ONE_TEST):
            shutil.copyfile(bmp_result_file, bmp_master_file)
            for xml_result in xml_result_files:
                if not xml_result.endswith('.catalog.xml'):
                    xml_master = xml_result.replace(xml_result_part, xml_master_part)
                    shutil.copyfile(xml_result, xml_master)
        else:
            report = GXPYTest.report_mismatch_files(bmp_result_file, bmp_master_file)
            for xml_result in xml_result_files:
                if not xml_result.endswith('.catalog.xml'):
                    xml_master = xml_result.replace(xml_result_part, xml_master_part)
                    report += GXPYTest.report_mismatch_files(xml_result, xml_master)
            if len(report) > 0:
                self.fail(report)

        UPDATE_ONE_TEST = False