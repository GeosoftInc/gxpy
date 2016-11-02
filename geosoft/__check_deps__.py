import sys
import platform

if sys.platform != 'win32':
    raise ImportError("Sorry: The Geosoft GX module does not currently support your platform ('{}')".format(sys.platform))

if sys.maxsize <= 2**32:
    raise ImportError("Sorry: The Geosoft GX module currently only supports 64-bit architecture (yours '{}')".format("-".join(platform.architecture())))

py_ver_major_minor = sys.version_info[:2]
if py_ver_major_minor < (3,4) or py_ver_major_minor > (3,6):
    raise ImportError("Sorry: The Geosoft GX module currently only Python versions 3.4 to 3.6 (yours '{}')".format(sys.version))

try:
    import numpy
except ImportError:
    raise ImportError("Sorry: The Geosoft GX module requires numpy version 1.7 or greater (yours 'not installed').")
else:
    needver = [1, 7, 0]
    havever = list(map(int, numpy.__version__.split('.'))) + [0] * len(needver)
    for a, b in zip(needver, havever):
        if a > b:
            raise ImportError("Sorry: The Geosoft GX module requires numpy version 1.7 or greater (yours '{}')".format(numpy.__version__))
