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
class GXMATH:
    """
    GXMATH class.

    This is not a class. This is a collection of standard
    mathematical functions, including most of the common
    logarithmic and geometric functions.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMATH(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXMATH`
        
        :returns: A null :class:`geosoft.gxapi.GXMATH`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMATH` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMATH`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def cross_product_(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Cross product of two vectors.
        """
        p7.value, p8.value, p9.value = gxapi_cy.WrapMATH.cross_product_(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7.value, p8.value, p9.value)
        



    @classmethod
    def abs_int_(cls, p1):
        """
        Calculate absolute value

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.abs_int_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def and_(cls, p1, p2):
        """
        Return the unary operation result of A & B
        
        Returns			an integer number
        
        If A or B is a dummy, returns dummy.
        """
        ret_val = gxapi_cy.WrapMATH.and_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def mod_int_(cls, p1, p2):
        """
        Calculates the modulus of two integers

        **Note:**

        If A or B is a dummy, returns dummy.
        """
        ret_val = gxapi_cy.WrapMATH.mod_int_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def or_(cls, p1, p2):
        """
        Return the unary operation result of A | B
        
        Returns			an integer number
        
        If A or B is a dummy, returns dummy.
        """
        ret_val = gxapi_cy.WrapMATH.or_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def round_int_(cls, p1):
        """
        Round to the nearest whole number

        **Note:**

        Negative values with decimal parts larger than .5 round down (-1.5 -> 2.0)
        Positive values with decimal parts larger than .5 round up (1.5 -> 2.0)
        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.round_int_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def xor_(cls, p1, p2):
        """
        Return the unary operation result of A ^ B
        
        Returns			an integer number
        
        If A or B is a dummy, returns dummy.
        """
        ret_val = gxapi_cy.WrapMATH.xor_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def nicer_log_scale_(cls, p1, p2, p3):
        """
        Finds nicer min, max values for logarithmic plot scales.

        **Note:**

        Will fail if the input upper bound is less than the lower
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
        p1.value, p2.value = gxapi_cy.WrapMATH.nicer_log_scale_(GXContext._get_tls_geo(), p1.value, p2.value, p3)
        



    @classmethod
    def nicer_scale_(cls, p1, p2, p3, p4):
        """
        Compute a nicer scale for a given min and max.
        """
        p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapMATH.nicer_scale_(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value)
        



    @classmethod
    def normalise_3d_(cls, p1, p2, p3):
        """
        Scale a vector to unit length.

        **Note:**

        Divides each component by the vector
        magnitude.
        """
        p1.value, p2.value, p3.value = gxapi_cy.WrapMATH.normalise_3d_(GXContext._get_tls_geo(), p1.value, p2.value, p3.value)
        



    @classmethod
    def abs_double_(cls, p1):
        """
        Calculate absolute value

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.abs_double_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_cos_(cls, p1):
        """
        Calculate the arccosine

        **Note:**

        Dummy values or values < -1 or > 1 return dummy
        """
        ret_val = gxapi_cy.WrapMATH.arc_cos_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_sin_(cls, p1):
        """
        Calculate the arcsin

        **Note:**

        Dummy values or values < -1 or > 1 return dummy
        """
        ret_val = gxapi_cy.WrapMATH.arc_sin_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_tan_(cls, p1):
        """
        Calculate the arctan

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.arc_tan_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_tan2_(cls, p1, p2):
        """
        Calculate ArcTan(Y/X)

        **Note:**

        If either X or Y is a dummy, returns dummy
        """
        ret_val = gxapi_cy.WrapMATH.arc_tan2_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def ceil_(cls, p1):
        """
        Calculates the ceiling of the value

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.ceil_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def cos_(cls, p1):
        """
        Calculate the cosine

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.cos_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def dot_product_3d_(cls, p1, p2, p3, p4, p5, p6):
        """
        Compute Dot product of two vectors.
        """
        ret_val = gxapi_cy.WrapMATH.dot_product_3d_(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6)
        return ret_val



    @classmethod
    def exp_(cls, p1):
        """
        Calculate e raised to the power of X

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.exp_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def floor_(cls, p1):
        """
        Calculates the floor of the value

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.floor_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def hypot_(cls, p1, p2):
        """
        sqrt(X*X + Y*Y)

        **Note:**

        If either X or Y is a dummy, the returned value is dummy
        """
        ret_val = gxapi_cy.WrapMATH.hypot_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def lambda_trans_(cls, p1, p2):
        """
        Performs lambda transform on a value.

        **Note:**

        Returns 0 for input Z = 0.
        returns log10(Z) for lambda = 0.
        returns (Z^lambda - 1)/lambda for Z > 0.
        returns dummy for Z = dummy.
        """
        ret_val = gxapi_cy.WrapMATH.lambda_trans_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def lambda_trans_rev_(cls, p1, p2):
        """
        Performs a reverse lambda transform on a value.

        **Note:**

        See rLambdaTrans.
        """
        ret_val = gxapi_cy.WrapMATH.lambda_trans_rev_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def log_(cls, p1):
        """
        Calculate the natural log

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.log_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def log10_(cls, p1):
        """
        Calculate the base 10 log

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.log10_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def log_z_(cls, p1, p2, p3):
        """
        Given a Z value and the Log style and Log Minimum this
        function will return the log value.

        **Note:**

        Mode = 0 (regular log mode)
        
        Returns:
        Log10(Z)  for Z > minimum
        Log10(minimum) for Z <= minimum
        
        Mode = 1 (log / linear / negative log mode)
        
        Returns:
        minimum * ( log10( |Z| / minimum) + 1 )   for Z > minimum
        Z for |Z| <= minimum   (the linear part of the range)
        -minimum * ( log10( |Z| / minimum) + 1 )   for Z < -minimum
        """
        ret_val = gxapi_cy.WrapMATH.log_z_(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def mod_double_(cls, p1, p2):
        """
        Calculates the modulus of two reals (A mod B)

        **Note:**

        The modulus of A with respect to B is defined
        as the difference of A with the largest integral multiple of B
        smaller than or equal to A.
        
        e.g.   A  mod B
        20 mod 10 = 0
        20 mod 9 = 2
        
        f A or B is a dummy, returns dummy.
        """
        ret_val = gxapi_cy.WrapMATH.mod_double_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def rotate_vector_(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Rotate a vector about an axis.

        **Note:**

        Rotates a vector by the input angle around an arbitrary axis.
        Angles are measured clockwise looking along the axis (away from the origin).
        Assumes a right hand coordinate system.
        """
        p8.value, p9.value, p10.value = gxapi_cy.WrapMATH.rotate_vector_(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7, p8.value, p9.value, p10.value)
        



    @classmethod
    def pow_(cls, p1, p2):
        """
        Calculate X raised to the power of Y

        **Note:**

        If either X or Y is a dummy, returns dummy
        """
        ret_val = gxapi_cy.WrapMATH.pow_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def rand_(cls):
        """
        Get a  random number between 0 and 1

        **Note:**

        Use SRand_MATH to seed the random number generator before a series of
        calls to this function are made.
        The standard "C" function rand() is called.
        """
        ret_val = gxapi_cy.WrapMATH.rand_(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def round_double_(cls, p1, p2):
        """
        Round to n significant digits

        **Note:**

        Negative values ending in 5XXX to n sig digits round down
        Positive values ending in 5XXX to n sig digits round up
        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.round_double_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def sign_(cls, p1, p2):
        """
        Determine return value based on value of Z1

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.sign_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def sin_(cls, p1):
        """
        Calculate the sin

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.sin_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def sqrt_(cls, p1):
        """
        Calculate the square root

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.sqrt_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def tan_(cls, p1):
        """
        Calculate the tangent

        **Note:**

        Dummy values return dummy
        """
        ret_val = gxapi_cy.WrapMATH.tan_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def un_log_z_(cls, p1, p2, p3):
        """
        Inverse of rLogZ

        **Note:**

        See Notes for rLogZ.
        """
        ret_val = gxapi_cy.WrapMATH.un_log_z_(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def s_rand_(cls):
        """
        Seed the random-number generator with current time

        **Note:**

        Use the rRand_MATH function to create a random number between  0 and 1.
        The standard "C" function srand() is called.
        """
        gxapi_cy.WrapMATH.s_rand_(GXContext._get_tls_geo())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer