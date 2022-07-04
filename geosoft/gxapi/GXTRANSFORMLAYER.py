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
class GXTRANSFORMLAYER(gxapi_cy.WrapTRANSFORMLAYER):
    """
    GXTRANSFORMLAYER class.

    Object to interface with GMSYS 3D view objects that supports transforming layer.
    """

    def __init__(self, handle=0):
        super(GXTRANSFORMLAYER, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTRANSFORMLAYER <geosoft.gxapi.GXTRANSFORMLAYER>`
        
        :returns: A null `GXTRANSFORMLAYER <geosoft.gxapi.GXTRANSFORMLAYER>`
        :rtype:   GXTRANSFORMLAYER
        """
        return GXTRANSFORMLAYER()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def end(self, applyChanges):
        """
        End interactive editing for selected grid layer in gmsys.
        
        :param applyChanges:  Apply changes to layer.
        :type  applyChanges:  bool

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._end(applyChanges)
        




    def cancel_(self):
        """
        Cancel changes done in the transform layer
        

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._cancel_()
        




    def undo(self):
        """
        Undo one step of editing in the transform layer
        

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._undo()
        




    def redo(self):
        """
        Redo one step of editing in the transform layer
        

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._redo()
        




    def can_undo(self):
        """
        Can perform undo on the transform layer
        
        :rtype:             int

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._can_undo()
        return ret_val




    def can_redo(self):
        """
        Can perform redo on the transform layer
        
        :rtype:             int

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._can_redo()
        return ret_val




    def save_to_new_layer_grid(self, sGrid):
        """
        Save changes to a new grid
        
        :param sGrid:       output grid path
        :type  sGrid:       str

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._save_to_new_layer_grid(sGrid.encode())
        




    def apply_constant_transform(self, elevation):
        """
        Apply constant transform to the transform layer
        
        :param elevation:   change in elevation to apply
        :type  elevation:   float

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._apply_constant_transform(elevation)
        




    def select_node(self, nodeIdx):
        """
        Select or deselect a node by its index
        
        :param nodeIdx:     node index
        :type  nodeIdx:     int

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._select_node(nodeIdx)
        




    def clear_node_selection(self):
        """
        Clear the section status of every node
        

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._clear_node_selection()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer