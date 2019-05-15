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
class GXRA(gxapi_cy.WrapRA):
    """
    GXRA class.

    The `GXRA <geosoft.gxapi.GXRA>` class is used to access ASCII files sequentially or
    by line number. The files are opened in read-only mode, so no
    write operations are defined
    """

    def __init__(self, handle=0):
        super(GXRA, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXRA <geosoft.gxapi.GXRA>`
        
        :returns: A null `GXRA <geosoft.gxapi.GXRA>`
        :rtype:   GXRA
        """
        return GXRA()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, file):
        """
        Creates `GXRA <geosoft.gxapi.GXRA>`
        
        :param file:  Name of the file
        :type  file:  str

        :returns:     `GXRA <geosoft.gxapi.GXRA>` Object
        :rtype:       GXRA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapRA._create(GXContext._get_tls_geo(), file.encode())
        return GXRA(ret_val)



    @classmethod
    def create_sbf(cls, sbf, file):
        """
        Creates `GXRA <geosoft.gxapi.GXRA>` on an `GXSBF <geosoft.gxapi.GXSBF>`
        
        :param sbf:   Storage
        :param file:  Name of the file
        :type  sbf:   GXSBF
        :type  file:  str

        :returns:     `GXRA <geosoft.gxapi.GXRA>` Object
        :rtype:       GXRA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method allows you to open an `GXRA <geosoft.gxapi.GXRA>` in a structured file
        storage (an `GXSBF <geosoft.gxapi.GXSBF>`).  SBFs can be created inside other data
        containers, such as workspaces, maps, images and databases.
        This lets you store application specific information together
        with the data to which it applies.

        .. seealso::

            sbf.gxh
        """
        ret_val = gxapi_cy.WrapRA._create_sbf(GXContext._get_tls_geo(), sbf, file.encode())
        return GXRA(ret_val)






    def gets(self, strbuff):
        """
        Get next full line from `GXRA <geosoft.gxapi.GXRA>`
        
        :param strbuff:  Buffer in which to place string
        :type  strbuff:  str_ref

        :returns:        0 - Ok
                         1 - End of file
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, strbuff.value = self._gets(strbuff.value.encode())
        return ret_val




    def len(self):
        """
        Returns the total number of lines in `GXRA <geosoft.gxapi.GXRA>`
        

        :returns:    # of lines in the `GXRA <geosoft.gxapi.GXRA>`.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._len()
        return ret_val




    def line(self):
        """
        Returns current line #, 0 is the first
        

        :returns:    The current read line location.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This will be the next line read.
        """
        ret_val = self._line()
        return ret_val




    def seek(self, line):
        """
        Position next read to specified line #
        
        :param line:  Line #, 0 is the first.
        :type  line:  int

        :returns:     0 if seeked line is within the range of lines,
                      1 if outside range, line pointer will not be moved.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._seek(line)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer