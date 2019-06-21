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
class GXAGG(gxapi_cy.WrapAGG):
    """
    GXAGG class.

    The `GXAGG <geosoft.gxapi.GXAGG>` class is used to handle image display on maps.
    An aggregate contains one or more image layers (LAY) with
    each layer representing a grid or image file. The `GXAGG <geosoft.gxapi.GXAGG>`
    will combine all the layers to form one image
    """

    def __init__(self, handle=0):
        super(GXAGG, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXAGG <geosoft.gxapi.GXAGG>`
        
        :returns: A null `GXAGG <geosoft.gxapi.GXAGG>`
        :rtype:   GXAGG
        """
        return GXAGG()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def set_model(self, model):
        """
        Sets the Color Model
        
        :param model:  :ref:`AGG_MODEL`
        :type  model:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_model(model)
        




    def change_brightness(self, brt):
        """
        Change the brightness.
        
        :param brt:  -1.0 - black; 0.0 no change; 1.0 white
        :type  brt:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 0.0 brightness does nothing.
        -1.0 to 0.0 makes colors darker, -1.0 is black
        0.0 to 1.0 makes colors lighter, 1.0 is white
        """
        self._change_brightness(brt)
        



    @classmethod
    def create(cls):
        """
        Create an aggregate
        

        :returns:    `GXAGG <geosoft.gxapi.GXAGG>` object
        :rtype:      GXAGG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapAGG._create(GXContext._get_tls_geo())
        return GXAGG(ret_val)



    @classmethod
    def create_map(cls, map, name):
        """
        Create `GXAGG <geosoft.gxapi.GXAGG>` from Map with Group name.
        
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` on which to place the view
        :param name:  `GXAGG <geosoft.gxapi.GXAGG>` group name
        :type  map:   GXMAP
        :type  name:  str

        :returns:     `GXAGG <geosoft.gxapi.GXAGG>` object
        :rtype:       GXAGG

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Agg Group name must include the View name with a
        backslash separating the view name and group name; e.g.
        "Data\\AGG_test" (when used as a string, the double slash
        represents as single \\).
        """
        ret_val = gxapi_cy.WrapAGG._create_map(GXContext._get_tls_geo(), map, name.encode())
        return GXAGG(ret_val)






    def get_layer_itr(self, layer, itr):
        """
        Get the `GXITR <geosoft.gxapi.GXITR>` of a layer
        
        :param layer:  Layer number
        :type  layer:  int
        :type  itr:    GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Layers are numbered from 0, consecutively in the order they are
        placed in the aggregate.

        An error will occur if the layer does not exist.

        Caller must create/destroy `GXITR <geosoft.gxapi.GXITR>`.
        """
        self._get_layer_itr(layer, itr)
        




    def list_img(self, gvv):
        """
        Lists file names of all the IMGs inside of the `GXAGG <geosoft.gxapi.GXAGG>`.
        
        :param gvv:  `GXVV <geosoft.gxapi.GXVV>` of type -`STR_FILE <geosoft.gxapi.STR_FILE>`
        :type  gvv:  GXVV

        :returns:    The number of IMGs.
        :rtype:      int

        .. versionadded:: 5.0.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned `GXVV <geosoft.gxapi.GXVV>` contains the file names.
        """
        ret_val = self._list_img(gvv)
        return ret_val




    def num_layers(self):
        """
        Get the number of layers in an aggregate.
        

        :returns:    The number of layers in an aggregate.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_layers()
        return ret_val




    def layer_img(self, name, zone, color, cont):
        """
        Add an image as a layer in an aggregate.
        
        :param name:   Grid name
        :param zone:   :ref:`AGG_LAYER_ZONE` transform to use if color table has none defined.
        :param color:  Color table name, "" for default This can be a .TBL .ZON .`GXITR <geosoft.gxapi.GXITR>` or .`GXAGG <geosoft.gxapi.GXAGG>` file .TBL is the default
        :param cont:   Color contour interval or `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :type  name:   str
        :type  zone:   int
        :type  color:  str
        :type  cont:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `layer_shade_img <geosoft.gxapi.GXAGG.layer_shade_img>`
        """
        self._layer_img(name.encode(), zone, color.encode(), cont)
        




    def layer_img_ex(self, name, zone, color, min, max, cont):
        """
        Add an image as a layer in an aggregate.
        
        :param name:   Grid name
        :param zone:   :ref:`AGG_LAYER_ZONE` transform to use if color table has none defined.
        :param color:  Color table name, "" for default This can be a .TBL .ZON .`GXITR <geosoft.gxapi.GXITR>` or .`GXAGG <geosoft.gxapi.GXAGG>` file .TBL is the default
        :param min:    Minimum value or `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param max:    Maximum value or `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param cont:   Color contour interval or `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :type  name:   str
        :type  zone:   int
        :type  color:  str
        :type  min:    float
        :type  max:    float
        :type  cont:   float

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `layer_shade_img <geosoft.gxapi.GXAGG.layer_shade_img>`
        """
        self._layer_img_ex(name.encode(), zone, color.encode(), min, max, cont)
        




    def layer_shade_img(self, name, color, inc, dec, scl):
        """
        Add a shaded image as a layer in an aggregate.
        
        :param name:   Grid name
        :param color:  Color table name, "" for default
        :param inc:    Inclination
        :param dec:    Declination
        :param scl:    Scale (`rDUMMY <geosoft.gxapi.rDUMMY>` for default, returns value used)
        :type  name:   str
        :type  color:  str
        :type  inc:    float
        :type  dec:    float
        :type  scl:    float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A new grid file will be created to hold the shaded
        image data.  This file will have the same name as the
        original grid but with "_s" added to the root name.
        It will always be located in the workspace directory
        regardless of the location of the original source image.
        If the file already exists, it will replaced.
        """
        scl.value = self._layer_shade_img(name.encode(), color.encode(), inc, dec, scl.value)
        




    def get_brightness(self):
        """
        Get the brightness setting of the `GXAGG <geosoft.gxapi.GXAGG>`
        
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Brightness can range from -1.0 (black) to 1.0 (white).
        This brightness control is relative to the normal color
        when the `GXAGG <geosoft.gxapi.GXAGG>` is created.

        `GXAGG <geosoft.gxapi.GXAGG>` brightness depends on the brightness of the `GXITR <geosoft.gxapi.GXITR>` of each layer.
        Calling dGetBright_AGG will poll all layers, and if all have the same
        brightness, this is returned.  If any of the layers have a different
        brightness, the current brightness of each layer is changed to be
        the reference brightness (0.0)and the brightness value of 0.0 is
        returned.

        .. seealso::

            `change_brightness <geosoft.gxapi.GXAGG.change_brightness>`, `get_brightness <geosoft.gxapi.GXAGG.get_brightness>`, `change_brightness <geosoft.gxapi.GXAGG.change_brightness>`
        """
        ret_val = self._get_brightness()
        return ret_val




    def set_layer_itr(self, layer, itr):
        """
        Set the `GXITR <geosoft.gxapi.GXITR>` of a layer
        
        :param layer:  Layer number
        :type  layer:  int
        :type  itr:    GXITR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Layers are numbered from 0, consecutively in the order they are
        placed in the aggregate.

        An error will occur if the layer does not exist.

        Caller must create/destroy `GXITR <geosoft.gxapi.GXITR>`.
        """
        self._set_layer_itr(layer, itr)
        




    def set_render_method(self, method):
        """
        Sets the Rendering Method
        
        :param method:  :ref:`AGG_RENDER`
        :type  method:  int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_render_method(method)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer