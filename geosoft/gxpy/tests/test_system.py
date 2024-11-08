#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
"""
@author: Ian
"""
import unittest
import os
import time
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys

from base import GXPYTest


class Test(GXPYTest):
    @classmethod
    def tf(cls, f):
        return os.path.join(os.path.dirname(cls._test_case_py), f)

    def test_system(self):
        self.start()
        self.assertEqual(gsys.__version__, geosoft.__version__)

    def test_call_location(self):
        self.start()

        f = gsys.call_location()
        p = gsys.call_location(1)
        self.assertIn("test_call_location", f)
        self.assertIn("test_system.py", f)
        self.assertIn("line 28", f)
        self.assertIn("run", p)

    def test_func(self):
        self.start()

        f = gsys.func_name()
        p = gsys.func_name(2) # This may change with Python upgrades if the unittest.case code changes 
        self.assertEqual(f, "test_func")
        self.assertEqual(p, "run")

    def test_statics(self):
        self.start()

        app = gsys.app_name()
        self.assertTrue(len(app) > 0)
        func = gsys.func_name()
        self.assertEqual(func, 'test_statics')

    def test_unzip(self):
        self.start()

        folder, files = gsys.unzip(Test.tf('little.zip'), Test.tf('_test'), checkready=1)
        self.assertEqual(len(files), 3)
        self.assertTrue(os.path.isfile(folder + '\\little.png'))
        self.assertTrue(os.path.isfile(folder + '\\little - Copy.png'))
        self.assertTrue(os.path.isfile(folder + '\\little - Copy (2).png'))
        gsys.remove_dir(folder, tries=0)

    def test_task_range(self):
        self.start()

        nrecords = 200000000
        nfields = 1
        bufsize = 10000000 # this needs to be big enough to properly test the parallel implementation

        data = np.arange(nrecords*nfields*3).reshape(nrecords, nfields, 3)

        def get_record_count():
            return data.shape[0]

        def read_records(i,j):
            return data[i:(i+j), :, :]

        def validate(range_min,range_max):
            self.assertEqual(range_min[0],data[0,0,0])
            self.assertEqual(range_min[1],data[0,0,1])
            self.assertEqual(range_min[2],data[0,0,2])
            self.assertEqual(range_max[0],data[-1,0,0])
            self.assertEqual(range_max[1],data[-1,0,1])
            self.assertEqual(range_max[2],data[-1,0,2])

        def reference_range(): # Roger's reference implementation

            record_count = get_record_count()
            if record_count < 1:
                return

            #first_point = kv.Project.read_records(src_name, 0, 1)
            first_point = read_records(0, 1)
            range_min = [first_point[0][0][0], first_point[0][0][1], first_point[0][0][2]]
            range_max = range_min[:]

            record_offset = 1
            buf_size = min(bufsize, record_count)

            while record_offset < record_count:
                records_to_read = min(buf_size, record_count - record_offset)
                # buf = kv.Project.read_records(src_name, record_offset, records_to_read)
                buf = read_records(record_offset, records_to_read)
                for i in range(records_to_read):
                    # kv.Thread.task_progress(record_offset / record_count * 100)
                    record_offset += 1
                    # if kv.Thread.is_cancelling():
                    #     return
                    range_min[0] = min(buf[i][0][0], range_min[0])
                    range_min[1] = min(buf[i][0][1], range_min[1])
                    range_min[2] = min(buf[i][0][2], range_min[2])
                    range_max[0] = max(buf[i][0][0], range_max[0])
                    range_max[1] = max(buf[i][0][1], range_max[1])
                    range_max[2] = max(buf[i][0][2], range_max[2])

            return range_min, range_max

        def numpy_range(): # Minimum change numpy implementation, only replace inner loop

            record_count = get_record_count()
            if record_count < 1:
                return

            first_point = read_records(0, 1)
            range_min = [first_point[0][0][0], first_point[0][0][1], first_point[0][0][2]]
            range_max = range_min[:]

            record_offset = 1
            buf_size = min(bufsize, record_count)

            while record_offset < record_count:
                records_to_read = min(buf_size, record_count - record_offset)
                buf = read_records(record_offset, records_to_read)
                bx = buf[:,0,0]
                by = buf[:,0,1]
                bz = buf[:,0,2]
                range_min = [min(range_min[0], np.nanmin(bx)),
                             min(range_min[1], np.nanmin(by)),
                             min(range_min[2], np.nanmin(bz))]
                range_max = [max(range_max[0], np.nanmax(bx)),
                             max(range_max[1], np.nanmax(by)),
                             max(range_max[2], np.nanmax(bz))]
                record_offset += buf.shape[0]

            return range_min, range_max

        def numpy_parallel_range(): # parallel implementation

            record_count = get_record_count()
            if record_count < 1:
                return

            first_point = read_records(0, 1)
            range_min = [first_point[0][0][0], first_point[0][0][1], first_point[0][0][2]]
            range_max = range_min[:]

            record_offset = 1
            buf_size = min(bufsize, record_count)

            while record_offset < record_count:
                records_to_read = min(buf_size, record_count - record_offset)
                buf = read_records(record_offset, records_to_read)

                # arrange the problem for three parallel threads
                parallel = [(range_min[0], range_max[0], buf[:,0,0]),
                            (range_min[1], range_max[1], buf[:,0,1]),
                            (range_min[2], range_max[2], buf[:,0,2])]

                # run in parallel
                results = gsys.parallel_map(lambda a: (min(a[0], np.nanmin(a[2])), max(a[1], np.nanmax(a[2]))), parallel)

                # update the ranges from the results, which are in a list of (min,max)
                zip1,zip2 = zip(*results)
                range_min = list(zip1)
                range_max = list(zip2)

                record_offset += buf.shape[0]

            return range_min, range_max

        def time_test(func, reference_time=None):

            start = time.time()
            range_min, range_max = func()
            end = time.time()

            # make sure result is correct
            validate(range_min,range_max)
            elapsed = end-start
            if reference_time is None:
                speed_improvement = 1
            else:
                speed_improvement = reference_time / elapsed

            geosoft.gxpy.gx.gx().log("{}: time: {} seconds, {} times faster than reference".format(func.__name__, elapsed, speed_improvement))
            return elapsed

        #ref = time_test(reference_range)
        ref = 0
        ref = time_test(numpy_range, ref)
        time_test(numpy_parallel_range, ref)

        # testing documented parallel example
        data = [(1+i, 2+i) for i in range(20)]
        geosoft.gxpy.gx.gx().log('parallel:',gsys.parallel_map(lambda ab: ab[0] + ab[1], data))

###############################################################################################
if __name__ == '__main__':
    unittest.main()
