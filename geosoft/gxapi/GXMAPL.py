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
class GXMAPL:
    """
    GXMAPL class.

    The :class:`geosoft.gxapi.GXMAPL` class is the interface with the MAPPLOT program,
    which reads a MAPPLOT control file and plots graphical
    entities to a map. The :class:`geosoft.gxapi.GXMAPL` object is created for a given
    control file, then passed to the MAPPLOT program, along
    with the target :class:`geosoft.gxapi.GXMAP` object on which to do the drawing
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMAPL(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXMAPL`
        
        :returns: A null :class:`geosoft.gxapi.GXMAPL`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMAPL` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMAPL`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2, p3):
        """
        Create a :class:`geosoft.gxapi.GXMAPL`.

        **Note:**

        The default map groups will use the reference name with
        "_Data" and "_Base" added.  If no reference name is specified,
        the name ":class:`geosoft.gxapi.GXMAPL`" is used
        """
        ret_val = gxapi_cy.WrapMAPL.create(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return GXMAPL(ret_val)



    @classmethod
    def create_reg(cls, p1, p2, p3, p4):
        """
        Create a :class:`geosoft.gxapi.GXMAPL` with :class:`geosoft.gxapi.GXREG`.

        **Note:**

        The default map groups will use the reference name with
        "_Data" and "_Base" added.  If no reference name is specified,
        the name ":class:`geosoft.gxapi.GXMAPL`" is used
        """
        ret_val = gxapi_cy.WrapMAPL.create_reg(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4._wrapper)
        return GXMAPL(ret_val)






    def process(self, p2):
        """
        Process a :class:`geosoft.gxapi.GXMAPL`
        """
        self._wrapper.process(p2._wrapper)
        




    def replace_string(self, p2, p3):
        """
        Adds a replacement string to a mapplot control file.
        """
        self._wrapper.replace_string(p2.encode(), p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer