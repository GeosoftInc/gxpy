#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
"""
Geosoft system functions.

.. note::

    Regression tests provide usage examples: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_system.py>`_

"""
import time
import inspect
import os
import gc
import shutil
import zipfile
import threading
import sys
from itertools import count
import geosoft

__version__ = geosoft.__version__


def translate(s):
    """ Translate string to user language."""
    return s


def _t(s):
    return translate(s)


def _logit(fn, *args, **kw):
    """function console printing decorator"""

    def logger(*args, **kw):
        ret = fn(*args, **kw)
        print('{} called with args({}), kwargs({}); returns({})'.format(fn.__name__, args, kw, ret))
        return ret

    return logger


def app_name():
    """
    Returns application script name.

    .. versionadded:: 9.1

    """
    return os.path.normpath(sys.argv[0])


def func_name(stack=0):
    """
    Returns function name.

    :param stack:   depth into the calling stack, 0 (default) is this function, 1 is parent, etc.
    :returns:       function name, None if too deep into the stack

    .. versionchanged:: 9.2 added stack
    .. versionadded:: 9.1

    """
    try:
        func = inspect.stack()[stack+1][3]
        return func
    except:
        return None

def call_location(stack=0):
    """
    Returns function call location including file and line number as a string

    :param stack:   depth into the calling stack, 0 (default) is this function, 1 is parent, etc.
    :returns:       string formatted as '<file>, line XX in <function>', empty string if too deep into the stack

    .. versionadded:: 9.2

    """
    try:
        stack_location = inspect.stack()[stack+1]
        file, line, func = stack_location[1:4]
        return '{}, line {} in function {}.'.format(file, line, func)
    except:
        return ''

def _parallel_foreach(f, l, threads=3, return_=False):
    """
    Apply f to each element of l, in parallel, called by parallel_map().
    From: http://wiki.scipy.org/Cookbook/Multithreading
    """

    if threads > 1:
        iteratorlock = threading.Lock()
        exceptions = []
        if return_:
            n = 0
            d = {}
            i = zip(count(), l.__iter__())
        else:
            i = l.__iter__()

        def runall():
            while True:
                iteratorlock.acquire()
                try:
                    try:
                        if exceptions:
                            return
                        v = next(i)
                    finally:
                        iteratorlock.release()
                except StopIteration:
                    return
                try:
                    if return_:
                        n, x = v
                        d[n] = f(x)
                    else:
                        f(v)
                except:
                    e = sys.exc_info()
                    iteratorlock.acquire()
                    try:
                        exceptions.append(e)
                    finally:
                        iteratorlock.release()

        threadlist = [threading.Thread(target=runall) for j in range(threads)]
        for t in threadlist:
            t.start()
        for t in threadlist:
            t.join()
        if exceptions:
            a, b, c = exceptions[0]
            raise (a, b, c)
        if return_:
            r = sorted(d.items())
            return [v for (n, v) in r]
    else:
        if return_:
            return [f(v) for v in l]
        else:
            for v in l:
                f(v)
            return


def parallel_map(f, l, threads=None):
    """
    A parallel equivalent of the map() built-in Python function (it supports only one iterable argument though).

    :param f:       function to run in parallel f(). Must be thread-safe, of course.
    :param l:       iterable list of arguments to pass to each thread.  Use tuples for multiple arguments.
    :param threads: number of threads to use, default is number of cores on computer

    :returns:       list of results from each call to f(), in order of iterable l.

    :example:

    .. code::

        import gxpy.system as gsys

        def func(ab):
            '''
            :param ab:  tuple (a,b)
            :returns:   a+b
            '''
            return ab[0] + ab[1]

        # create list of 20 argument sets to calculate in parallel
        data = [(1+i, 2+i) for i in range(20)]

        # print results of running function in parallel
        print(gsys.parallel_map(func, data))
        # prints: [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]

        # same thing using a lambda function
        print(gsys.parallel_map(lambda ab: ab[0] + ab[1], data))

    .. versionadded:: 9.1

    """
    if threads is None:
        threads = os.cpu_count()
    return _parallel_foreach(f, l, threads=threads, return_=True)


#############
# classes

class GXSysException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.system`.

    .. versionadded:: 9.1
    """
    pass


def wait_on_file(fileName, wait=100, retries=10):
    """
    Working with large files on systems that cache the file can cause a situation
    where the file is not yet completely written out before an attempt is made to open
    a file that has just been closed.

    Call this function to wait for the file to be available.  Best to do this right after
    you know that you may have written out a large file, or in a try/except around a file
    open.

    :param fileName:
    :wait:              time in milliseconds to wait between retries
    :retries:           maximum number of retries
    :raises:            GX_SysException if fail to get read access to the file.

    .. versionadded:: 9.1

    """

    tries = 0
    while True:
        if os.access(fileName, os.W_OK):
            return
        if tries >= retries:
            raise GXSysException(_t('Unable to access {}').format(fileName))
        tries += 1
        time.sleep(wait / 1000.0)


def _unzip(zip_file_name, folder):
    with zipfile.ZipFile(zip_file_name) as zf:
        zf.extractall(folder)
        files = zf.namelist()
    return files


def unzip(zip_file_name, folder=None, report=None, checkready=25):
    """
    Decompress and write the content of a zip file to a folder.

    :param zip_file_name:   zip file name, must have extension
    :param folder:          folder to write results, create it it does not exist
    :param report:          ignored
    :param checkready:      time in 1/10 second to check completion of each file, default 25
    :returns:               (folder that contains unzipped files, list of files)

    .. versionadded:: 9.1

    """

    # get full path
    zip_file_name = os.path.abspath(zip_file_name)

    # if no folder, determine based on zip file name
    if folder is None:
        folder = os.path.splitext(zip_file_name)[0]

    # create a folder
    if not os.path.exists(folder):
        os.makedirs(folder)

    files = None
    try:
        files = _unzip(zip_file_name, folder)

    except:
        raise GXSysException(_t('Cannot process zip file {}').format(zip_file_name))

    finally:

        # check that files are ready for access
        if files and checkready > 0:
            for n in files:
                wait_on_file(os.path.join(folder, n), wait=100, retries=int(checkready * 100))

    return folder, files


def remove_dir(directory, wait=200, tries=10):
    """
    Robust directory removal, with timed retries to allow for OS timing lags.  If you need to use this
    you may have a coding error in which you are not properly releasing a resource.

    :param directory:   directory name, must be a directory
    :param wait:        wait between retries in milliseconds
    :param tries:       number of times to retry

    .. versionadded:: 9.1
    """

    if os.path.isdir(directory):
        t = 0
        while True:
            try:
                shutil.rmtree(directory)
                return
            except:
                t += 1
                if t >= tries:
                    raise
                time.sleep(wait / 1000.0)
