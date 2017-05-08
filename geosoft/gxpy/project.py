"""
Geosoft project.

.. note::

    Test example: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/examples/om-extensions/test_project.py>`_

"""
import os
import geosoft
import geosoft.gxapi as gxapi
from .utility import dict_from_lst, dummy_none
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
    Exceptions from this module.

    .. versionadded:: 9.1
    """
    pass


def running_script():
    """
    :return: 1 if running from a script, 0 if running interactively.

    .. versionadded:: 9.1

    """

    return not gxapi.GXSYS.interactive()

class Geosoft_project:

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

    def __init__(self):

        s = gxapi.str_ref()
        gxapi.GXPROJ.get_name(s)
        self.project_file = os.path.normpath(s.value)
        self.name = os.path.basename(self.project_file).split('.')[0]

    @property
    def project_databases(self):
        return self._list_project_docs(DOC_TYPE_DATABASE)

    @property
    def project_grids(self):
        return self._list_project_docs(DOC_TYPE_GRID)

    @property
    def project_maps(self):
        return self._list_project_docs(DOC_TYPE_MAP)

    @property
    def project_3dv(self):
        return self._list_project_docs(DOC_TYPE_3DV)

    @property
    def project_voxels(self):
        return self._list_project_docs(DOC_TYPE_VOXEL)

    @property
    def project_voxi_models(self):
        return self._list_project_docs(DOC_TYPE_VOXI)

    @property
    def project_gmsys_3d(self):
        return self._list_project_docs(DOC_TYPE_GMS3D)

    @property
    def project_gmsys_2d(self):
        return self._list_project_docs(DOC_TYPE_GMS2D)

    @property
    def open_databases(self):
        return self._list_open_docs(DOC_TYPE_DATABASE)

    @property
    def open_grids(self):
        return self._list_open_docs(DOC_TYPE_GRID)

    @property
    def open_maps(self):
        return self._list_open_docs(DOC_TYPE_MAP)

    @property
    def open_3dv(self):
        return self._list_open_docs(DOC_TYPE_3DV)

    @property
    def open_voxels(self):
        return self._list_open_docs(DOC_TYPE_VOXEL)

    @property
    def open_voxi_models(self):
        return self._list_open_docs(DOC_TYPE_VOXI)

    @property
    def open_gmsys_3d(self):
        return self._list_open_docs(DOC_TYPE_GMS3D)

    @property
    def open_gmsys_2d(self):
        return self._list_open_docs(DOC_TYPE_GMS2D)

    @property
    def current_database(self):
        return self._current_doc(DOC_TYPE_DATABASE)

    @property
    def current_grid(self):
        return self._current_doc(DOC_TYPE_GRID)

    @property
    def current_map(self):
        return self._current_doc(DOC_TYPE_MAP)

    @property
    def current_3dv(self):
        return self._current_doc(DOC_TYPE_3DV)

    @property
    def current_voxel(self):
        return self._current_doc(DOC_TYPE_VOXEL)

    @property
    def current_voxi(self):
        return self._current_doc(DOC_TYPE_VOXI)

    @property
    def current_gmsys_3d(self):
        return self._current_doc(DOC_TYPE_GMS3D)

    @property
    def current_gmsys_2d(self):
        return self._current_doc(DOC_TYPE_GMS2D)

    @property
    def menus(self):
        """
        Returns Oasis montaj menu information.
    
        :returns:   (default_menus, loaded_menus, user_menus)
    
       .. versionadded:: 9.2    
        """

        def_menus = gxapi.GXLST.create(512)
        loaded_menus = gxapi.GXLST.create(512)
        user_menus = gxapi.GXLST.create(512)
        gxapi.GXSYS.get_loaded_menus(def_menus, loaded_menus, user_menus)

        return list(dict_from_lst(def_menus).keys()), \
               list(dict_from_lst(loaded_menus).keys()), \
               list(dict_from_lst(user_menus).keys())


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
    This method depends on "user_input.gx" and can only be used from an extension running
    inside a Geosoft Desktop application.

    :param title:       dialog box title.  A description can be added as a second-line using a line-break.
                        example: "Your title/nDescriptive help"
    :param prompt:      prompt string to
    :param kind:        kind of response required: 'string', 'int', 'float', 'file', 'colour' or 'list'
    :param items:       comma-separated string or list/tupple of items for a list
    :param default:     default value.  For multifile can be a string ('|' delimiter) or list/tupple.
    :param filemask:    File type mask '.dat', '*.dat,*.grd', '\*\*,*.grd' for multiple files
                        Comma delimited, or a list/tupple
    :return:        user response
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