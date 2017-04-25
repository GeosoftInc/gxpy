import os
import shutil
import glob
import unittest
import inspect
import subprocess
from tkinter import Tk, messagebox

os.environ['GEOSOFT_TEST_MODE'] = '1'
os.environ['GEOSOFT_TESTSYSTEM_MODE'] = '1'

import geosoft.gxpy.gx as gx
import geosoft.gxapi as gxapi
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.viewer as gxvwr
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gxsys

# Set the following to True to enable interactive updating of results.
# To incorporate a diff tool the GXPY_DIFF_TOOL environment
# variable should be defined.
UPDATE_RESULTS = False

# set to True to show viewer for each CRC call
SHOW_TEST_VIEWERS = False


# Make root window for UI methods
root_window = None
if UPDATE_RESULTS:
    root_window = Tk()
    root_window.overrideredirect(1)
    root_window.withdraw()

def _verify_no_gx_context():
    loc_gx = None
    try:
        loc_gx = gxapi.GXContext.current()
    except:
        loc_gx = None
        pass
    if loc_gx is not None:
        raise Exception("We have a GXContext but should not!")


class GXPYTest(unittest.TestCase):
    _multiprocess_shared_ = True
    _gx = None

    @classmethod
    def setUpGXPYTest(cls, res_stack=6):

        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        _verify_no_gx_context()
        cls._gx = gx.GXpy(log=print, res_stack=res_stack, max_warnings=8)

    @classmethod
    def tearDownGXPYTest(cls):
        if cls._gx:
            cls._gx._close()
        cls._gx = None
        _verify_no_gx_context()

    @classmethod
    def setUpClass(cls, res_stack=6):
        if cls is GXPYTest:
            raise unittest.SkipTest("Skip GXPYTest tests, it's a base class")
        cls.setUpGXPYTest()

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()

    def start(self):
        file = os.path.split(inspect.getfile(self.__class__))[1]
        func = self.id().split('.')[-1]
        self._result_dir = os.path.join('results', file, func)
        result_run_dir = os.path.join(self._result_dir, 'result')
        if os.path.exists(result_run_dir):
            shutil.rmtree(result_run_dir)

        self.gx.log("*** {} > {}".format(file, func))

    @property
    def gx(self):
        return self.__class__._gx

    @property
    def result_dir(self):
        # Do something if you want
        return self._result_dir

    @result_dir.setter
    def result_dir(self, value):
        # Do something if you want
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
        m = gxapi.GXMAP.create(map_file, gxmap.WRITE_OLD)
        m_res = gxapi.GXMAP.create(map_result, gxmap.WRITE_NEW)
        m.dup_map(m_res, gxapi.DUPMAP_COPY)
        m_res.pack_files()
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
    def _report_mismatch_files(cls, result, master):
        if not os.path.exists(result):
            return '{} does not exist\r\n'.format(result)
        if not os.path.exists(master):
            return '{} does not exist\r\n'.format(master)
        if not gxu.crc32_file(result) == gxu.crc32_file(master):
            return '{} and {} differ\r\n'.format(result, master)
        else:
            return ''

    @classmethod
    def _report_master_files_not_in_results(cls, xml_master_files, xml_result_files):
        report = ''
        xml_result_file_names = [os.path.split(f)[1] for f in xml_result_files]
        not_in_results = [f for f in xml_master_files if os.path.split(f)[1] not in xml_result_file_names]
        for f in not_in_results:
            report += '{} no longer exists in result dir\r\n'.format(f)
        return report

    @classmethod
    def _agnosticize_and_ensure_consistent_line_endings(cls, xml_file, replacement_dict):
        with open(xml_file) as f:
            lines = f.read().splitlines()

        with open(xml_file, 'wb') as f:
            for line in lines:
                # TODO Also replace known folder matches e.g. temp_folder with '<temp>' etc.
                for k, v in replacement_dict.items():
                    line = line.replace(k, v)
                f.write('{}\r\n'.format(line).encode('UTF-8'))

    def crc_map(self, map_file, *, format='PNG', pix_width=2048, update_results=False, alt_crc_name=None):
        """ 
        Run Geosoft crc testing protocol on Geosoft maps.
        
        :param pix_width:       pixel width, increase if achieve higher fidelity in the bitmap test
        :param update_results:  True to interactively update failing results 
        :param alt_crc_name:    test name.  The default is the name of the calling function.  The name
                                must be unique within this test suite, which it will be if there is
                                only one test per test function.  If you have more than one test in a single
                                testing function use this parameter to create unique names.
        """

        result_dir = os.path.join(self.result_dir, 'result')
        master_dir = os.path.join(self.result_dir, 'master')
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
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

        replacement_dict = {}
        if alt_crc_name is None:
            alt_crc_name = gxsys.func_name(1)
        replacement_dict[file_name_part] = alt_crc_name

        result_files = glob.glob(xml_result_file + '*')
        for result in result_files:
            self._agnosticize_and_ensure_consistent_line_endings(result, replacement_dict)

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

        xml_result_part = os.path.join('result', os.path.split(xml_result_file)[1])
        xml_master_part = os.path.join('master', os.path.split(xml_master_file)[1])
        xml_result_files = glob.glob(map_result_file + '*')
        xml_master_files = glob.glob(map_master_file + '*')

        report = self._report_mismatch_files(image_result_file, image_master_file)
        report += self._report_master_files_not_in_results(xml_master_files, xml_result_files)

        for xml_result in xml_result_files:
            xml_master = xml_result.replace(xml_result_part, xml_master_part)
            report += self._report_mismatch_files(xml_result, xml_master)

        if SHOW_TEST_VIEWERS:
            gxvwr.view_document(map_file)

        if len(report) > 0:
            if UPDATE_RESULTS or update_results:
                diff_tool = os.environ.get('GXPY_DIFF_TOOL', None)
                if diff_tool is not None:
                    update = messagebox.askyesnocancel('Test differences found ({})'.format(self.id()),
                                                       'The following files are different\n\n{}\n\n'
                                                       'Press Yes to update master result.\n'
                                                       'Press No to launch launch diff tool.\n'
                                                       'Press Cancel to ignore and continue.'.format(report))
                else:
                    update = True if messagebox.askokcancel(
                        'Test differences found ({})'.format(self.id()),
                        'The following files are different\n\n{}\n\n'
                        'Press Ok to update master result.\n'
                        'Press Cancel to ignore and continue.\n\n'
                        'Set GXPY_DIFF_TOOL environment variable to get option\n'
                        'to view differences in a diff tool.'.format(report)) else None

                if update is None:
                    self.fail(report)

                if update:
                    for xml_result in xml_result_files:
                        xml_master = xml_result.replace(os.path.splitext(xml_result_part)[0],
                                                        os.path.splitext(xml_master_part)[0])
                        shutil.copyfile(xml_result, xml_master)
                else:
                    subprocess.run([diff_tool, result_dir, master_dir])

            else:
                self.fail(report)
