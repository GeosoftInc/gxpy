#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
"""
Geosoft Viewers.

.. note::

    Test example: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/examples/stand-alone/test_viewer.py>`_

"""

import os
import subprocess
import geosoft
import geosoft.gxapi as gxapi

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class ViewerException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.viewer`.

    .. versionadded:: 9.2
    """
    pass


def _get_default_gd_exe():
    s = gxapi.str_ref()
    gxapi.GXSYS.get_directory(gxapi.SYS_DIR_GEOSOFT_BIN, s)
    bin_dir = s.value
    gd_exe = os.path.join(bin_dir, 'omcore.exe')
    if os.path.exists(gd_exe):
        return gd_exe
    gd_exe = os.path.join(bin_dir, 'omtarget.exe')
    if os.path.exists(gd_exe):
        return gd_exe
    gd_exe = os.path.join(bin_dir, 'omedu.exe')
    if os.path.exists(gd_exe):
        return gd_exe
    gd_exe = os.path.join(bin_dir, 'omv.exe')
    if os.path.exists(gd_exe):
        return gd_exe

    return None


def view_document(document_file_name, wait_for_close=True, env=None):
    """
    Open Geosoft Desktop application for viewing a supported Geosoft document type.  These include:
    
    ::
    
        gdb file
        map files
        geosoft_3dv files
        grid files
        voxel files
        vector_voxel files
        VOXI models
        GM-SYS 2d models
        GM-SYS 3d models
    
    :param document_file_name:  document file name, require decorators for grids, e.g. testgrid.grd(GRD).  
                                Supports all documents that can be openned by Geosoft Desktop.
    :param wait_for_close:      wait for process to exit, default `True`
    :param env:                 environment variables to add to os environment variables 

    .. versionadded:: 9.2
   
    """

    gd_exe = _get_default_gd_exe()
    if not gd_exe:
        gxapi.GXSYS.display_message('Geosoft Desktop application not Found',
                                    'Geosoft Desktop, Geosoft Target or a Geosoft viewer must be installed '
                                    'to view a Geosoft document type. Downloads are available from '
                                    'https://my.geosoft.com/downloads.')
    else:
        proc_env = os.environ.copy()
        if env:
            proc_env.update(env)
        proc = subprocess.Popen([gd_exe, '-doc={}'.format(document_file_name)], env=proc_env)
        if wait_for_close:
            proc.communicate()
