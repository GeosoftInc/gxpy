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
class GXLAYOUT(gxapi_cy.WrapLAYOUT):
    """
    GXLAYOUT class.

    Layout class for generic relative layout calculation

    The relative layout algorithm allows a logical organization of layout rectangles.
    You can set constraints with English-like semantics. For example:

    "Set the left side of rectangle 1 equal to the right side of rectangle 2 plus 10 pixels."
    "Set the bottom of rectangle 1 to 25 percent of the height of rectangle 2."
    "Move node 1 such that its bottom is equal to the top of rectangle 2 minus 10 pixels."

    The last constraint set would enjoy priority over any others as it would be
    the last one that would influence the rectangle calculations. See the notes for iSetConstraint
    for more details.
    """

    def __init__(self, handle=0):
        super(GXLAYOUT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLAYOUT <geosoft.gxapi.GXLAYOUT>`
        
        :returns: A null `GXLAYOUT <geosoft.gxapi.GXLAYOUT>`
        :rtype:   GXLAYOUT
        """
        return GXLAYOUT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def calculate_rects(self, min_x, min_y, max_x, max_y):
        """
        Calculate new positions based on initial conditions and constraints
        
        :param min_x:   Parent Rectangle Min X after calculation
        :param min_y:   Parent Rectangle Min Y after calculation
        :param max_x:   Parent Rectangle Max X after calculation
        :param max_y:   Parent Rectangle Max Y after calculation
        :type  min_x:   float_ref
        :type  min_y:   float_ref
        :type  max_x:   float_ref
        :type  max_y:   float_ref

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Use iGetRectangle to obtain the results for the other rectangles. Depending
        on the constraints set the parent rectangle may also change
        after the calculation (returned here for convenience).
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._calculate_rects(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def clear_all(self):
        """
        Remove all children and constraints from layout
        

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._clear_all()
        




    def clear_constraints(self):
        """
        Remove all constraints from layout
        

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._clear_constraints()
        



    @classmethod
    def create(cls, num, name):
        """
        Creates a layout calculation object
        
        :param num:   Initial number of objects (may be 0)
        :param name:  Optional name of parent layout (may be empty)
        :type  num:   int
        :type  name:  str

        :returns:     `GXLAYOUT <geosoft.gxapi.GXLAYOUT>` object.
        :rtype:       GXLAYOUT

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapLAYOUT._create(GXContext._get_tls_geo(), num, name.encode())
        return GXLAYOUT(ret_val)






    def get_rectangle(self, rect, min_x, min_y, max_x, max_y):
        """
        Gets the current bounds for a rectangle or the parent layout
        
        :param rect:    Rectangle to get info for (-1 for parent)
        :param min_x:   Rectangle Min X
        :param min_y:   Rectangle Min Y
        :param max_x:   Rectangle Max X
        :param max_y:   Rectangle Max Y
        :type  rect:    int
        :type  min_x:   float_ref
        :type  min_y:   float_ref
        :type  max_x:   float_ref
        :type  max_y:   float_ref

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._get_rectangle(rect, min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_rect_name(self, rect, name):
        """
        Gets an optional name the current info for a rectangle or the parent layout
        
        :param rect:    Rectangle to get info for (-1 for parent)
        :param name:    Buffer for name of the rectangle
        :type  rect:    int
        :type  name:    str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        name.value = self._get_rect_name(rect, name.value.encode())
        




    def add_constraint(self, rect_from, constr_from, rect_to, constr_to, o_mod, m_mod):
        """
        Add a constraint between any two rectangles or to one with absolute positioning
        
        :param rect_from:    From rectangle (Or -1 for parent)
        :param constr_from:  :ref:`LAYOUT_CONSTR` From constraint flag
        :param rect_to:      To rectangle (Or -1 for parent Or -2 for absolute positioning)
        :param constr_to:    :ref:`LAYOUT_CONSTR` To constraint flag
        :param o_mod:        Offset modifier
        :param m_mod:        Multiplicative modifier
        :type  rect_from:    int
        :type  constr_from:  int
        :type  rect_to:      int
        :type  constr_to:    int
        :type  o_mod:        float
        :type  m_mod:        float

        :returns:            0 - OK
                             1 - Error
        :rtype:              int

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Constraints can be applied between 2 rectangles in the layout, or to 1 rectangle with
        absolute positioning. Use the constraints to control left, right, bottom, top,
        width, height, or centering configurations. Examples:

        (ordered as rectangle from, constraint from, rectangle to, constraint to, offset modifier, multiplicative modifier)

        A, `LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`, B, `LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`, 0, 0, 1.0 		               Set left position of A equal to left pos of B
        A, `LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`, B, `LAYOUT_CONSTR_RIGHT <geosoft.gxapi.LAYOUT_CONSTR_RIGHT>`, 0, 0, 1.0		               Set left pos of A equal to right of B

        The offset modifier is used for additive manipulation of constraints
        A, `LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`, B, `LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`, 10, 0, 1.0		               Set left pos of A equal to left of B, plus 10
        A, `LAYOUT_CONSTR_BOTTOM <geosoft.gxapi.LAYOUT_CONSTR_BOTTOM>`, B, `LAYOUT_CONSTR_TOP <geosoft.gxapi.LAYOUT_CONSTR_TOP>`, -20, 0, 1.0	               Set bottom of A equal to top of B, minus 20

        Multiplicative manipulation of constraints
        A, `LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`, B, `LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`, 0, 0.5	                  Set the width of A equal to 0.5 times the width of B
        A, `LAYOUT_CONSTR_HEIGHT <geosoft.gxapi.LAYOUT_CONSTR_HEIGHT>`, B, `LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`, 0, 1.2	                  Set the height of A equal to 1.2 times the width of B

        You can use BOTH the multiplicative and offset modifiers in conjunction (multiplicative gets precedence)
        A, `LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`, B, `LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`, 10, 0.5 	                  A(width) = (0.5 * B(width)) + 10
        A, `LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`, B, `LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`, -20, 0.1	                  A(left) = (0.1 * B(width)) + (-20)

        If second node is -2, use absolute positioning
        A,`LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`,-2,<ignored>,25,<ignored>,<ignored> 	               Position left of A at position 25
        A,`LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`,-2,<ignored>,30,<ignored>,<ignored>	               Set width of A to 30

        Use the MOVE constraints to move an entire window without resizing
        A, `LAYOUT_CONSTR_MOVEL <geosoft.gxapi.LAYOUT_CONSTR_MOVEL>`, B, `LAYOUT_CONSTR_LEFT <geosoft.gxapi.LAYOUT_CONSTR_LEFT>`, 0, 0, 1.0	                  Move node A, align left with left side of B
        A, `LAYOUT_CONSTR_MOVEL <geosoft.gxapi.LAYOUT_CONSTR_MOVEL>`, B, `LAYOUT_CONSTR_RIGHT <geosoft.gxapi.LAYOUT_CONSTR_RIGHT>`, 0, 0, 1.0	               Move node A, align left with right side of B
        A, `LAYOUT_CONSTR_MOVET <geosoft.gxapi.LAYOUT_CONSTR_MOVET>`, B, `LAYOUT_CONSTR_WIDTH <geosoft.gxapi.LAYOUT_CONSTR_WIDTH>`, 0, 0, 1.0	               Move node A, align bottom to position equal to width of B
        A, `LAYOUT_CONSTR_MOVER <geosoft.gxapi.LAYOUT_CONSTR_MOVER>`, B, `LAYOUT_CONSTR_RIGHT <geosoft.gxapi.LAYOUT_CONSTR_RIGHT>`, 10, 1.1	                  Move node A, align right to 1.1*right of B, plus 10
        A, `LAYOUT_CONSTR_MOVEL <geosoft.gxapi.LAYOUT_CONSTR_MOVEL>`, NULL, 10, 0, 1.0	                                 Move node A, align left at position 10
        """
        ret_val = self._add_constraint(rect_from, constr_from, rect_to, constr_to, o_mod, m_mod)
        return ret_val




    def add_rectangle(self, min_x, min_y, max_x, max_y):
        """
        Adds a rectangle as one of the layout's children (Higer.
        
        :param min_x:   Rectangle Min X   (All 0's for undefined allowed)
        :param min_y:   Rectangle Min Y
        :param max_x:   Rectangle Max X
        :param max_y:   Rectangle Max Y
        :type  min_x:   float
        :type  min_y:   float
        :type  max_x:   float
        :type  max_y:   float

        :returns:       Rectangle number, -1 on error
        :rtype:         int

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._add_rectangle(min_x, min_y, max_x, max_y)
        return ret_val




    def num_rectangles(self):
        """
        Returns the number of children in the list.
        

        :returns:       Number of rectangles not counting the parent
        :rtype:         int

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._num_rectangles()
        return ret_val




    def set_rectangle(self, rect, min_x, min_y, max_x, max_y):
        """
        Sets the current bounds for a rectangle previously added to the layout
        
        :param rect:    Rectangle to set info for (-1 for parent)
        :param min_x:   Rectangle Min X
        :param min_y:   Rectangle Min Y
        :param max_x:   Rectangle Max X
        :param max_y:   Rectangle Max Y
        :type  rect:    int
        :type  min_x:   float
        :type  min_y:   float
        :type  max_x:   float
        :type  max_y:   float

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_rectangle(rect, min_x, min_y, max_x, max_y)
        




    def set_rectangle_name(self, rect, p3):
        """
        Sets an optional name the current info for a rectangle or the parent layout
        
        :param rect:    Rectangle to set info for (-1 for parent)
        :param p3:      Name
        :type  rect:    int
        :type  p3:      str

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_rectangle_name(rect, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer