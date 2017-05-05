import multiprocessing
import subprocess
import glob
import timeit

def work(test):
    return (test, subprocess.call(['nosetests', '-v', test]))

_exit_code = 0

def run_all_tests():
    tests = glob.glob('test_*.py')
    pool = multiprocessing.Pool(processes=6)
    print(pool.map(work, tests))
    return 0

if __name__ == '__main__':
    start_time = timeit.default_timer()
    exit_code = run_all_tests()
    print(timeit.default_timer() - start_time)
    exit(exit_code)

