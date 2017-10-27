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
class GXRA:
    """
    GXRA class.

    The `GXRA <geosoft.gxapi.GXRA>` class is used to access ASCII files sequentially or
    by line number. The files are opened in read-only mode, so no
    write operations are defined
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapRA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXRA`
        
        :returns: A null `GXRA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXRA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXRA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, file):
        """
        Creates `GXRA <geosoft.gxapi.GXRA>`
        """
        ret_val = gxapi_cy.WrapRA.create(GXContext._get_tls_geo(), file.encode())
        return GXRA(ret_val)



    @classmethod
    def create_sbf(cls, sbf, file):
        """
        Creates `GXRA <geosoft.gxapi.GXRA>` on an `GXSBF <geosoft.gxapi.GXSBF>`

        **Note:**

        This method allows you to open an `GXRA <geosoft.gxapi.GXRA>` in a structured file
        storage (an `GXSBF <geosoft.gxapi.GXSBF>`).  SBFs can be created inside other data
        containers, such as workspaces, maps, images and databases.
        This lets you store application specific information together
        with the data to which it applies.

        .. seealso::

            sbf.gxh
        """
        ret_val = gxapi_cy.WrapRA.create_sbf(GXContext._get_tls_geo(), sbf._wrapper, file.encode())
        return GXRA(ret_val)






    def gets(self, strbuff):
        """
        Get next full line from `GXRA <geosoft.gxapi.GXRA>`
        """
        ret_val, strbuff.value = self._wrapper.gets(strbuff.value.encode())
        return ret_val




    def len(self):
        """
        Returns the total number of lines in `GXRA <geosoft.gxapi.GXRA>`
        """
        ret_val = self._wrapper.len()
        return ret_val




    def line(self):
        """
        Returns current line #, 0 is the first

        **Note:**

        This will be the next line read.
        """
        ret_val = self._wrapper.line()
        return ret_val




    def seek(self, line):
        """
        Position next read to specified line #
        """
        ret_val = self._wrapper.seek(line)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer