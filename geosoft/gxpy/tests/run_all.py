#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import multiprocessing
import subprocess
import glob
import timeit
import os
import sys
import inspect

def work(test):
    this_file = os.path.join(os.getcwd(), inspect.getfile(work))
    this_folder = os.path.split(this_file)[0]
    nosetests = os.path.join(os.path.split(sys.executable)[0], 'scripts', 'nosetests')
    return (test, subprocess.call([nosetests, '-s', '-v', test], cwd=this_folder))

_exit_code = 0

def run_all_tests():
    tests = glob.glob('test_*.py')
    pool = multiprocessing.Pool(processes=6)
    return pool.map_async(work, tests).get(999999)

if __name__ == '__main__':
    start_time = timeit.default_timer()
    results = run_all_tests()
    print('======================================================================')
    print('Completed {} test fixtures in {}s'.format(
        len(results),
        round(timeit.default_timer() - start_time, 3))
    )

    failed_tests = [f[0] for f in results if f[1] != 0]
    if failed_tests:
        print('FAILED (fixtures={})'.format(','.join(failed_tests)), file=sys.stderr)
        exit(1)
    else:
        exit(0)

