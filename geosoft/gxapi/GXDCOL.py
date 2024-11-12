#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXST import GXST
from .GXVV import GXVV


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDCOL(gxapi_cy.WrapDCOL):
    """
    GXDCOL class.

    Object to interface with 2D map and 3D view objects that supports colour tool editing.
    """

    def __init__(self, handle=0):
        super(GXDCOL, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDCOL <geosoft.gxapi.GXDCOL>`
        
        :returns: A null `GXDCOL <geosoft.gxapi.GXDCOL>`
        :rtype:   GXDCOL
        """
        return GXDCOL()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def number_of_layers(self):
        """
        Get the number of layers.
        

        :returns:     The number of layers (often just one).
        :rtype:       int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._number_of_layers()
        return ret_val




    def get_type(self):
        """
        Get a layer's type
        

        :returns:     :ref:`DCOL_TYPE`
        :rtype:       int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_type()
        return ret_val




    def get_layer_info(self, index, itr, layer_name):
        """
        Get a layer's information
        
        :param index:       Index of layer
        :param itr:         `GXITR <geosoft.gxapi.GXITR>` Handle
        :param layer_name:  Name returned
        :type  index:       int
        :type  itr:         GXITR
        :type  layer_name:  str_ref

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        layer_name.value = self._get_layer_info(index, itr, layer_name.value.encode())
        




    def get_layer_itr(self, index, itr):
        """
        Get a layer's ITR
        
        :param index:  Index of layer
        :param itr:    `GXITR <geosoft.gxapi.GXITR>` Handle
        :type  index:  int
        :type  itr:    GXITR

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._get_layer_itr(index, itr)
        




    def set_layer_itr(self, index, itr, redrawMap):
        """
        Set a layer's ITR
        
        :param index:      Index of layer
        :param itr:        `GXITR <geosoft.gxapi.GXITR>` Handle
        :param redrawMap:  Force redraw of map (0: No, 1: Yes)?
        :type  index:      int
        :type  itr:        GXITR
        :type  redrawMap:  int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_layer_itr(index, itr, redrawMap)
        




    def set_itr_transform_from_layer(self, index, itr, transformType):
        """
        Set the input ITR transform to the provided type, based on the statistics of the chosen layer.
        
        :param index:          Index of layer
        :param itr:            `GXITR <geosoft.gxapi.GXITR>` Handle
        :param transformType:  :ref:`ITR_ZONE_MODEL`
        :type  index:          int
        :type  itr:            GXITR
        :type  transformType:  int

        :returns:              0 - Ok
                               1 - Cancel
        :rtype:                int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the input tranform type is ITR_ZONE_MODEL_NOZONE or ITR_ZONE_MODEL_NONE
        then the user-preference default will be used.
        NOTE: This alters the input ITR, not the selected layer's own ITR. The layer is accessed
        purely to get the current statistics.
        """
        ret_val = self._set_itr_transform_from_layer(index, itr, transformType)
        return ret_val




    def update_zone_transform_type(self, index, transformType):
        """
        Recalculate the layer's ITR to the provided type, based on the statistics of the chosen layer.
        
        :param index:          Index of layer
        :param transformType:  :ref:`ITR_ZONE_MODEL`
        :type  index:          int
        :type  transformType:  int

        :returns:              0 - Ok
                               1 - Cancel
        :rtype:                int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the input tranform type is ITR_ZONE_MODEL_NOZONE, ITR_ZONE_MODEL_NONE then nothing will happen
        and the function will return 1. The dialogs to enter parameters are shown for Linear, Log, Normal and Equal.
        """
        ret_val = self._update_zone_transform_type(index, transformType)
        return ret_val




    def update_zone_transform_parameters(self, index):
        """
        Recalculate the layer's ITR, based on the current type of the `GXDCOL <geosoft.gxapi.GXDCOL>`. Launches anappropriate zone transform type parameter GUI based on the current selection.
        
        :param index:  Index of layer
        :type  index:  int

        :returns:      0 - Ok
                       1 - Cancel
        :rtype:        int

        .. versionadded:: 2022.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The transform type assumed is the current transform type for the `GXDCOL <geosoft.gxapi.GXDCOL>`. The dialogs
        to enter parameters are shown for Linear, Log, Normal and Equal.
        """
        ret_val = self._update_zone_transform_parameters(index)
        return ret_val




    def get_layer_statistics(self, index):
        """
        Get a `GXST <geosoft.gxapi.GXST>` filled with layer statistics
        
        :param index:  Index of layer
        :type  index:  int

        :returns:      `GXST <geosoft.gxapi.GXST>` object
        :rtype:        GXST

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_layer_statistics(index)
        return GXST(ret_val)




    def get_layer_histogram(self, index, incr, min):
        """
        Get a `GXVV <geosoft.gxapi.GXVV>` filled with histogram bin counts for each zone of the ITR
        
        :param index:  Index of layer
        :param incr:   width of bin increment
        :param min:    Min (value at start of 2nd bin)
        :type  index:  int
        :type  incr:   float_ref
        :type  min:    float_ref

        :returns:      `GXVV <geosoft.gxapi.GXVV>` object
        :rtype:        GXVV

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, incr.value, min.value = self._get_layer_histogram(index, incr.value, min.value)
        return GXVV(ret_val)




    def save_layer_itr(self, index):
        """
        Save the layer's ITR to a file. A dialog prompts for the file name.
        
        :param index:  Index of layer
        :type  index:  int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._save_layer_itr(index)
        




    def get_brightness_type(self):
        """
        Is brightness set separately by layer and by object or just by object?
        

        :returns:     BRIGHTNESS_ALL - Set brightness for the object as a whole only
                      BRIGHTNESS_ALL_AND_LAYERS - Set brightness either for the object as a whole or by layer
        :rtype:       int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** For some objects (like AGG) brightness can be set for each layer, or for the object as a whole, while in others
        (like CSYMB) it can be set only for the object as a whole.
        """
        ret_val = self._get_brightness_type()
        return ret_val




    def set_brightness(self, brightness, layerSelection, layer):
        """
        Set the brightness of a single layer, or all the layers
        
        :param brightness:      Brightness value (-1.0 (black) <= brightness <= 1.0 (white))
        :param layerSelection:  :ref:`BRIGHT`
        :param layer:           layer index (required for BRIGHT_LAYER
        :type  brightness:      float
        :type  layerSelection:  int
        :type  layer:           int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_brightness(brightness, layerSelection, layer)
        




    def get_brightness(self, layerSelection, layer):
        """
        Get the brightness of a single layer, or all the layers
        
        :param layerSelection:  :ref:`BRIGHT`
        :param layer:           layer index (required for BRIGHT_LAYER
        :type  layerSelection:  int
        :type  layer:           int
        :rtype:                 float

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_brightness(layerSelection, layer)
        return ret_val




    def set_transparency(self, transparency):
        """
        Set the transparency. This is set for the entire map group.
        
        :param transparency:  Transparency value (1.0 - Opaque, 0.0 - Transparent)
        :type  transparency:  float

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_transparency(transparency)
        




    def get_transparency(self):
        """
        Get the transparency. This is returned for the entire map group.
        
        :rtype:       float

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_transparency()
        return ret_val




    def reset(self):
        """
        Reset the AGG back to its initial state. Same as cancelling out of the colour tool and restarting; all layers are reset.
        

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._reset()
        




    def end(self, apply_changes):
        """
        TODO
        
        :param apply_changes:  Apply changes to map.
        :type  apply_changes:  bool

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._end(apply_changes)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer