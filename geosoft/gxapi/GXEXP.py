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
class GXEXP(gxapi_cy.WrapEXP):
    """
    GXEXP class.

    `GXEXP <geosoft.gxapi.GXEXP>` objects are created from text strings that contain
    C-like math to be applied to channels in a database.
    It is used with the `GXDU.math <geosoft.gxapi.GXDU.math>` function (see `GXDU <geosoft.gxapi.GXDU>`). See also
    `GXIEXP <geosoft.gxapi.GXIEXP>` for applying math expressions to images (grids).
    See also `GXDU.math <geosoft.gxapi.GXDU.math>` applies expressions to the database
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEXP <geosoft.gxapi.GXEXP>`
        
        :returns: A null `GXEXP <geosoft.gxapi.GXEXP>`
        :rtype:   GXEXP
        """
        return GXEXP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, db, formula, unused):
        """
        This method creates an `GXEXP <geosoft.gxapi.GXEXP>` object.
        
        :param db:       Database Object
        :param formula:  Expression using channel names
        :param unused:   Legacy parameter, no longer used.
        :type  db:       GXDB
        :type  formula:  str
        :type  unused:   int

        :returns:        `GXEXP <geosoft.gxapi.GXEXP>` Object
        :rtype:          GXEXP

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Expressions are strings that contain C-like math to be
        applied to channels in a database.  For example, following
        an expression:

        ::

           "@a = mag-64000; @b = gravity*100;
            $sRatio = @a/@b;
            MULT = @a *@b;"

        Rules:

           ``;``
             terminates a sub-expression

           ``@``
             prefix to a temporary name, which is a double precision
             floating point number to be used later in the same
             expression.

           ``$``
             prefix to a local GX variable name.  Such names will be
             evaluated to the variable value at the time `create <geosoft.gxapi.GXEXP.create>`
             is called.

        All other tokens are assumed to be channel names.
        """
        ret_val = gxapi_cy.WrapEXP._create(GXContext._get_tls_geo(), db, formula.encode(), unused)
        return GXEXP(ret_val)



    @classmethod
    def create_file(cls, db, file):
        """
        This method creates an `GXEXP <geosoft.gxapi.GXEXP>` object from a file
        
        :param db:    Database Object
        :param file:  File name
        :type  db:    GXDB
        :type  file:  str

        :returns:     `GXEXP <geosoft.gxapi.GXEXP>` Object
        :rtype:       GXEXP

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapEXP._create_file(GXContext._get_tls_geo(), db, file.encode())
        return GXEXP(ret_val)







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer