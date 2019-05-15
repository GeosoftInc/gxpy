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
class GXMATH(gxapi_cy.WrapMATH):
    """
    GXMATH class.

    This is not a class. This is a collection of standard
    mathematical functions, including most of the common
    logarithmic and geometric functions.
    """

    def __init__(self, handle=0):
        super(GXMATH, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMATH <geosoft.gxapi.GXMATH>`
        
        :returns: A null `GXMATH <geosoft.gxapi.GXMATH>`
        :rtype:   GXMATH
        """
        return GXMATH()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def cross_product_(cls, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        """
        Cross product of two vectors.
        
        :param x1:  X1 component
        :param y1:  Y1 component
        :param z1:  Z1 component
        :param x2:  X2 component
        :param y2:  Y2 component
        :param z2:  Z2 component
        :param x3:  X3 component (output)
        :param y3:  Y3 component (output)
        :param z3:  Z3 component (output)
        :type  x1:  float
        :type  y1:  float
        :type  z1:  float
        :type  x2:  float
        :type  y2:  float
        :type  z2:  float
        :type  x3:  float_ref
        :type  y3:  float_ref
        :type  z3:  float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x3.value, y3.value, z3.value = gxapi_cy.WrapMATH._cross_product_(GXContext._get_tls_geo(), x1, y1, z1, x2, y2, z2, x3.value, y3.value, z3.value)
        



    @classmethod
    def abs_int_(cls, n):
        """
        Calculate absolute value
        
        :param n:  Integer
        :type  n:  int

        :returns:    Integer
        :rtype:      int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._abs_int_(GXContext._get_tls_geo(), n)
        return ret_val



    @classmethod
    def and_(cls, pi_val1, pi_val2):
        """
        Return the unary operation result of A & B

        Returns			an integer number

        If A or B is a dummy, returns dummy.
        
        :param pi_val1:  A
        :param pi_val2:  B
        :type  pi_val1:  int
        :type  pi_val2:  int
        :rtype:          int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMATH._and_(GXContext._get_tls_geo(), pi_val1, pi_val2)
        return ret_val



    @classmethod
    def mod_int_(cls, a, b):
        """
        Calculates the modulus of two integers
        
        :param a:  A
        :param b:  B (must not be zero)
        :type  a:  int
        :type  b:  int

        :returns:    Int
        :rtype:      int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If A or B is a dummy, returns dummy.
        """
        ret_val = gxapi_cy.WrapMATH._mod_int_(GXContext._get_tls_geo(), a, b)
        return ret_val



    @classmethod
    def or_(cls, pi_val1, pi_val2):
        """
        Return the unary operation result of A | B

        Returns			an integer number

        If A or B is a dummy, returns dummy.
        
        :param pi_val1:  A
        :param pi_val2:  B
        :type  pi_val1:  int
        :type  pi_val2:  int
        :rtype:          int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMATH._or_(GXContext._get_tls_geo(), pi_val1, pi_val2)
        return ret_val



    @classmethod
    def round_int_(cls, z):
        """
        Round to the nearest whole number
        
        :param z:  Round
        :type  z:  float

        :returns:    Integer
        :rtype:      int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Negative values with decimal parts larger than .5 round down (-1.5 -> 2.0)
        Positive values with decimal parts larger than .5 round up (1.5 -> 2.0)
        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._round_int_(GXContext._get_tls_geo(), z)
        return ret_val



    @classmethod
    def xor_(cls, pi_val1, pi_val2):
        """
        Return the unary operation result of A ^ B

        Returns			an integer number

        If A or B is a dummy, returns dummy.
        
        :param pi_val1:  A
        :param pi_val2:  B
        :type  pi_val1:  int
        :type  pi_val2:  int
        :rtype:          int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMATH._xor_(GXContext._get_tls_geo(), pi_val1, pi_val2)
        return ret_val



    @classmethod
    def nicer_log_scale_(cls, min, max, fine):
        """
        Finds nicer min, max values for logarithmic plot scales.
        
        :param min:   Min value (changed)
        :param max:   Max value (changed)
        :param fine:  Fine flag
        :type  min:   float_ref
        :type  max:   float_ref
        :type  fine:  int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Will fail if the input upper bound is less than the lower
        bound, but will work if the two values are equal.
        The input bounds are overwritten.

        Input lower and upper bounds, returns "nicer" values.
        If the Fine flag is set to TRUE, the values will have the
        form N x 10^Y, where N is a value from 1 to 9, and 10^Y
        is an integral power of 10. If the Fine flag is set to
        FALSE, the scaling is coarse, and the bounding exact
        powers of 10 are returned.
        For example,  the values (.034, 23) return (.03, 30) for
        fine scaling, and (0.01, 100) for coarse scaling.
        """
        min.value, max.value = gxapi_cy.WrapMATH._nicer_log_scale_(GXContext._get_tls_geo(), min.value, max.value, fine)
        



    @classmethod
    def nicer_scale_(cls, min, max, inc, pow):
        """
        Compute a nicer scale for a given min and max.
        
        :param min:  Min value (changed)
        :param max:  Max value (changed)
        :param inc:  Inc value (returned)
        :param pow:  Power value (returned)
        :type  min:  float_ref
        :type  max:  float_ref
        :type  inc:  float_ref
        :type  pow:  int_ref

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min.value, max.value, inc.value, pow.value = gxapi_cy.WrapMATH._nicer_scale_(GXContext._get_tls_geo(), min.value, max.value, inc.value, pow.value)
        



    @classmethod
    def normalise_3d_(cls, x, y, z):
        """
        Scale a vector to unit length.
        
        :param x:  X component (altered)
        :param y:  Y component (altered)
        :param z:  Z component (altered)
        :type  x:  float_ref
        :type  y:  float_ref
        :type  z:  float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Divides each component by the vector
        magnitude.
        """
        x.value, y.value, z.value = gxapi_cy.WrapMATH._normalise_3d_(GXContext._get_tls_geo(), x.value, y.value, z.value)
        



    @classmethod
    def abs_double_(cls, z):
        """
        Calculate absolute value
        
        :param z:  Real
        :type  z:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._abs_double_(GXContext._get_tls_geo(), z)
        return ret_val



    @classmethod
    def arc_cos_(cls, val):
        """
        Calculate the arccosine
        
        :param val:  Real
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values or values < -1 or > 1 return dummy
        """
        ret_val = gxapi_cy.WrapMATH._arc_cos_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def arc_sin_(cls, val):
        """
        Calculate the arcsin
        
        :param val:  Real
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values or values < -1 or > 1 return dummy
        """
        ret_val = gxapi_cy.WrapMATH._arc_sin_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def arc_tan_(cls, val):
        """
        Calculate the arctan
        
        :param val:  Real
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._arc_tan_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def arc_tan2_(cls, y, x):
        """
        Calculate ArcTan(Y/X)
        
        :param y:  Y
        :param x:  X
        :type  y:  float
        :type  x:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If either X or Y is a dummy, returns dummy
        """
        ret_val = gxapi_cy.WrapMATH._arc_tan2_(GXContext._get_tls_geo(), y, x)
        return ret_val



    @classmethod
    def ceil_(cls, z):
        """
        Calculates the ceiling of the value
        
        :param z:  Real
        :type  z:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._ceil_(GXContext._get_tls_geo(), z)
        return ret_val



    @classmethod
    def cos_(cls, val):
        """
        Calculate the cosine
        
        :param val:  Angle in radians
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._cos_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def dot_product_3d_(cls, x1, y1, z1, x2, y2, z2):
        """
        Compute Dot product of two vectors.
        
        :param x1:  X1 component
        :param y1:  Y1 component
        :param z1:  Z1 component
        :param x2:  X2 component
        :param y2:  Y2 component
        :param z2:  Z2 component
        :type  x1:  float
        :type  y1:  float
        :type  z1:  float
        :type  x2:  float
        :type  y2:  float
        :type  z2:  float

        :returns:    Dot product
        :rtype:      float

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMATH._dot_product_3d_(GXContext._get_tls_geo(), x1, y1, z1, x2, y2, z2)
        return ret_val



    @classmethod
    def exp_(cls, val):
        """
        Calculate e raised to the power of X
        
        :param val:  X
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._exp_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def floor_(cls, z):
        """
        Calculates the floor of the value
        
        :param z:  Real
        :type  z:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._floor_(GXContext._get_tls_geo(), z)
        return ret_val



    @classmethod
    def hypot_(cls, x, y):
        """
        sqrt(X*X + Y*Y)
        
        :param x:  X
        :param y:  Y
        :type  x:  float
        :type  y:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If either X or Y is a dummy, the returned value is dummy
        """
        ret_val = gxapi_cy.WrapMATH._hypot_(GXContext._get_tls_geo(), x, y)
        return ret_val



    @classmethod
    def lambda_trans_(cls, z, lda):
        """
        Performs lambda transform on a value.
        
        :param z:    Z Value
        :param lda:  Lambda value
        :type  z:    float
        :type  lda:  float

        :returns:    The lambda transformed value
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns 0 for input Z = 0.
        returns log10(Z) for lambda = 0.
        returns (Z^lambda - 1)/lambda for Z > 0.
        returns dummy for Z = dummy.

        .. seealso::

            `lambda_trans_rev_ <geosoft.gxapi.GXMATH.lambda_trans_rev_>`
        """
        ret_val = gxapi_cy.WrapMATH._lambda_trans_(GXContext._get_tls_geo(), z, lda)
        return ret_val



    @classmethod
    def lambda_trans_rev_(cls, z, lda):
        """
        Performs a reverse lambda transform on a value.
        
        :param z:    Lambda transformed Z Value
        :param lda:  Lambda value
        :type  z:    float
        :type  lda:  float

        :returns:    The original non-lambda transformed value
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See rLambdaTrans.

        .. seealso::

            `lambda_trans_ <geosoft.gxapi.GXMATH.lambda_trans_>`
        """
        ret_val = gxapi_cy.WrapMATH._lambda_trans_rev_(GXContext._get_tls_geo(), z, lda)
        return ret_val



    @classmethod
    def log_(cls, val):
        """
        Calculate the natural log
        
        :param val:  Real
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._log_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def log10_(cls, val):
        """
        Calculate the base 10 log
        
        :param val:  Real
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._log10_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def log_z_(cls, z, mode, min):
        """
        Given a Z value and the Log style and Log Minimum this
        function will return the log value.
        
        :param z:     Z Value
        :param mode:  Log Mode (0 - Log, 1 - LogLinearLog)
        :param min:   Log Minimum (must be greater than 0)
        :type  z:     float
        :type  mode:  int
        :type  min:   float

        :returns:     The Log Value.
        :rtype:       float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Mode = 0 (regular log mode) returns:

        ::

            Log10(Z)  for Z > minimum
            Log10(minimum) for Z <= minimum


        Mode = 1 (log / linear / negative log mode) returns:

        ::

            minimum * ( log10( |Z| / minimum) + 1 )   for Z > minimum
            Z for |Z| <= minimum   (the linear part of the range)
            -minimum * ( log10( |Z| / minimum) + 1 )   for Z < -minimum

        .. seealso::

            `un_log_z_ <geosoft.gxapi.GXMATH.un_log_z_>`
        """
        ret_val = gxapi_cy.WrapMATH._log_z_(GXContext._get_tls_geo(), z, mode, min)
        return ret_val



    @classmethod
    def mod_double_(cls, a, b):
        """
        Calculates the modulus of two reals (A mod B)
        
        :param a:  A
        :param b:  B (must not be zero)
        :type  a:  float
        :type  b:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The modulus of A with respect to B is defined
        as the difference of A with the largest integral multiple of B
        smaller than or equal to A.

        e.g.   A  mod B
        20 mod 10 = 0
        20 mod 9 = 2

        f A or B is a dummy, returns dummy.
        """
        ret_val = gxapi_cy.WrapMATH._mod_double_(GXContext._get_tls_geo(), a, b)
        return ret_val



    @classmethod
    def rotate_vector_(cls, x1, y1, z1, angle, x2, y2, z2, x3, y3, z3):
        """
        Rotate a vector about an axis.
        
        :param x1:     X1 component (vector to rotate)
        :param y1:     Y1 component
        :param z1:     Z1 component
        :param angle:  Angle to rotate, CW in radians
        :param x2:     X2 component (axis of rotation)
        :param y2:     Y2 component
        :param z2:     Z2 component
        :param x3:     X3 component  (rotated vector, can
        :param y3:     Y3 component   be the same as input)
        :param z3:     Z3 component
        :type  x1:     float
        :type  y1:     float
        :type  z1:     float
        :type  angle:  float
        :type  x2:     float
        :type  y2:     float
        :type  z2:     float
        :type  x3:     float_ref
        :type  y3:     float_ref
        :type  z3:     float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Rotates a vector by the input angle around an arbitrary axis.
        Angles are measured clockwise looking along the axis (away from the origin).
        Assumes a right hand coordinate system.
        """
        x3.value, y3.value, z3.value = gxapi_cy.WrapMATH._rotate_vector_(GXContext._get_tls_geo(), x1, y1, z1, angle, x2, y2, z2, x3.value, y3.value, z3.value)
        



    @classmethod
    def pow_(cls, x, y):
        """
        Calculate X raised to the power of Y
        
        :param x:  X
        :param y:  Y
        :type  x:  float
        :type  y:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If either X or Y is a dummy, returns dummy
        """
        ret_val = gxapi_cy.WrapMATH._pow_(GXContext._get_tls_geo(), x, y)
        return ret_val



    @classmethod
    def rand_(cls):
        """
        Get a  random number between 0 and 1
        

        :returns:    A real number
        :rtype:      float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use `s_rand_ <geosoft.gxapi.GXMATH.s_rand_>` to seed the random number generator before a series of
        calls to this function are made.
        The standard "C" function rand() is called.
        """
        ret_val = gxapi_cy.WrapMATH._rand_(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def round_double_(cls, z, n):
        """
        Round to n significant digits
        
        :param z:  Real
        :param n:  Number of significant digits to round to
        :type  z:  float
        :type  n:  int

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Negative values ending in 5XXX to n sig digits round down
        Positive values ending in 5XXX to n sig digits round up
        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._round_double_(GXContext._get_tls_geo(), z, n)
        return ret_val



    @classmethod
    def sign_(cls, z_sign, z_val):
        """
        Determine return value based on value of Z1
        
        :param z_sign:  Z1
        :param z_val:   Z2
        :type  z_sign:  float
        :type  z_val:   float

        :returns:       ``|Z2| if Z1 > 0, -|Z2| if Z1 < 0, 0 if Z1 = 0, and Z2 if Z1 = Dummy``
        :rtype:         float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._sign_(GXContext._get_tls_geo(), z_sign, z_val)
        return ret_val



    @classmethod
    def sin_(cls, val):
        """
        Calculate the sin
        
        :param val:  Angle in radians
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._sin_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def sqrt_(cls, val):
        """
        Calculate the square root
        
        :param val:  Real
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._sqrt_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def tan_(cls, val):
        """
        Calculate the tangent
        
        :param val:  Angle in radians
        :type  val:  float

        :returns:    Real
        :rtype:      float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH._tan_(GXContext._get_tls_geo(), val)
        return ret_val



    @classmethod
    def un_log_z_(cls, z, mode, min):
        """
        Inverse of rLogZ
        
        :param z:     Log value
        :param mode:  Log Mode (0 - Log, 1 - LogLinearLog)
        :param min:   Log Minimum (must be greater than 0)
        :type  z:     float
        :type  mode:  int
        :type  min:   float

        :returns:     The original value
        :rtype:       float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See Notes for rLogZ.

        .. seealso::

            `log_z_ <geosoft.gxapi.GXMATH.log_z_>`
        """
        ret_val = gxapi_cy.WrapMATH._un_log_z_(GXContext._get_tls_geo(), z, mode, min)
        return ret_val



    @classmethod
    def s_rand_(cls):
        """
        Seed the random-number generator with current time
        

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use the `rand_ <geosoft.gxapi.GXMATH.rand_>` function to create a random number between  0 and 1.
        The standard "C" function srand() is called.
        """
        gxapi_cy.WrapMATH._s_rand_(GXContext._get_tls_geo())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer