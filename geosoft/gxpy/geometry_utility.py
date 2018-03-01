"""
Geometry utilities.

.. seealso:: `geosoft.gxpy.geometry`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_geometry_utility.py>`_
    
"""
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import vv as gxvv
from . import geometry as gxgeo

__version__ = geosoft.__version__

SPLINE_LINEAR = gxapi.VVU_SPL_LINEAR  #:
SPLINE_CUBIC = gxapi.VVU_SPL_CUBIC  #:
SPLINE_AKIMA = gxapi.VVU_SPL_AKIMA  #:
SPLINE_NEAREST = gxapi.VVU_SPL_NEAREST  #:


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GeometryUtilityException(geosoft.GXRuntimeError):
    """
    Exceptions from `geosoft.gxpy.geometry_utility`.

    .. versionadded:: 9.4
    """
    pass


def resample(pp, interval, spline=SPLINE_CUBIC, closed=None):
    """
    Return points resampled at a constant separation along the trace of points.

    :param pp:          `geosoft.gxpy.geometry.PPoint` instance, or a 2D numpy array.
    :param interval:    constant sampling interval
    :param spline:      spline method, one of:

        ============== ========================================================
        SPLINE_LINEAR  points will be along linear line segments between points
        SPLINE_CUBIC   use a minimum-curvature smooth spline
        SPLINE_AKIMA   us an Akima spline, which will not over-shoot data
        SPLINE_NEAREST assign the nearest value
        ============== ========================================================

    :param closed:      `True` to close the line. Smooth splines will appear continuous at the join if closed.
                        If not specified and the first and last points are the same, `True` is assumed.

    :return:            `geosoft.gxpy.geometry.PPoint` instance, or a 2D numpy array, matching the type passed.

    .. versionadded:: 9.4
    """

    if interval <= 0:
        raise GeometryUtilityException(_t('Interval must be > 0'))

    if isinstance(pp, gxgeo.PPoint):
        xyz = pp.xyz
    else:
        if not isinstance(pp, np.ndarray):
            pp = np.array(pp, dtype=np.float64)
        if pp.ndim == 1:
            pp = pp.reshape(len(pp), 1)
        if pp.shape[1] >= 3:
            xyz = pp[:, :3]
        else:
            xyz = np.zeros((len(pp), 3), dtype=np.float64)
            xyz[:, :pp.shape[1]] = pp

    if len(xyz) < 2:
        return pp.copy()

    # closed?
    already_closed = tuple(xyz[0]) == tuple(xyz[-1])
    last_point = -1
    if len(xyz) == 2:
        if already_closed:
            return pp.copy()
        if closed is None:
            closed = False
        if spline in (SPLINE_AKIMA, SPLINE_CUBIC):
            spline = SPLINE_LINEAR
        if closed:
            _xyz = np.zeros(len(xyz) + 1)
            _xyz[:-1] = xyz
            _xyz[-1] = xyz[0]
            xyz = _xyz

    else:
        if closed is None:
            closed = already_closed

        if closed:

            # add points to ensure continuously smooth on ends
            if already_closed:
                closed_xyz = np.empty((len(xyz) + 4, 3))
                closed_xyz[-2:] = xyz[1:3]
                closed_xyz[0:2] = xyz[-3:-1]
            else:
                closed_xyz = np.empty((len(xyz) + 5, 3))
                closed_xyz[-3:] = xyz[:3]
                closed_xyz[0:2] = xyz[-2:]
            closed_xyz[2: 2 + len(xyz)] = xyz


            xyz = closed_xyz
            last_point = -3

    # get vvs
    vvx, vvy, vvz = gxvv.vvset_from_np(xyz)

    # calculate distance
    vvd = gxvv.GXvv(dtype=np.float64)
    gxapi.GXVVU.distance_3d(vvx.gxvv, vvy.gxvv, vvz.gxvv, 0., vvd.gxvv)

    # make up a sampling vector
    if closed:
        start = vvd[2][0]
        d = vvd[last_point][0] - start
    else:
        start = 0.
        d = vvd[-1][0]
    nd = int(d / interval) + 1
    if closed:
        nd += 1
    nps = np.arange(nd, dtype=np.float64) * interval + start
    vvs = gxvv.GXvv(nps)

    # spline locations
    vvxd = gxvv.GXvv(dtype=np.float64)
    gxapi.GXVVU.spline2(vvd.gxvv, vvx.gxvv, vvs.gxvv, vvxd.gxvv, spline)
    vvyd = gxvv.GXvv(dtype=np.float64)
    gxapi.GXVVU.spline2(vvd.gxvv, vvy.gxvv, vvs.gxvv, vvyd.gxvv, spline)
    vvzd = gxvv.GXvv(dtype=np.float64)
    gxapi.GXVVU.spline2(vvd.gxvv, vvz.gxvv, vvs.gxvv, vvzd.gxvv, spline)

    xyz = gxvv.np_from_vvset((vvxd, vvyd, vvzd))

    if closed:
        xyz[-1] = xyz[0]
        if tuple(xyz[-1]) == tuple(xyz[-2]):
            xyz = xyz[:-1]

    if isinstance(pp, gxgeo.PPoint):
        return gxgeo.PPoint(xyz, coordinate_system=pp.coordinate_system)
    else:
        return xyz[:, :pp.shape[1]]
