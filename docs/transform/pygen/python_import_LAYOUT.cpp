#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXLAYOUT_wrap_calculate_rects(GXLAYOUTPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->calculate_rects(arg1, arg2, arg3, arg4);
}
inline void GXLAYOUT_wrap_clear_all(GXLAYOUTPtr self)
{
    self->clear_all();
}
inline void GXLAYOUT_wrap_clear_constraints(GXLAYOUTPtr self)
{
    self->clear_constraints();
}
inline GXLAYOUTPtr GXLAYOUT_wrap_create(int32_t arg1, const gx_string_type& arg2)
{
    GXLAYOUTPtr ret = GXLAYOUT::create(arg1, arg2);
    return ret;
}
inline void GXLAYOUT_wrap_get_rectangle(GXLAYOUTPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    self->get_rectangle(arg1, arg2, arg3, arg4, arg5);
}
inline void GXLAYOUT_wrap_get_rect_name(GXLAYOUTPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_rect_name(arg1, arg2);
}
inline int32_t GXLAYOUT_wrap_add_constraint(GXLAYOUTPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, double arg6)
{
    int32_t ret = self->add_constraint(arg1, (LAYOUT_CONSTR)arg2, arg3, (LAYOUT_CONSTR)arg4, arg5, arg6);
    return ret;
}
inline int32_t GXLAYOUT_wrap_add_rectangle(GXLAYOUTPtr self, double arg1, double arg2, double arg3, double arg4)
{
    int32_t ret = self->add_rectangle(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXLAYOUT_wrap_num_rectangles(GXLAYOUTPtr self)
{
    int32_t ret = self->num_rectangles();
    return ret;
}
inline void GXLAYOUT_wrap_set_rectangle(GXLAYOUTPtr self, int32_t arg1, double arg2, double arg3, double arg4, double arg5)
{
    self->set_rectangle(arg1, arg2, arg3, arg4, arg5);
}
inline void GXLAYOUT_wrap_set_rectangle_name(GXLAYOUTPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_rectangle_name(arg1, arg2);
}

void gxPythonImportGXLAYOUT()
{

    class_<GXLAYOUT, GXLAYOUTPtr> pyClass("GXLAYOUT",
                                          "\n.. parsed-literal::\n\n"
                                          "   \n"
                                          "   		Layout class for generic relative layout calculation\n"
                                          "   \n"
                                          "   		The relative layout algorithm allows a logical organization of layout rectangles.\n"
                                          "   		You can set constraints with English-like semantics. For example:\n"
                                          "   \n"
                                          "   		\"Set the left side of rectangle 1 equal to the right side of rectangle 2 plus 10 pixels.\"\n"
                                          "   		\"Set the bottom of rectangle 1 to 25 percent of the height of rectangle 2.\"\n"
                                          "   		\"Move node 1 such that its bottom is equal to the top of rectangle 2 minus 10 pixels.\"\n"
                                          "   \n"
                                          "   		The last constraint set would enjoy priority over any others as it would be\n"
                                          "   		the last one that would influence the rectangle calculations. See the notes for iSetConstraint\n"
                                          "   		for more details.\n"
                                          "   	\n\n"
                                          , no_init);

    pyClass.def("null", &GXLAYOUT::null, "null() -> GXLAYOUT\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXLAYOUT`\n\n:returns: A null :class:`geosoft.gxapi.GXLAYOUT`\n:rtype: :class:`geosoft.gxapi.GXLAYOUT`\n").staticmethod("null");
    pyClass.def("is_null", &GXLAYOUT::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXLAYOUT is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXLAYOUT`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXLAYOUT::_internal_handle);
    pyClass.def("calculate_rects", &GXLAYOUT_wrap_calculate_rects,
                "calculate_rects((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate new positions based on initial conditions and constraints\n\n"

                ":param arg1: Parent Rectangle Min X after calculation\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Parent Rectangle Min Y after calculation\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Parent Rectangle Max X after calculation\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Parent Rectangle Max Y after calculation\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use iGetRectangle to obtain the results for the other rectangles. Depending\n"
                "   					on the constraints set the parent rectangle may also change\n"
                "   					after the calculation (returned here for convenience).\n"
                "   				\n\n"
               );
    pyClass.def("clear_all", &GXLAYOUT_wrap_clear_all,
                "clear_all() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove all children and constraints from layout\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("clear_constraints", &GXLAYOUT_wrap_clear_constraints,
                "clear_constraints() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove all constraints from layout\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("create", &GXLAYOUT_wrap_create,
                "create((int)arg1, (str)arg2) -> GXLAYOUT:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a layout calculation object\n\n"

                ":param arg1: Initial number of objects (may be 0)\n"
                ":type arg1: int\n"
                ":param arg2: Optional name of parent layout (may be empty)\n"
                ":type arg2: str\n"
                ":returns: LAYOUT object.\n"
                ":rtype: :class:`geosoft.gxapi.GXLAYOUT`\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("create");
    pyClass.def("get_rectangle", &GXLAYOUT_wrap_get_rectangle,
                "get_rectangle((int)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the current bounds for a rectangle or the parent layout\n\n"

                ":param arg1: Rectangle to get info for (-1 for parent)\n"
                ":type arg1: int\n"
                ":param arg2: Rectangle Min X\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Rectangle Min Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Rectangle Max X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Rectangle Max Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_rect_name", &GXLAYOUT_wrap_get_rect_name,
                "get_rect_name((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets an optional name the current info for a rectangle or the parent layout\n\n"

                ":param arg1: Rectangle to get info for (-1 for parent)\n"
                ":type arg1: int\n"
                ":param arg2: Buffer for name of the rectangle\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("add_constraint", &GXLAYOUT_wrap_add_constraint,
                "add_constraint((int)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (float)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a constraint between any two rectangles or to one with absolute positioning\n\n"

                ":param arg1: From rectangle (Or -1 for parent)\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`LAYOUT_CONSTR`\\  From constraint flag\n"
                ":type arg2: int\n"
                ":param arg3: To rectangle (Or -1 for parent Or -2 for absolute positioning)\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`LAYOUT_CONSTR`\\  To constraint flag\n"
                ":type arg4: int\n"
                ":param arg5: Offset modifier\n"
                ":type arg5: float\n"
                ":param arg6: Multiplicative modifier\n"
                ":type arg6: float\n"
                ":returns: 0 - OK\n"
                "          						1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Constraints can be applied between 2 rectangles in the layout, or to 1 rectangle with\n"
                "   					absolute positioning. Use the constraints to control left, right, bottom, top,\n"
                "   					width, height, or centering configurations. Examples:\n"
                "   \n"
                "   					(ordered as rectangle from, constraint from, rectangle to, constraint to, offset modifier, multiplicative modifier)\n"
                "   \n"
                "   					A, LAYOUT_CONSTR_LEFT, B, LAYOUT_CONSTR_LEFT, 0, 0, 1.0 		               Set left position of A equal to left pos of B\n"
                "   					A, LAYOUT_CONSTR_LEFT, B, LAYOUT_CONSTR_RIGHT, 0, 0, 1.0		               Set left pos of A equal to right of B\n"
                "   \n"
                "   					The offset modifier is used for additive manipulation of constraints\n"
                "   					A, LAYOUT_CONSTR_LEFT, B, LAYOUT_CONSTR_LEFT, 10, 0, 1.0		               Set left pos of A equal to left of B, plus 10\n"
                "   					A, LAYOUT_CONSTR_BOTTOM, B, LAYOUT_CONSTR_TOP, -20, 0, 1.0	               Set bottom of A equal to top of B, minus 20\n"
                "   \n"
                "   					Multiplicative manipulation of constraints\n"
                "   					A, LAYOUT_CONSTR_WIDTH, B, LAYOUT_CONSTR_WIDTH, 0, 0.5	                  Set the width of A equal to 0.5 times the width of B\n"
                "   					A, LAYOUT_CONSTR_HEIGHT, B, LAYOUT_CONSTR_WIDTH, 0, 1.2	                  Set the height of A equal to 1.2 times the width of B\n"
                "   \n"
                "   					You can use BOTH the multiplicative and offset modifiers in conjunction (multiplicative gets precedence)\n"
                "   					A, LAYOUT_CONSTR_WIDTH, B, LAYOUT_CONSTR_WIDTH, 10, 0.5 	                  A(width) = (0.5 \\ `*`\\  B(width)) + 10\n"
                "   					A, LAYOUT_CONSTR_LEFT, B, LAYOUT_CONSTR_WIDTH, -20, 0.1	                  A(left) = (0.1 \\ `*`\\  B(width)) + (-20)\n"
                "   \n"
                "   					If second node is -2, use absolute positioning\n"
                "   					A,LAYOUT_CONSTR_LEFT,-2,<ignored>,25,<ignored>,<ignored> 	               Position left of A at position 25\n"
                "   					A,LAYOUT_CONSTR_WIDTH,-2,<ignored>,30,<ignored>,<ignored>	               Set width of A to 30\n"
                "   \n"
                "   					Use the MOVE constraints to move an entire window without resizing\n"
                "   					A, LAYOUT_CONSTR_MOVEL, B, LAYOUT_CONSTR_LEFT, 0, 0, 1.0	                  Move node A, align left with left side of B\n"
                "   					A, LAYOUT_CONSTR_MOVEL, B, LAYOUT_CONSTR_RIGHT, 0, 0, 1.0	               Move node A, align left with right side of B\n"
                "   					A, LAYOUT_CONSTR_MOVET, B, LAYOUT_CONSTR_WIDTH, 0, 0, 1.0	               Move node A, align bottom to position equal to width of B\n"
                "   					A, LAYOUT_CONSTR_MOVER, B, LAYOUT_CONSTR_RIGHT, 10, 1.1	                  Move node A, align right to 1.1\\ `*`\\ right of B, plus 10\n"
                "   					A, LAYOUT_CONSTR_MOVEL, NULL, 10, 0, 1.0	                                 Move node A, align left at position 10\n"
                "   				\n\n"
               );
    pyClass.def("add_rectangle", &GXLAYOUT_wrap_add_rectangle,
                "add_rectangle((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds a rectangle as one of the layout's children (Higer.\n\n"

                ":param arg1: Rectangle Min X   (All 0's for undefined allowed)\n"
                ":type arg1: float\n"
                ":param arg2: Rectangle Min Y\n"
                ":type arg2: float\n"
                ":param arg3: Rectangle Max X\n"
                ":type arg3: float\n"
                ":param arg4: Rectangle Max Y\n"
                ":type arg4: float\n"
                ":returns: Rectangle number, -1 on error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("num_rectangles", &GXLAYOUT_wrap_num_rectangles,
                "num_rectangles() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the number of children in the list.\n\n"

                ":returns: Number of rectangles not counting the parent\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("set_rectangle", &GXLAYOUT_wrap_set_rectangle,
                "set_rectangle((int)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the current bounds for a rectangle previously added to the layout\n\n"

                ":param arg1: Rectangle to set info for (-1 for parent)\n"
                ":type arg1: int\n"
                ":param arg2: Rectangle Min X\n"
                ":type arg2: float\n"
                ":param arg3: Rectangle Min Y\n"
                ":type arg3: float\n"
                ":param arg4: Rectangle Max X\n"
                ":type arg4: float\n"
                ":param arg5: Rectangle Max Y\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("set_rectangle_name", &GXLAYOUT_wrap_set_rectangle_name,
                "set_rectangle_name((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets an optional name the current info for a rectangle or the parent layout\n\n"

                ":param arg1: Rectangle to set info for (-1 for parent)\n"
                ":type arg1: int\n"
                ":param arg2: Name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );

    scope().attr("LAYOUT_CONSTR_LEFT") = (int32_t)0;
    scope().attr("LAYOUT_CONSTR_RIGHT") = (int32_t)1;
    scope().attr("LAYOUT_CONSTR_TOP") = (int32_t)2;
    scope().attr("LAYOUT_CONSTR_BOTTOM") = (int32_t)3;
    scope().attr("LAYOUT_CONSTR_WIDTH") = (int32_t)4;
    scope().attr("LAYOUT_CONSTR_HEIGHT") = (int32_t)5;
    scope().attr("LAYOUT_CONSTR_HCENTER") = (int32_t)6;
    scope().attr("LAYOUT_CONSTR_VCENTER") = (int32_t)7;
    scope().attr("LAYOUT_CONSTR_MOVEL") = (int32_t)8;
    scope().attr("LAYOUT_CONSTR_MOVER") = (int32_t)9;
    scope().attr("LAYOUT_CONSTR_MOVET") = (int32_t)10;
    scope().attr("LAYOUT_CONSTR_MOVEB") = (int32_t)11;

}
