#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXTEST_wrap_enable_disable_arc_engine_license(bool arg1)
{
    GXTEST::enable_disable_arc_engine_license(arg1);
}
inline int32_t GXTEST_wrap_arc_engine_license()
{
    int32_t ret = GXTEST::arc_engine_license();
    return ret;
}
inline bool GXTEST_wrap_test_mode()
{
    bool ret = GXTEST::test_mode();
    return ret;
}
inline void GXTEST_wrap_wrapper_test(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXTEST::wrapper_test(arg1, arg2);
}
inline void GXTEST_wrap_core_class(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXTEST::core_class(arg1, arg2);
}

void gxPythonImportGXTEST()
{

    class_<GXTEST, boost::noncopyable> pyClass("GXTEST",
            "\n.. parsed-literal::\n\n"
            "   Used to place special testing methods\n\n"
            , no_init);


    pyClass.def("enable_disable_arc_engine_license", &GXTEST_wrap_enable_disable_arc_engine_license,
                "enable_disable_arc_engine_license((bool)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Forcefully disable ArEngine license availability for testing purposes\n\n"

                ":param arg1: Enable/disable? bool\n"
                ":type arg1: bool\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"
               ).staticmethod("enable_disable_arc_engine_license");
    pyClass.def("arc_engine_license", &GXTEST_wrap_arc_engine_license,
                "arc_engine_license() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Test availability of an ArEngine license on this system\n\n"

                ":returns: 0 - Not available, 1 - Available\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("arc_engine_license");
    pyClass.def("test_mode", &GXTEST_wrap_test_mode,
                "test_mode() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks to see if we are running inside testing system\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"
               ).staticmethod("test_mode");
    pyClass.def("wrapper_test", &GXTEST_wrap_wrapper_test,
                "wrapper_test((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Test to make sure all wrappers are valid linking\n\n"

                ":param arg1: List of functions to test\n"
                ":type arg1: str\n"
                ":param arg2: Output log file\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               ).staticmethod("wrapper_test");
    pyClass.def("core_class", &GXTEST_wrap_core_class,
                "core_class((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generic Class Test Wrapper\n\n"

                ":param arg1: Name of class to test\n"
                ":type arg1: str\n"
                ":param arg2: Output log file\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.2.0\n\n"
               ).staticmethod("core_class");


}
