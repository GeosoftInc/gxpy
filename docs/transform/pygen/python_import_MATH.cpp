#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMATH_wrap_cross_product_(double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9)
{
    GXMATH::cross_product_(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline int32_t GXMATH_wrap_abs_int_(int32_t arg1)
{
    int32_t ret = GXMATH::abs_int_(arg1);
    return ret;
}
inline int32_t GXMATH_wrap_and_(int32_t arg1, int32_t arg2)
{
    int32_t ret = GXMATH::and_(arg1, arg2);
    return ret;
}
inline int32_t GXMATH_wrap_mod_int_(int32_t arg1, int32_t arg2)
{
    int32_t ret = GXMATH::mod_int_(arg1, arg2);
    return ret;
}
inline int32_t GXMATH_wrap_or_(int32_t arg1, int32_t arg2)
{
    int32_t ret = GXMATH::or_(arg1, arg2);
    return ret;
}
inline int32_t GXMATH_wrap_round_int_(double arg1)
{
    int32_t ret = GXMATH::round_int_(arg1);
    return ret;
}
inline int32_t GXMATH_wrap_xor_(int32_t arg1, int32_t arg2)
{
    int32_t ret = GXMATH::xor_(arg1, arg2);
    return ret;
}
inline void GXMATH_wrap_nicer_log_scale_(float_ref& arg1, float_ref& arg2, int32_t arg3)
{
    GXMATH::nicer_log_scale_(arg1, arg2, arg3);
}
inline void GXMATH_wrap_nicer_scale_(float_ref& arg1, float_ref& arg2, float_ref& arg3, int_ref& arg4)
{
    GXMATH::nicer_scale_(arg1, arg2, arg3, arg4);
}
inline void GXMATH_wrap_normalise_3d_(float_ref& arg1, float_ref& arg2, float_ref& arg3)
{
    GXMATH::normalise_3d_(arg1, arg2, arg3);
}
inline double GXMATH_wrap_abs_double_(double arg1)
{
    double ret = GXMATH::abs_double_(arg1);
    return ret;
}
inline double GXMATH_wrap_arc_cos_(double arg1)
{
    double ret = GXMATH::arc_cos_(arg1);
    return ret;
}
inline double GXMATH_wrap_arc_sin_(double arg1)
{
    double ret = GXMATH::arc_sin_(arg1);
    return ret;
}
inline double GXMATH_wrap_arc_tan_(double arg1)
{
    double ret = GXMATH::arc_tan_(arg1);
    return ret;
}
inline double GXMATH_wrap_arc_tan2_(double arg1, double arg2)
{
    double ret = GXMATH::arc_tan2_(arg1, arg2);
    return ret;
}
inline double GXMATH_wrap_ceil_(double arg1)
{
    double ret = GXMATH::ceil_(arg1);
    return ret;
}
inline double GXMATH_wrap_cos_(double arg1)
{
    double ret = GXMATH::cos_(arg1);
    return ret;
}
inline double GXMATH_wrap_dot_product_3d_(double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    double ret = GXMATH::dot_product_3d_(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline double GXMATH_wrap_exp_(double arg1)
{
    double ret = GXMATH::exp_(arg1);
    return ret;
}
inline double GXMATH_wrap_floor_(double arg1)
{
    double ret = GXMATH::floor_(arg1);
    return ret;
}
inline double GXMATH_wrap_hypot_(double arg1, double arg2)
{
    double ret = GXMATH::hypot_(arg1, arg2);
    return ret;
}
inline double GXMATH_wrap_lambda_trans_(double arg1, double arg2)
{
    double ret = GXMATH::lambda_trans_(arg1, arg2);
    return ret;
}
inline double GXMATH_wrap_lambda_trans_rev_(double arg1, double arg2)
{
    double ret = GXMATH::lambda_trans_rev_(arg1, arg2);
    return ret;
}
inline double GXMATH_wrap_log_(double arg1)
{
    double ret = GXMATH::log_(arg1);
    return ret;
}
inline double GXMATH_wrap_log10_(double arg1)
{
    double ret = GXMATH::log10_(arg1);
    return ret;
}
inline double GXMATH_wrap_log_z_(double arg1, int32_t arg2, double arg3)
{
    double ret = GXMATH::log_z_(arg1, arg2, arg3);
    return ret;
}
inline double GXMATH_wrap_mod_double_(double arg1, double arg2)
{
    double ret = GXMATH::mod_double_(arg1, arg2);
    return ret;
}
inline void GXMATH_wrap_rotate_vector_(double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10)
{
    GXMATH::rotate_vector_(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline double GXMATH_wrap_pow_(double arg1, double arg2)
{
    double ret = GXMATH::pow_(arg1, arg2);
    return ret;
}
inline double GXMATH_wrap_rand_()
{
    double ret = GXMATH::rand_();
    return ret;
}
inline double GXMATH_wrap_round_double_(double arg1, int32_t arg2)
{
    double ret = GXMATH::round_double_(arg1, arg2);
    return ret;
}
inline double GXMATH_wrap_sign_(double arg1, double arg2)
{
    double ret = GXMATH::sign_(arg1, arg2);
    return ret;
}
inline double GXMATH_wrap_sin_(double arg1)
{
    double ret = GXMATH::sin_(arg1);
    return ret;
}
inline double GXMATH_wrap_sqrt_(double arg1)
{
    double ret = GXMATH::sqrt_(arg1);
    return ret;
}
inline double GXMATH_wrap_tan_(double arg1)
{
    double ret = GXMATH::tan_(arg1);
    return ret;
}
inline double GXMATH_wrap_un_log_z_(double arg1, int32_t arg2, double arg3)
{
    double ret = GXMATH::un_log_z_(arg1, arg2, arg3);
    return ret;
}
inline void GXMATH_wrap_s_rand_()
{
    GXMATH::s_rand_();
}

void gxPythonImportGXMATH()
{

    class_<GXMATH, boost::noncopyable> pyClass("GXMATH",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		This is not a class. This is a collection of standard\n"
            "   		mathematical functions, including most of the common\n"
            "   		logarithmic and geometric functions.\n"
            "   	\n\n"
            , no_init);


    pyClass.def("cross_product", &GXMATH_wrap_cross_product_,
                "cross_product((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Cross product of two vectors.\n\n"

                ":param arg1: X1 component\n"
                ":type arg1: float\n"
                ":param arg2: Y1 component\n"
                ":type arg2: float\n"
                ":param arg3: Z1 component\n"
                ":type arg3: float\n"
                ":param arg4: X2 component\n"
                ":type arg4: float\n"
                ":param arg5: Y2 component\n"
                ":type arg5: float\n"
                ":param arg6: Z2 component\n"
                ":type arg6: float\n"
                ":param arg7: X3 component (output)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Y3 component (output)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Z3 component (output)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("cross_product");
    pyClass.def("abs_int", &GXMATH_wrap_abs_int_,
                "abs_int((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate absolute value\n\n"

                ":param arg1: integer\n"
                ":type arg1: int\n"
                ":returns: integer\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("abs_int");
    pyClass.def("and", &GXMATH_wrap_and_,
                "and((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Return the unary operation result of A & B\n"
                "   \n"
                "   					Returns			an integer number\n"
                "   \n"
                "   					If A or B is a dummy, returns dummy.\n"
                "   				\n\n"

                ":param arg1: A\n"
                ":type arg1: int\n"
                ":param arg2: B\n"
                ":type arg2: int\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("and");
    pyClass.def("mod_int", &GXMATH_wrap_mod_int_,
                "mod_int((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates the modulus of two integers\n\n"

                ":param arg1: A\n"
                ":type arg1: int\n"
                ":param arg2: B (must not be zero)\n"
                ":type arg2: int\n"
                ":returns: int\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If A or B is a dummy, returns dummy.\n\n"
               ).staticmethod("mod_int");
    pyClass.def("or", &GXMATH_wrap_or_,
                "or((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Return the unary operation result of A \\ `|`\\  B\n"
                "   \n"
                "   					Returns			an integer number\n"
                "   \n"
                "   					If A or B is a dummy, returns dummy.\n"
                "   				\n\n"

                ":param arg1: A\n"
                ":type arg1: int\n"
                ":param arg2: B\n"
                ":type arg2: int\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("or");
    pyClass.def("round_int", &GXMATH_wrap_round_int_,
                "round_int((float)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Round to the nearest whole number\n\n"

                ":param arg1: round\n"
                ":type arg1: float\n"
                ":returns: integer\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Negative values with decimal parts larger than .5 round down (-1.5 -> 2.0)\n"
                "   					Positive values with decimal parts larger than .5 round up (1.5 -> 2.0)\n"
                "   					Dummy values return dummy\n"
                "   				\n\n"
               ).staticmethod("round_int");
    pyClass.def("xor", &GXMATH_wrap_xor_,
                "xor((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Return the unary operation result of A ^ B\n"
                "   \n"
                "   					Returns			an integer number\n"
                "   \n"
                "   					If A or B is a dummy, returns dummy.\n"
                "   				\n\n"

                ":param arg1: A\n"
                ":type arg1: int\n"
                ":param arg2: B\n"
                ":type arg2: int\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("xor");
    pyClass.def("nicer_log_scale", &GXMATH_wrap_nicer_log_scale_,
                "nicer_log_scale((float_ref)arg1, (float_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Finds nicer min, max values for logarithmic plot scales.\n\n"

                ":param arg1: Min value (changed)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Max value (changed)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Fine flag\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Will fail if the input upper bound is less than the lower\n"
                "   					bound, but will work if the two values are equal.\n"
                "   					The input bounds are overwritten.\n"
                "   \n"
                "   					Input lower and upper bounds, returns \"nicer\" values.\n"
                "   					If the Fine flag is set to TRUE, the values will have the\n"
                "   					form N x 10^Y, where N is a value from 1 to 9, and 10^Y\n"
                "   					is an integral power of 10. If the Fine flag is set to\n"
                "   					FALSE, the scaling is coarse, and the bounding exact\n"
                "   					powers of 10 are returned.\n"
                "   					For example,  the values (.034, 23) return (.03, 30) for\n"
                "   					fine scaling, and (0.01, 100) for coarse scaling.\n"
                "   				\n\n"
               ).staticmethod("nicer_log_scale");
    pyClass.def("nicer_scale", &GXMATH_wrap_nicer_scale_,
                "nicer_scale((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute a nicer scale for a given min and max.\n\n"

                ":param arg1: Min value (changed)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Max value (changed)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Inc value (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Power value (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("nicer_scale");
    pyClass.def("normalise_3d", &GXMATH_wrap_normalise_3d_,
                "normalise_3d((float_ref)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scale a vector to unit length.\n\n"

                ":param arg1: X component (altered)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y component (altered)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z component (altered)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Divides each component by the vector\n"
                "   					magnitude.\n"
                "   				\n\n"
               ).staticmethod("normalise_3d");
    pyClass.def("abs_double", &GXMATH_wrap_abs_double_,
                "abs_double((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate absolute value\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("abs_double");
    pyClass.def("arc_cos", &GXMATH_wrap_arc_cos_,
                "arc_cos((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the arccosine\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values or values < -1 or > 1 return dummy\n\n"
               ).staticmethod("arc_cos");
    pyClass.def("arc_sin", &GXMATH_wrap_arc_sin_,
                "arc_sin((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the arcsin\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values or values < -1 or > 1 return dummy\n\n"
               ).staticmethod("arc_sin");
    pyClass.def("arc_tan", &GXMATH_wrap_arc_tan_,
                "arc_tan((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the arctan\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("arc_tan");
    pyClass.def("arc_tan2", &GXMATH_wrap_arc_tan2_,
                "arc_tan2((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate ArcTan(Y/X)\n\n"

                ":param arg1: Y\n"
                ":type arg1: float\n"
                ":param arg2: X\n"
                ":type arg2: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If either X or Y is a dummy, returns dummy\n\n"
               ).staticmethod("arc_tan2");
    pyClass.def("ceil", &GXMATH_wrap_ceil_,
                "ceil((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates the ceiling of the value\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("ceil");
    pyClass.def("cos", &GXMATH_wrap_cos_,
                "cos((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the cosine\n\n"

                ":param arg1: Angle in radians\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("cos");
    pyClass.def("dot_product_3d", &GXMATH_wrap_dot_product_3d_,
                "dot_product_3d((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute Dot product of two vectors.\n\n"

                ":param arg1: X1 component\n"
                ":type arg1: float\n"
                ":param arg2: Y1 component\n"
                ":type arg2: float\n"
                ":param arg3: Z1 component\n"
                ":type arg3: float\n"
                ":param arg4: X2 component\n"
                ":type arg4: float\n"
                ":param arg5: Y2 component\n"
                ":type arg5: float\n"
                ":param arg6: Z2 component\n"
                ":type arg6: float\n"
                ":returns: Dot product\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("dot_product_3d");
    pyClass.def("exp", &GXMATH_wrap_exp_,
                "exp((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate e raised to the power of X\n\n"

                ":param arg1: X\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("exp");
    pyClass.def("floor", &GXMATH_wrap_floor_,
                "floor((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates the floor of the value\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("floor");
    pyClass.def("hypot", &GXMATH_wrap_hypot_,
                "hypot((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   sqrt(X\\ `*`\\ X + Y\\ `*`\\ Y)\n\n"

                ":param arg1: X\n"
                ":type arg1: float\n"
                ":param arg2: Y\n"
                ":type arg2: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If either X or Y is a dummy, the returned value is dummy\n\n"
               ).staticmethod("hypot");
    pyClass.def("lambda_trans", &GXMATH_wrap_lambda_trans_,
                "lambda_trans((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Performs lambda transform on a value.\n\n"

                ":param arg1: Z Value\n"
                ":type arg1: float\n"
                ":param arg2: Lambda value\n"
                ":type arg2: float\n"
                ":returns: The lambda transformed value\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns 0 for input Z = 0.\n"
                "   					returns log10(Z) for lambda = 0.\n"
                "   					returns (Z^lambda - 1)/lambda for Z > 0.\n"
                "   					returns dummy for Z = dummy.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMATH.lambda_trans_rev`\\ \n\n"
               ).staticmethod("lambda_trans");
    pyClass.def("lambda_trans_rev", &GXMATH_wrap_lambda_trans_rev_,
                "lambda_trans_rev((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Performs a reverse lambda transform on a value.\n\n"

                ":param arg1: Lambda transformed Z Value\n"
                ":type arg1: float\n"
                ":param arg2: Lambda value\n"
                ":type arg2: float\n"
                ":returns: The original non-lambda transformed value\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See rLambdaTrans.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMATH.lambda_trans`\\ \n\n"
               ).staticmethod("lambda_trans_rev");
    pyClass.def("log", &GXMATH_wrap_log_,
                "log((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the natural log\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("log");
    pyClass.def("log10", &GXMATH_wrap_log10_,
                "log10((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the base 10 log\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("log10");
    pyClass.def("log_z", &GXMATH_wrap_log_z_,
                "log_z((float)arg1, (int)arg2, (float)arg3) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Given a Z value and the Log style and Log Minimum this\n"
                "   					function will return the log value.\n"
                "   				\n\n"

                ":param arg1: Z Value\n"
                ":type arg1: float\n"
                ":param arg2: Log Mode (0 - Log, 1 - LogLinearLog)\n"
                ":type arg2: int\n"
                ":param arg3: Log Minimum (must be greater than 0)\n"
                ":type arg3: float\n"
                ":returns: The Log Value.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Mode = 0 (regular log mode)\n"
                "   \n"
                "   					Returns:\n"
                "   					Log10(Z)  for Z > minimum\n"
                "   					Log10(minimum) for Z <= minimum\n"
                "   \n"
                "   					Mode = 1 (log / linear / negative log mode)\n"
                "   \n"
                "   					Returns:\n"
                "   					minimum \\ `*`\\  ( log10( \\ `|`\\ Z\\ `|`\\  / minimum) + 1 )   for Z > minimum\n"
                "   					Z for \\ `|`\\ Z\\ `|`\\  <= minimum   (the linear part of the range)\n"
                "   					-minimum \\ `*`\\  ( log10( \\ `|`\\ Z\\ `|`\\  / minimum) + 1 )   for Z < -minimum\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMATH.un_log_z`\\ \n\n"
               ).staticmethod("log_z");
    pyClass.def("mod_double", &GXMATH_wrap_mod_double_,
                "mod_double((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates the modulus of two reals (A mod B)\n\n"

                ":param arg1: A\n"
                ":type arg1: float\n"
                ":param arg2: B (must not be zero)\n"
                ":type arg2: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The modulus of A with respect to B is defined\n"
                "   					as the difference of A with the largest integral multiple of B\n"
                "   					smaller than or equal to A.\n"
                "   \n"
                "   					e.g.   A  mod B\n"
                "   					20 mod 10 = 0\n"
                "   					20 mod 9 = 2\n"
                "   \n"
                "   					f A or B is a dummy, returns dummy.\n"
                "   				\n\n"
               ).staticmethod("mod_double");
    pyClass.def("rotate_vector", &GXMATH_wrap_rotate_vector_,
                "rotate_vector((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Rotate a vector about an axis.\n\n"

                ":param arg1: X1 component (vector to rotate)\n"
                ":type arg1: float\n"
                ":param arg2: Y1 component\n"
                ":type arg2: float\n"
                ":param arg3: Z1 component\n"
                ":type arg3: float\n"
                ":param arg4: Angle to rotate, CW in radians\n"
                ":type arg4: float\n"
                ":param arg5: X2 component (axis of rotation)\n"
                ":type arg5: float\n"
                ":param arg6: Y2 component\n"
                ":type arg6: float\n"
                ":param arg7: Z2 component\n"
                ":type arg7: float\n"
                ":param arg8: X3 component  (rotated vector, can\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Y3 component   be the same as input)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Z3 component\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Rotates a vector by the input angle around an arbitrary axis.\n"
                "   					Angles are measured clockwise looking along the axis (away from the origin).\n"
                "   					Assumes a right hand coordinate system.\n"
                "   				\n\n"
               ).staticmethod("rotate_vector");
    pyClass.def("pow", &GXMATH_wrap_pow_,
                "pow((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate X raised to the power of Y\n\n"

                ":param arg1: X\n"
                ":type arg1: float\n"
                ":param arg2: Y\n"
                ":type arg2: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If either X or Y is a dummy, returns dummy\n\n"
               ).staticmethod("pow");
    pyClass.def("rand", &GXMATH_wrap_rand_,
                "rand() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a  random number between 0 and 1\n\n"

                ":returns: a real number\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use \\ :func:`geosoft.gxapi.GXMATH.s_rand`\\  to seed the random number generator before a series of\n"
                "   					calls to this function are made.\n"
                "   					The standard \"C\" function rand() is called.\n"
                "   				\n\n"
               ).staticmethod("rand");
    pyClass.def("round_double", &GXMATH_wrap_round_double_,
                "round_double((float)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Round to n significant digits\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":param arg2: number of significant digits to round to\n"
                ":type arg2: int\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Negative values ending in 5XXX to n sig digits round down\n"
                "   					Positive values ending in 5XXX to n sig digits round up\n"
                "   					Dummy values return dummy\n"
                "   				\n\n"
               ).staticmethod("round_double");
    pyClass.def("sign", &GXMATH_wrap_sign_,
                "sign((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Determine return value based on value of Z1\n\n"

                ":param arg1: Z1\n"
                ":type arg1: float\n"
                ":param arg2: Z2\n"
                ":type arg2: float\n"
                ":returns: \\ `|`\\ Z2\\ `|`\\  if Z1>0, -\\ `|`\\ Z2\\ `|`\\  if Z1<0, 0 if Z1 = 0, and Z2 if Z1 = Dummy\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("sign");
    pyClass.def("sin", &GXMATH_wrap_sin_,
                "sin((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the sin\n\n"

                ":param arg1: Angle in radians\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("sin");
    pyClass.def("sqrt", &GXMATH_wrap_sqrt_,
                "sqrt((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the square root\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("sqrt");
    pyClass.def("tan", &GXMATH_wrap_tan_,
                "tan((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the tangent\n\n"

                ":param arg1: Angle in radians\n"
                ":type arg1: float\n"
                ":returns: real\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values return dummy\n\n"
               ).staticmethod("tan");
    pyClass.def("un_log_z", &GXMATH_wrap_un_log_z_,
                "un_log_z((float)arg1, (int)arg2, (float)arg3) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Inverse of rLogZ\n\n"

                ":param arg1: log value\n"
                ":type arg1: float\n"
                ":param arg2: Log Mode (0 - Log, 1 - LogLinearLog)\n"
                ":type arg2: int\n"
                ":param arg3: Log Minimum (must be greater than 0)\n"
                ":type arg3: float\n"
                ":returns: The original value\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See Notes for rLogZ.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMATH.log_z`\\ \n\n"
               ).staticmethod("un_log_z");
    pyClass.def("s_rand", &GXMATH_wrap_s_rand_,
                "s_rand() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Seed the random-number generator with current time\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use the \\ :func:`geosoft.gxapi.GXMATH.rand`\\  function to create a random number between  0 and 1.\n"
                "   					The standard \"C\" function srand() is called.\n"
                "   				\n\n"
               ).staticmethod("s_rand");


}
