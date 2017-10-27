### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
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

    The `GXEDOC <geosoft.gxapi.GXEDOC>` class provides access to a generic documents views as loaded within
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
        Creates a new `GXGMSYS <geosoft.gxapi.GXGMSYS>` 3D Model into the workspace, flags as new.
        
        :param name:  Document to load.
        :param nx:    X Size
        :param ny:    Y Size
        :param type:  `GMS3D_MODELTYPE`
        :type  name:  str
        :type  nx:    int
        :type  ny:    int
        :type  type:  int

        :returns:     Handle to the newly created edited model.
        :rtype:       GXEDOC

        .. versionadded:: 5.0

        **Note:**

        See `load <geosoft.gxapi.GXEDOC.load>`. This is used for brand new documents, it also sets
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
        
        :param type:  `EDOC_TYPE`
        :type  type:  int

        :returns:     `GXEDOC <geosoft.gxapi.GXEDOC>` Object
        :rtype:       GXEDOC

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapEDOC.current(GXContext._get_tls_geo(), type)
        return GXEDOC(ret_val)



    @classmethod
    def current_no_activate(cls, type):
        """
        This method returns the Current Edited Document.
        
        :param type:  `EDOC_TYPE`
        :type  type:  int

        :returns:     `GXEDOC <geosoft.gxapi.GXEDOC>` Object
        :rtype:       GXEDOC

        .. versionadded:: 9.0

        **Note:**

        This function acts just like `current <geosoft.gxapi.GXEDOC.current>` except that the document is not activated (brought to foreground) and no
        				guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDOC.current_no_activate(GXContext._get_tls_geo(), type)
        return GXEDOC(ret_val)



    @classmethod
    def current_if_exists(cls, type):
        """
        This method returns the Current Edited Document.
        
        :param type:  `EDOC_TYPE`
        :type  type:  int

        :returns:     `GXEDOC <geosoft.gxapi.GXEDOC>` Object to current edited document. If there is no current document,
                      the user is not prompted for a document, and 0 is returned.
        :rtype:       GXEDOC

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapEDOC.current_if_exists(GXContext._get_tls_geo(), type)
        return GXEDOC(ret_val)





    @classmethod
    def get_documents_lst(cls, lst, path, type):
        """
        Load the file names of open documents into a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` to load
        :param path:  `EDOC_PATH`
        :param type:  `EDOC_TYPE`
        :type  lst:   GXLST
        :type  path:  int
        :type  type:  int

        :returns:     The number of documents loaded into the `GXLST <geosoft.gxapi.GXLST>`.
                      The `GXLST <geosoft.gxapi.GXLST>` is cleared first.
        :rtype:       int

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapEDOC.get_documents_lst(GXContext._get_tls_geo(), lst._wrapper, path, type)
        return ret_val




    def get_name(self, name):
        """
        Get the name of the document object of this `GXEDOC <geosoft.gxapi.GXEDOC>`.
        
        :param name:  Name returned
        :type  name:  str_ref

        .. versionadded:: 5.0
        """
        name.value = self._wrapper.get_name(name.value.encode())
        




    def get_window_state(self):
        """
        Retrieve the current state of the document window
        

        :returns:     `EDOC_WINDOW_STATE`
        :rtype:       int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.get_window_state()
        return ret_val



    @classmethod
    def have_current(cls, type):
        """
        Returns true if a document is loaded
        
        :param type:  `EDOC_TYPE`
        :type  type:  int

        :returns:     `GEO_BOOL`
        :rtype:       int

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapEDOC.have_current(GXContext._get_tls_geo(), type)
        return ret_val



    @classmethod
    def loaded(cls, name, type):
        """
        Returns 1 if a document is loaded .
        
        :param name:  document name
        :param type:  `EDOC_TYPE`
        :type  name:  str
        :type  type:  int

        :returns:     1 if document is loaded, 0 otherwise.
        :rtype:       int

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapEDOC.loaded(GXContext._get_tls_geo(), name.encode(), type)
        return ret_val




    def get_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        
        :param left:         Window left position
        :param top:          Window top position
        :param right:        Window right position
        :param bottom:       Window bottom position
        :param state:        Window state `EDOC_WINDOW_STATE`
        :param is_floating:  Docked or floating `EDOC_WINDOW_POSITION`
        :type  left:         int_ref
        :type  top:          int_ref
        :type  right:        int_ref
        :type  bottom:       int_ref
        :type  state:        int_ref
        :type  is_floating:  int_ref

        .. versionadded:: 9.0
        """
        left.value, top.value, right.value, bottom.value, state.value, is_floating.value = self._wrapper.get_window_position(left.value, top.value, right.value, bottom.value, state.value, is_floating.value)
        




    def set_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        
        :param left:         Window left position
        :param top:          Window top position
        :param right:        Window right position
        :param bottom:       Window bottom position
        :param state:        Window state `EDOC_WINDOW_STATE`
        :param is_floating:  Docked or floating `EDOC_WINDOW_POSITION`
        :type  left:         int
        :type  top:          int
        :type  right:        int
        :type  bottom:       int
        :type  state:        int
        :type  is_floating:  int

        .. versionadded:: 9.0
        """
        self._wrapper.set_window_position(left, top, right, bottom, state, is_floating)
        




    def read_only(self):
        """
        Checks if a document is currently opened in a read-only mode.
        

        :returns:     `GEO_BOOL`
        :rtype:       int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.read_only()
        return ret_val



    @classmethod
    def load(cls, name, type):
        """
        Loads a list of documents into the workspace
        
        :param name:  list of documents (';' or '|' delimited) to load.
        :param type:  `EDOC_TYPE`
        :type  name:  str
        :type  type:  int

        :returns:     Handle to current edited document, which will be the last
                      document in the list.
        :rtype:       GXEDOC

        .. versionadded:: 5.0

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
        
        :param name:  list of documents (';' or '|' delimited) to load.
        :param type:  `EDOC_TYPE`
        :type  name:  str
        :type  type:  int

        :returns:     Handle to current edited document, which will be the last
                      document in the list.
        :rtype:       GXEDOC

        .. versionadded:: 9.0

        **Note:**

        This function acts just like `load <geosoft.gxapi.GXEDOC.load>` except that the document(s) is not activated (brought to foreground) and no
        					guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDOC.load_no_activate(GXContext._get_tls_geo(), name.encode(), type)
        return GXEDOC(ret_val)




    def make_current(self):
        """
        Makes this `GXEDOC <geosoft.gxapi.GXEDOC>` object the current active object to the user.
        

        .. versionadded:: 5.0
        """
        self._wrapper.make_current()
        




    def set_window_state(self, state):
        """
        Changes the state of the document window
        
        :param state:  `EDOC_WINDOW_STATE`
        :type  state:  int

        .. versionadded:: 5.0
        """
        self._wrapper.set_window_state(state)
        



    @classmethod
    def sync(cls, file, type):
        """
        Syncronize the Metadata of a document that is not currently open
        
        :param file:  Document file name
        :param type:  `EDOC_TYPE`
        :type  file:  str
        :type  type:  int

        .. versionadded:: 5.0
        """
        gxapi_cy.WrapEDOC.sync(GXContext._get_tls_geo(), file.encode(), type)
        




    def sync_open(self):
        """
        Syncronize the Metadata of a document
        

        .. versionadded:: 5.0
        """
        self._wrapper.sync_open()
        



    @classmethod
    def un_load(cls, name, type):
        """
        Unloads an edited document.
        
        :param name:  Name of document to unload
        :param type:  `EDOC_TYPE`
        :type  name:  str
        :type  type:  int

        .. versionadded:: 5.0

        **Note:**

        If the document is not loaded, nothing happens.
        Same as `un_load_verify <geosoft.gxapi.GXEDOC.un_load_verify>` with FALSE to prompt save.
        """
        gxapi_cy.WrapEDOC.un_load(GXContext._get_tls_geo(), name.encode(), type)
        



    @classmethod
    def un_load_all(cls, type):
        """
        Unloads all opened documents
        
        :param type:  `EDOC_TYPE`
        :type  type:  int

        .. versionadded:: 5.0
        """
        gxapi_cy.WrapEDOC.un_load_all(GXContext._get_tls_geo(), type)
        



    @classmethod
    def un_load_discard(cls, name, type):
        """
        Unloads a document in the workspace, discards changes.
        
        :param name:  Name of document to unload
        :param type:  `EDOC_TYPE`
        :type  name:  str
        :type  type:  int

        .. versionadded:: 5.0

        **Note:**

        If the document is not loaded, nothing happens.
        """
        gxapi_cy.WrapEDOC.un_load_discard(GXContext._get_tls_geo(), name.encode(), type)
        



    @classmethod
    def un_load_verify(cls, name, verify, type):
        """
        Unloads an edited document, optional prompt to save.
        
        :param name:    Name of document to unload
        :param verify:  `EDOC_UNLOAD`
        :param type:    `EDOC_TYPE`
        :type  name:    str
        :type  verify:  int
        :type  type:    int

        .. versionadded:: 5.0

        **Note:**

        If the document is not loaded, nothing happens.
        The user can be prompted to save before unloading.
        If `EDOC_UNLOAD_NO_PROMPT <geosoft.gxapi.EDOC_UNLOAD_NO_PROMPT>`, data is always saved.
        """
        gxapi_cy.WrapEDOC.un_load_verify(GXContext._get_tls_geo(), name.encode(), verify, type)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer