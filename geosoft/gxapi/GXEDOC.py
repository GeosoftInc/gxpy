### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEDOC:
    """
    GXEDOC class.

    The `GXEDOC` class provides access to a generic documents views as loaded within
    Oasis montaj.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEDOC(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEDOC`
        
        :returns: A null `GXEDOC`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXEDOC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXEDOC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# GMSYS 3D Models


    @classmethod
    def create_new_gms_3d(cls, name, nx, ny, type):
        """
        Creates a new `GXGMSYS` 3D Model into the workspace, flags as new.

        **Note:**

        See `load`. This is used for brand new documents, it also sets
        an internal flag such that if on closing the user chooses
        not to save changes, the document is deleted thus keeping the
        project folders clean.
        """
        ret_val = gxapi_cy.WrapEDOC.create_new_gms_3d(GXContext._get_tls_geo(), name.encode(), nx, ny, type)
        return GXEDOC(ret_val)




# Miscellaneous


    @classmethod
    def current(cls, type):
        """
        This method returns the Current Edited Document.
        """
        ret_val = gxapi_cy.WrapEDOC.current(GXContext._get_tls_geo(), type)
        return GXEDOC(ret_val)



    @classmethod
    def current_no_activate(cls, type):
        """
        This method returns the Current Edited Document.

        **Note:**

        This function acts just like `current` except that the document is not activated (brought to foreground) and no
        				guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDOC.current_no_activate(GXContext._get_tls_geo(), type)
        return GXEDOC(ret_val)



    @classmethod
    def current_if_exists(cls, type):
        """
        This method returns the Current Edited Document.
        """
        ret_val = gxapi_cy.WrapEDOC.current_if_exists(GXContext._get_tls_geo(), type)
        return GXEDOC(ret_val)





    @classmethod
    def get_documents_lst(cls, lst, path, type):
        """
        Load the file names of open documents into a `GXLST`.
        """
        ret_val = gxapi_cy.WrapEDOC.get_documents_lst(GXContext._get_tls_geo(), lst._wrapper, path, type)
        return ret_val




    def get_name(self, name):
        """
        Get the name of the document object of this `GXEDOC`.
        """
        name.value = self._wrapper.get_name(name.value.encode())
        




    def get_window_state(self):
        """
        Retrieve the current state of the document window
        """
        ret_val = self._wrapper.get_window_state()
        return ret_val



    @classmethod
    def have_current(cls, type):
        """
        Returns true if a document is loaded
        """
        ret_val = gxapi_cy.WrapEDOC.have_current(GXContext._get_tls_geo(), type)
        return ret_val



    @classmethod
    def loaded(cls, name, type):
        """
        Returns 1 if a document is loaded .
        """
        ret_val = gxapi_cy.WrapEDOC.loaded(GXContext._get_tls_geo(), name.encode(), type)
        return ret_val




    def get_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        """
        left.value, top.value, right.value, bottom.value, state.value, is_floating.value = self._wrapper.get_window_position(left.value, top.value, right.value, bottom.value, state.value, is_floating.value)
        




    def set_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        """
        self._wrapper.set_window_position(left, top, right, bottom, state, is_floating)
        




    def read_only(self):
        """
        Checks if a document is currently opened in a read-only mode.
        """
        ret_val = self._wrapper.read_only()
        return ret_val



    @classmethod
    def load(cls, name, type):
        """
        Loads a list of documents into the workspace

        **Note:**

        The last listed document will become the current document.
        
        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEDOC.load(GXContext._get_tls_geo(), name.encode(), type)
        return GXEDOC(ret_val)



    @classmethod
    def load_no_activate(cls, name, type):
        """
        Loads a list of documents into the workspace

        **Note:**

        This function acts just like `load` except that the document(s) is not activated (brought to foreground) and no
        					guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDOC.load_no_activate(GXContext._get_tls_geo(), name.encode(), type)
        return GXEDOC(ret_val)




    def make_current(self):
        """
        Makes this `GXEDOC` object the current active object to the user.
        """
        self._wrapper.make_current()
        




    def set_window_state(self, state):
        """
        Changes the state of the document window
        """
        self._wrapper.set_window_state(state)
        



    @classmethod
    def sync(cls, file, type):
        """
        Syncronize the Metadata of a document that is not currently open
        """
        gxapi_cy.WrapEDOC.sync(GXContext._get_tls_geo(), file.encode(), type)
        




    def sync_open(self):
        """
        Syncronize the Metadata of a document
        """
        self._wrapper.sync_open()
        



    @classmethod
    def un_load(cls, name, type):
        """
        Unloads an edited document.

        **Note:**

        If the document is not loaded, nothing happens.
        Same as `un_load_verify` with FALSE to prompt save.
        """
        gxapi_cy.WrapEDOC.un_load(GXContext._get_tls_geo(), name.encode(), type)
        



    @classmethod
    def un_load_all(cls, type):
        """
        Unloads all opened documents
        """
        gxapi_cy.WrapEDOC.un_load_all(GXContext._get_tls_geo(), type)
        



    @classmethod
    def un_load_discard(cls, name, type):
        """
        Unloads a document in the workspace, discards changes.

        **Note:**

        If the document is not loaded, nothing happens.
        """
        gxapi_cy.WrapEDOC.un_load_discard(GXContext._get_tls_geo(), name.encode(), type)
        



    @classmethod
    def un_load_verify(cls, name, verify, type):
        """
        Unloads an edited document, optional prompt to save.

        **Note:**

        If the document is not loaded, nothing happens.
        The user can be prompted to save before unloading.
        If `EDOC_UNLOAD_NO_PROMPT`, data is always saved.
        """
        gxapi_cy.WrapEDOC.un_load_verify(GXContext._get_tls_geo(), name.encode(), verify, type)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer