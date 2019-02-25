import geosoft.gxapi as gxa
import numpy as np

def gs_from_np(dtype):
    dtype = np.dtype(dtype)
    if dtype == np.byte:
        return gxa.GS_BYTE
    elif dtype == np.ubyte:
        return gxa.GS_UBYTE
    elif dtype == np.int16:
        return gxa.GS_SHORT
    elif dtype == np.uint16:
        return gxa.GS_USHORT
    elif dtype == np.int32:
        return gxa.GS_LONG
    elif dtype == np.uint32:
        return gxa.GS_ULONG
    elif dtype == np.int64:
        return gxa.GS_LONG64
    elif dtype == np.uint64:
        return gxa.GS_ULONG64
    elif dtype == np.float32:
        return gxa.GS_FLOAT
    elif dtype == np.float64:
        return gxa.GS_DOUBLE
    else:
        raise gxa.GXAPIError("Numpy array type does not map to one of the supported GS_TYPES");
