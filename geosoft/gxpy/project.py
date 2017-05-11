"""
Geosoft desktop project interface, which provides access to an active and open Geosoft desktop project.

:Classes:

    ======================== =====================
    :class:`Geosoft_project` the geosoft project
    ======================== =====================

.. seealso:: :mod:`geosoft.gxapi.GXPROJ`, :mod:`geosoft.gxapi.GXEDB`, :mod:`geosoft.gxapi.GXEMAP`

.. note::

    Test example:     
    `geosoft project tests <https://github.com/GeosoftInc/gxpy/blob/master/examples/om-extensions/test_project.py>`_

"""
import os
import geosoft
import geosoft.gxapi as gxapi
from .utility import dict_from_lst
from . import vv as gxvv

__version__ = geosoft.__version__


def _t(s):
    return s

DOC_TYPE_DATABASE = "Database"
DOC_TYPE_GRID = "Grid"
DOC_TYPE_MAP = "Map"
DOC_TYPE_3DV = "3DView"
DOC_TYPE_VOXEL = "Voxel"
DOC_TYPE_VOXI = "VoxelInversion"
DOC_TYPE_MXD = "MXD"
DOC_TYPE_GMS3D = "GMS3D"
DOC_TYPE_GMS2D = "GMS2D"
DOC_TYPE_ALL = "All"

class ProjectException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.project`.

    .. versionadded:: 9.1
    """
    pass


def running_script():
    """
    :returns: 1 if running from a script, 0 if running interactively.

    .. versionadded:: 9.1

    """

    return not gxapi.GXSYS.interactive()

class Geosoft_project(object):
    """
    Use this class to interact with an open Geosoft project. This singleton class is available only from an 
    extension running from an open Geosoft project.  
    
    """

    def _list_open_docs(self, dtype):
        with gxvv.GXvv(None, 'U2048') as docvv:
            gxapi.GXPROJ.list_loaded_documents(docvv.gxvv, dtype)
            return docvv.list()

    def _list_project_docs(self, dtype):
        with gxvv.GXvv(None, 'U2048') as docvv:
            gxapi.GXPROJ.list_documents(docvv.gxvv, dtype)
            return docvv.list()

    def _current_doc(self, dtype):
        s = gxapi.str_ref()
        gxapi.GXPROJ.current_document_of_type(s, dtype)
        return s.value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self):

        s = gxapi.str_ref()
        gxapi.GXPROJ.get_name(s)
        self.project_file = os.path.normpath(s.value)
        self.name = os.path.basename(self.project_file).split('.')[0]

    @property
    def project_databases(self):
        """list of databases in the project"""
        return self._list_project_docs(DOC_TYPE_DATABASE)

    @property
    def project_grids(self):
        """list of grids in the project"""
        return self._list_project_docs(DOC_TYPE_GRID)

    @property
    def project_maps(self):
        """list of maps in the project"""
        return self._list_project_docs(DOC_TYPE_MAP)

    @property
    def project_3dv(self):
        """list of geosoft_3dv (3D views) in the project"""
        return self._list_project_docs(DOC_TYPE_3DV)

    @property
    def project_voxels(self):
        """list of voxels/voxettes in the project"""
        return self._list_project_docs(DOC_TYPE_VOXEL)

    @property
    def project_voxi_models(self):
        """list of VOXI models in the project"""
        return self._list_project_docs(DOC_TYPE_VOXI)

    @property
    def project_gmsys_3d(self):
        """list of GM-SYS 3D models in the project"""
        return self._list_project_docs(DOC_TYPE_GMS3D)

    @property
    def project_gmsys_2d(self):
        """list of GM-SYS 2D models in the project"""
        return self._list_project_docs(DOC_TYPE_GMS2D)

    @property
    def open_databases(self):
        """list of databases open as a database document"""
        return self._list_open_docs(DOC_TYPE_DATABASE)

    @property
    def open_grids(self):
        """list of grids open as a grid document"""
        return self._list_open_docs(DOC_TYPE_GRID)

    @property
    def open_maps(self):
        """list of maps open as a map document"""
        return self._list_open_docs(DOC_TYPE_MAP)

    @property
    def open_3dv(self):
        """list of geosoft_3dv (3d views) open in a 3D viewer"""
        return self._list_open_docs(DOC_TYPE_3DV)

    @property
    def open_voxels(self):
        """list of voxels/voxettes open as a document"""
        return self._list_open_docs(DOC_TYPE_VOXEL)

    @property
    def open_voxi_models(self):
        """list of VOXI models open as a document"""
        return self._list_open_docs(DOC_TYPE_VOXI)

    @property
    def open_gmsys_3d(self):
        """list of GM-SYS 3D models open as a document"""
        return self._list_open_docs(DOC_TYPE_GMS3D)

    @property
    def open_gmsys_2d(self):
        """list of GM-SYS 2D models open as a document"""
        return self._list_open_docs(DOC_TYPE_GMS2D)

    @property
    def current_database(self):
        """the open database that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_DATABASE)

    @property
    def current_grid(self):
        """the open grid that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_GRID)

    @property
    def current_map(self):
        """the open map that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_MAP)

    @property
    def current_3dv(self):
        """the open geosoft_3dv that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_3DV)

    @property
    def current_voxel(self):
        """the open voxel that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_VOXEL)

    @property
    def current_voxi(self):
        """the open VOXI model that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_VOXI)

    @property
    def current_gmsys_3d(self):
        """the open GM-SYS 3D model that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_GMS3D)

    @property
    def current_gmsys_2d(self):
        """the open GM-SYS 2D model that has current (or most recent) focus"""
        return self._current_doc(DOC_TYPE_GMS2D)

    @property
    def menus(self):
        """
        Oasis montaj menu information: (default_menus, loaded_menus, user_menus)
        """

        def_menus = gxapi.GXLST.create(512)
        loaded_menus = gxapi.GXLST.create(512)
        user_menus = gxapi.GXLST.create(512)
        gxapi.GXSYS.get_loaded_menus(def_menus, loaded_menus, user_menus)

        return list(dict_from_lst(def_menus).keys()), \
               list(dict_from_lst(loaded_menus).keys()), \
               list(dict_from_lst(user_menus).keys())

    def current_db_state(self):
        """
        Return the state of the current database.
        
        :returns: dict of the current database state, {} of there is no current database.
        
            =================== ========================================================
            'disp_chan_list'    list of displayed channels
            'selection'         current selection as (line, channel, start_fid, end_fid)
            =================== ========================================================
            
        .. versionadded:: 9.2
        """

        sdb = {}
        if self.current_database:

            glst = gxapi.GXLST.create(4096)

            edb = gxapi.GXEDB.current_no_activate()
            n = edb.disp_chan_lst(glst)
            if n > 0:
                sdb['disp_chan_list'] = list(dict_from_lst(glst).keys())
            else:
                sdb['disp_chan_list'] = []

            s = gxapi.str_ref()
            sch = gxapi.str_ref()
            sln = gxapi.str_ref()
            sfd = gxapi.str_ref()
            edb.get_current_selection(s, sch, sln, sfd)

            if sch.value == '[All]':
                sch.value = '*'
            if sln.value == '[All]':
                sln.value = '*'
            if sfd.value == '[All]':
                fd = ('*', '*')
            elif sfd.value == "[None]":
                fd = ('', '')
            else:
                fd = sfd.value.split(' to ')
                fd = (fd[0], fd[1])
            sdb['selection'] = (sln.value, sch.value, fd[0], fd[1])

        return sdb

    def current_map_state(self):
        """
        Return the state of the current map.
        
        :returns: dict of the current map state, {} if no current map.
            
            =============== =========================================================
            'current_view'  name of the current view
            'display_area'  (min_x, min_y, max_x, max_y) in units of the current view
            '3d_view_name'  if a 3D view, name of the view
            'point'         (x, y) of the current selection point
            'cursor'        (x, y) of the current cursor location
            =============== =========================================================
        
        .. versionadded:: 9.2
        """

        smap = {}
        if self.current_map:

            fx = gxapi.float_ref()
            fy = gxapi.float_ref()
            fx2 = gxapi.float_ref()
            fy2 = gxapi.float_ref()
            s = gxapi.str_ref()

            smap = {}
            emap = gxapi.GXEMAP.current_no_activate()

            emap.get_current_view(s)
            smap['current_view'] = s.value

            emap.get_display_area(fx, fy, fx2, fy2)
            smap['display_area'] = (fx.value, fy.value, fx2.value, fy2.value)

            if emap.is_3d_view():

                emap.get_3d_view_name(s)
                smap['3d_view'] = s.value

            else:
                # 2D


                emap.get_cur_point(fx, fy)
                smap["point"] = (fx.value, fy.value, None)
                emap.get_cursor(fx, fy)
                smap["cursor"] = (fx.value, fy.value, None)

            return smap


def user_message(title, message):
    """
    Display a message to the user
    
    :param title:   message box title
    :param message: message

    .. versionadded:: 9.2

    """
    gxapi.GXSYS.display_message(title, message)


def _user_input_gx(kind):
    """Resolve and run the user_input GX"""
    gxapi.GXSYS.set_string("USER_INPUT", "TYPE", str(kind))
    dir = os.path.split(__file__)[0]
    user_input = os.path.join(os.path.join(dir, 'user_input'), 'user_input.gx')
    ret = gxapi.GXSYS.run_gx(user_input)
    if ret == -1:
        gxapi.GXSYS.cancel()
    return ret


def pause(title='Pause...', cancel=False):
    """
    Display a pause dialog, wait for user to press continue or cancel
    
    :param title:   The pause dialog title, default is "Pause..."
    :param cancel:  If True, show a cancel button
    :raises:        :py:ex:GXCancel if the user cancels the dialog

    .. versionadded:: 9.2

    """

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        if not cancel:
            _user_input_gx(9)
        else:
            _user_input_gx(10)
    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)


def get_user_input(title="Input required...", prompt='?', kind='string', default='', items='', filemask=''):
    """
    Display a dialog prompt on the Geosoft Desktop and wait for user input.
    This method depends on `user_input.gx <https://github.com/GeosoftInc/gxpy/tree/master/geosoft/gxpy/user_input>`_
    and can only be used from an extension running inside a Geosoft Desktop application.

    :param title:       dialog box title.  A description can be added as a second-line using a line-break.
                        example: "Your title/nDescriptive help"
    :param prompt:      prompt string to
    :param kind:        kind of response required: 'string', 'int', 'float', 'file', 'colour' or 'list'
    :param items:       comma-separated string or list/tupple of items for a list
    :param default:     default value.  For multifile can be a string ('|' delimiter) or list/tupple.
    :param filemask:    File type mask '.dat', '*.dat,*.grd', '\*\*,*.grd' for multiple files
                        Comma delimited, or a list/tupple
    :returns:       user response
    :raise:         :py:ex:GXCancel if the user cancels the dialog

    .. versionadded:: 9.1

    """

    gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
    try:
        # what kind of dialog
        if kind == 'color':
            kind = 'colour'
        kind_list = {'string':  0,
                     'float':   1,
                     'int':     2,
                     'list':    3,
                     'colour':  4,
                     'file':    5,
                     'newfile': 6,
                     'oldfile': 7}
        kind = kind_list[kind]

        gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
        gxapi.GXSYS.set_string("USER_INPUT", "PROMPT", str(prompt))

        # clean up filemask
        if not isinstance(filemask, str):
            if len(filemask) > 0:
                filemask = ';'.join(filemask)
            else:
                filemask = ''
        filemask = filemask.replace(',', ';')
        if filemask == '**':
            filemask = '**;*.*'
        gxapi.GXSYS.set_string("USER_INPUT", "FILEMASK", filemask)

        # make a list out of the items.
        if len(items) > 0:
            if type(items) is dict:
                items = [(k) for k in items.keys()]
            elif isinstance(items, str):
                items = items.split(',')
            gxapi.GXSYS.set_string("USER_INPUT", "LIST", ",".join(items))

            # make sure default is in the list
            if default not in items:
                if len(items) > 0:
                    default = items[0]

        # resolve default string
        if kind == kind_list['file']:
            if isinstance(default, str):
                default = default.replace(',', '|').replace(';', '|')
            else:
                if len(default) > 0:
                    default = '|'.join(default)
                else:
                    default = ''
        gxapi.GXSYS.set_string("USER_INPUT", "RESPONSE", str(default))

        # show the dialog
        ret = _user_input_gx(kind)

        if ret == 0:

            strr = gxapi.str_ref()
            gxapi.GXSYS.gt_string("USER_INPUT", "RESPONSE", strr)
            if kind == kind_list['int']:
                return int(strr.value)
            if kind == kind_list['float']:
                return float(strr.value)
            if kind == kind_list['file'] and filemask[:2] == '**':
                return strr.value.split('|')
            return strr.value

        raise ProjectException(_t('GX Error ({})').format(ret))

    finally:
        gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)