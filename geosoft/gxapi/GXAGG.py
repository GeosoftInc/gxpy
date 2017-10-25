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
class GXAGG:
    """
    GXAGG class.

    The :class:`geosoft.gxapi.GXAGG` class is used to handle image display on maps.
    An aggregate contains one or more image layers (LAY) with
    each layer representing a grid or image file. The :class:`geosoft.gxapi.GXAGG`
    will combine all the layers to form one image
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapAGG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXAGG`
        
        :returns: A null :class:`geosoft.gxapi.GXAGG`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXAGG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXAGG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def set_model(self, p2):
        """
        Sets the Color Model
        """
        self._wrapper.set_model(p2)
        




    def change_brightness(self, p2):
        """
        Change the brightness.

        **Note:**

        0.0 brightness does nothing.
        -1.0 to 0.0 makes colors darker, -1.0 is black
        0.0 to 1.0 makes colors lighter, 1.0 is white
        """
        self._wrapper.change_brightness(p2)
        



    @classmethod
    def create(cls):
        """
        Create an aggregate
        """
        ret_val = gxapi_cy.WrapAGG.create(GXContext._get_tls_geo())
        return GXAGG(ret_val)



    @classmethod
    def create_map(cls, p1, p2):
        """
        Create :class:`geosoft.gxapi.GXAGG` from Map with Group name.

        **Note:**

        The Agg Group name must include the View name with a
        backslash separating the view name and group name; e.g.
        "Data\\AGG_test" (when used as a string, the double slash
        represents as single \\).
        """
        ret_val = gxapi_cy.WrapAGG.create_map(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXAGG(ret_val)






    def get_layer_itr(self, p2, p3):
        """
        Get the :class:`geosoft.gxapi.GXITR` of a layer

        **Note:**

        Layers are numbered from 0, consecutively in the order they are
        placed in the aggregate.
        
        An error will occur if the layer does not exist.
        
        Caller must create/destroy :class:`geosoft.gxapi.GXITR`.
        """
        self._wrapper.get_layer_itr(p2, p3._wrapper)
        




    def list_img(self, p2):
        """
        Lists file names of all the IMGs inside of the :class:`geosoft.gxapi.GXAGG`.

        **Note:**

        The returned :class:`geosoft.gxapi.GXVV` contains the file names.
        """
        ret_val = self._wrapper.list_img(p2._wrapper)
        return ret_val




    def num_layers(self):
        """
        Get the number of layers in an aggregate.
        """
        ret_val = self._wrapper.num_layers()
        return ret_val




    def layer_img(self, p2, p3, p4, p5):
        """
        Add an image as a layer in an aggregate.
        """
        self._wrapper.layer_img(p2.encode(), p3, p4.encode(), p5)
        




    def layer_img_ex(self, p2, p3, p4, p5, p6, p7):
        """
        Add an image as a layer in an aggregate.
        """
        self._wrapper.layer_img_ex(p2.encode(), p3, p4.encode(), p5, p6, p7)
        




    def layer_shade_img(self, p2, p3, p4, p5, p6):
        """
        Add a shaded image as a layer in an aggregate.

        **Note:**

        A new grid file will be created to hold the shaded
        image data.  This file will have the same name as the
        original grid but with "_s" added to the root name.
        It will always be located in the workspace directory
        regardless of the location of the original source image.
        If the file already exists, it will replaced.
        """
        p6.value = self._wrapper.layer_shade_img(p2.encode(), p3.encode(), p4, p5, p6.value)
        




    def get_brightness(self):
        """
        Get the brightness setting of the :class:`geosoft.gxapi.GXAGG`

        **Note:**

        Brightness can range from -1.0 (black) to 1.0 (white).
        This brightness control is relative to the normal color
        when the :class:`geosoft.gxapi.GXAGG` is created.
        
        :class:`geosoft.gxapi.GXAGG` brightness depends on the brightness of the :class:`geosoft.gxapi.GXITR` of each layer.
        Calling dGetBright_AGG will poll all layers, and if all have the same
        brightness, this is returned.  If any of the layers have a different
        brightness, the current brightness of each layer is changed to be
        the reference brightness (0.0)and the brightness value of 0.0 is
        returned.
        """
        ret_val = self._wrapper.get_brightness()
        return ret_val




    def set_layer_itr(self, p2, p3):
        """
        Set the :class:`geosoft.gxapi.GXITR` of a layer

        **Note:**

        Layers are numbered from 0, consecutively in the order they are
        placed in the aggregate.
        
        An error will occur if the layer does not exist.
        
        Caller must create/destroy :class:`geosoft.gxapi.GXITR`.
        """
        self._wrapper.set_layer_itr(p2, p3._wrapper)
        




    def set_render_method(self, p2):
        """
        Sets the Rendering Method
        """
        self._wrapper.set_render_method(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer