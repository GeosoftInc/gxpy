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
class GXMAPL:
    """
    GXMAPL class.

    The `GXMAPL <geosoft.gxapi.GXMAPL>` class is the interface with the MAPPLOT program,
    which reads a MAPPLOT control file and plots graphical
    entities to a map. The `GXMAPL <geosoft.gxapi.GXMAPL>` object is created for a given
    control file, then passed to the MAPPLOT program, along
    with the target `GXMAP <geosoft.gxapi.GXMAP>` object on which to do the drawing
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
        A null (undefined) instance of `GXMAPL`
        
        :returns: A null `GXMAPL`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMAPL` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMAPL`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, name, ref_name, line):
        """
        Create a `GXMAPL <geosoft.gxapi.GXMAPL>`.
        
        :param name:      `GXMAPL <geosoft.gxapi.GXMAPL>` file name
        :param ref_name:  Map base reference name
        :param line:      Start line number in file (0 is first)
        :type  name:      str
        :type  ref_name:  str
        :type  line:      int

        :returns:         `GXMAPL <geosoft.gxapi.GXMAPL>`, aborts if creation fails
        :rtype:           GXMAPL

        .. versionadded:: 5.0

        **Note:**

        The default map groups will use the reference name with
        "_Data" and "_Base" added.  If no reference name is specified,
        the name "`GXMAPL <geosoft.gxapi.GXMAPL>`" is used
        """
        ret_val = gxapi_cy.WrapMAPL.create(GXContext._get_tls_geo(), name.encode(), ref_name.encode(), line)
        return GXMAPL(ret_val)



    @classmethod
    def create_reg(cls, name, ref_name, line, reg):
        """
        Create a `GXMAPL <geosoft.gxapi.GXMAPL>` with `GXREG <geosoft.gxapi.GXREG>`.
        
        :param name:      `GXMAPL <geosoft.gxapi.GXMAPL>` file name
        :param ref_name:  Map base reference name
        :param line:      Start line number in file (0 is first)
        :type  name:      str
        :type  ref_name:  str
        :type  line:      int
        :type  reg:       GXREG

        :returns:         `GXMAPL <geosoft.gxapi.GXMAPL>`, aborts if creation fails
        :rtype:           GXMAPL

        .. versionadded:: 5.0

        **Note:**

        The default map groups will use the reference name with
        "_Data" and "_Base" added.  If no reference name is specified,
        the name "`GXMAPL <geosoft.gxapi.GXMAPL>`" is used
        """
        ret_val = gxapi_cy.WrapMAPL.create_reg(GXContext._get_tls_geo(), name.encode(), ref_name.encode(), line, reg._wrapper)
        return GXMAPL(ret_val)






    def process(self, map):
        """
        Process a `GXMAPL <geosoft.gxapi.GXMAPL>`
        
        :type  map:   GXMAP

        .. versionadded:: 5.0
        """
        self._wrapper.process(map._wrapper)
        




    def replace_string(self, var, repl):
        """
        Adds a replacement string to a mapplot control file.
        
        :param var:   Variable
        :param repl:  Replacement
        :type  var:   str
        :type  repl:  str

        .. versionadded:: 5.0
        """
        self._wrapper.replace_string(var.encode(), repl.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer