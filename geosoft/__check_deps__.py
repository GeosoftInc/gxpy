import sys
from os import environ
import platform

if sys.platform != 'win32':
    raise ImportError("Sorry: The Geosoft GX module does not currently support your platform ('{}')".format(sys.platform))

if sys.maxsize <= 2**32:
    raise ImportError("Sorry: The Geosoft GX module currently only supports 64-bit architecture (yours '{}')".format("-".join(platform.architecture())))

py_ver_major_minor = sys.version_info[:2]
if py_ver_major_minor < (3,4) or py_ver_major_minor > (3,6):
    raise ImportError("Sorry: The Geosoft GX module currently only Python versions 3.4 to 3.6 (yours '{}')".format(sys.version))

def is_arcgispro_py3_env():
    conda_default_env = environ['CONDA_DEFAULT_ENV']
    if conda_default_env:
        return conda_default_env.endswith('arcgispro-py3')
    else:
        return False

numpy_min_ver = [1, 11, 0]
numpy_min_ver_str = '1.11'
if is_arcgispro_py3_env():
    numpy_min_ver = [1, 9, 0]
    numpy_min_ver_str = '1.9'
try:
    import numpy
except ImportError:
    raise ImportError("Sorry: The Geosoft GX module requires numpy version {} or greater (yours 'not installed').".format(numpy_min_ver_str))
else:
    numpy_have_ver = list(map(int, numpy.__version__.split('.'))) + [0] * len(numpy_min_ver)
    for a, b in zip(numpy_min_ver, numpy_have_ver):
        if a > b:
            raise ImportError("Sorry: The Geosoft GX module requires numpy version {} or greater (yours '{}')".format(numpy_min_ver_str, numpy.__version__))
