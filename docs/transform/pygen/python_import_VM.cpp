#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXVMPtr GXVM_wrap_create(int32_t arg1, int32_t arg2)
{
    GXVMPtr ret = GXVM::create((GEO_VAR)arg1, arg2);
    return ret;
}
inline GXVMPtr GXVM_wrap_create_ext(int32_t arg1, int32_t arg2)
{
    GXVMPtr ret = GXVM::create_ext((GS_TYPES)arg1, arg2);
    return ret;
}
inline int32_t GXVM_wrap_get_int(GXVMPtr self, int32_t arg1)
{
    int32_t ret = self->get_int(arg1);
    return ret;
}
inline void GXVM_wrap_get_string(GXVMPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_string(arg1, arg2);
}
inline int32_t GXVM_wrap_length(GXVMPtr self)
{
    int32_t ret = self->length();
    return ret;
}
inline void GXVM_wrap_re_size(GXVMPtr self, int32_t arg1)
{
    self->re_size(arg1);
}
inline double GXVM_wrap_get_double(GXVMPtr self, int32_t arg1)
{
    double ret = self->get_double(arg1);
    return ret;
}
inline void GXVM_wrap_set_int(GXVMPtr self, int32_t arg1, int32_t arg2)
{
    self->set_int(arg1, arg2);
}
inline void GXVM_wrap_set_double(GXVMPtr self, int32_t arg1, double arg2)
{
    self->set_double(arg1, arg2);
}
inline void GXVM_wrap_set_string(GXVMPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_string(arg1, arg2);
}

void gxPythonImportGXVM()
{

    class_<GXVM, GXVMPtr> pyClass("GXVM",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		In-memory vector data methods\n"
                                  "   		The VM class will store vector (array) data in a memory buffer which\n"
                                  "   		can be accessed using the VM methods.\n"
                                  "   		The main use for the VM class is to store data in a single physical\n"
                                  "   		memory location.  This memory can then be accessed by a user DLL using\n"
                                  "   		the \\ :func:`geosoft.gxapi.GXGEO.get_ptr_vm`\\  function defined in gx_extern.h.\n"
                                  "   		VM memory can be any size, but a VM is intended for handling relatively\n"
                                  "   		small sets of data compared to a VV, which can work efficiently with\n"
                                  "   		very large volumes of data.  The acceptable maximum VM size depends on\n"
                                  "   		the operating system and the performance requirements of an application.\n"
                                  "   		The best performance is achieved when all VM memory can be stored\n"
                                  "   		comfortably within the the available system RAM.  If all VM memory\n"
                                  "   		will not fit in the system RAM, the operating system virtual memory\n"
                                  "   		manager will be used to swap memory to the operations systems virtual\n"
                                  "   		memory paging file.  Note that the operating system virtual memory\n"
                                  "   		manager is much slower than the manager used by Geosoft when working with\n"
                                  "   		very large arrays in a VV.\n"
                                  "   \n"
                                  "   		See VV for methods to move data between a VM and a VV.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXVM::null, "null() -> GXVM\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXVM`\n\n:returns: A null :class:`geosoft.gxapi.GXVM`\n:rtype: :class:`geosoft.gxapi.GXVM`\n").staticmethod("null");
    pyClass.def("is_null", &GXVM::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXVM is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXVM`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXVM::_internal_handle);
    pyClass.def("create", &GXVM_wrap_create,
                "create((int)arg1, (int)arg2) -> GXVM:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VM.\n\n"

                ":param arg1: \\ :ref:`GEO_VAR`\\ \n"
                ":type arg1: int\n"
                ":param arg2: VM length (less than 16777215)\n"
                ":type arg2: int\n"
                ":returns: VM Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVM`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The VM elements are initialized to dummies.\n\n"
               ).staticmethod("create");
    pyClass.def("create_ext", &GXVM_wrap_create_ext,
                "create_ext((int)arg1, (int)arg2) -> GXVM:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VM, using one of the \\ :ref:`GS_TYPES`\\  special data types.\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg1: int\n"
                ":param arg2: VM length (less than 16777215)\n"
                ":type arg2: int\n"
                ":returns: VM Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVM`\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The VM elements are initialized to dummies.\n\n"
               ).staticmethod("create_ext");
    pyClass.def("get_int", &GXVM_wrap_get_int,
                "get_int((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an integer element from a VM.\n\n"

                ":param arg1: element wanted\n"
                ":type arg1: int\n"
                ":returns: Element wanted, or iDUMMY\n"
                "          						if the value is dummy or outside of the range of data.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_string", &GXVM_wrap_get_string,
                "get_string((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a string element from a VM.\n\n"

                ":param arg1: element wanted\n"
                ":type arg1: int\n"
                ":param arg2: string in which to place element\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns element wanted, or blank string\n"
                "   					if the value is dummy or outside of the range of data.\n"
                "   \n"
                "   					Type conversions are performed if necessary.  Dummy values\n"
                "   					are converted to \"\\ `*`\\ \" string.\n"
                "   				\n\n"
               );
    pyClass.def("length", &GXVM_wrap_length,
                "length() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns current VM length.\n\n"

                ":returns: # of elements in the VM.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("re_size", &GXVM_wrap_re_size,
                "re_size((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-set the size of a VM.\n\n"

                ":param arg1: new size (number of elements)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If increasing the VM size, new elements are set to dummies.\n\n"
               );
    pyClass.def("get_double", &GXVM_wrap_get_double,
                "get_double((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a real element from a VM.\n\n"

                ":param arg1: element wanted\n"
                ":type arg1: int\n"
                ":returns: Element wanted, or rDUMMY\n"
                "          						if the value is dummy or outside of the range of data.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_int", &GXVM_wrap_set_int,
                "set_int((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an integer element in a VM.\n\n"

                ":param arg1: element to set\n"
                ":type arg1: int\n"
                ":param arg2: value to set\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   \n"
                "   					If the element is > current VM length, the VM length is\n"
                "   					increased.  Reallocating VM lengths can lead to fragmented\n"
                "   					memory and should be avoided if possible.\n"
                "   				\n\n"
               );
    pyClass.def("set_double", &GXVM_wrap_set_double,
                "set_double((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a real element in a VM.\n\n"

                ":param arg1: element to set\n"
                ":type arg1: int\n"
                ":param arg2: value to set\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   \n"
                "   					If the element is > current VM length, the VM length is\n"
                "   					increased.  Reallocating VM lengths can lead to fragmented\n"
                "   					memory and should be avoided if possible.\n"
                "   				\n\n"
               );
    pyClass.def("set_string", &GXVM_wrap_set_string,
                "set_string((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a string element in a VM.\n\n"

                ":param arg1: element to set\n"
                ":type arg1: int\n"
                ":param arg2: string to set\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   \n"
                "   					If the element is > current VM length, the VM length is\n"
                "   					increased.  Reallocating VM lengths can lead to fragmented\n"
                "   					memory and should be avoided if possible.\n"
                "   				\n\n"
               );


}
