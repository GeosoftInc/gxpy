
.. _GXMVU:

 
GXMVU class
==================================

.. autoclass:: geosoft.gxapi.GXMVU
   :members:

.. _EMLAY_GEOMETRY:

EMLAY_GEOMETRY constants
-----------------------------------------------------------------------

::

   Type of Geometry 

.. autoattribute:: geosoft.gxapi.EMLAY_V_COPLANAR

::

   0 

.. autoattribute:: geosoft.gxapi.EMLAY_H_COPLANAR

::

   1 

.. autoattribute:: geosoft.gxapi.EMLAY_V_COAXIAL

::

   2 

.. _ARROW_ALIGNMENT:

ARROW_ALIGNMENT constants
-----------------------------------------------------------------------

::

   Direction of alignment 

.. autoattribute:: geosoft.gxapi.ARROW_ALIGNMENT_HORIZONTAL


.. autoattribute:: geosoft.gxapi.ARROW_ALIGNMENT_VERTICAL


.. _BARCHART_LABEL:

BARCHART_LABEL constants
-----------------------------------------------------------------------

::

   Place to draw bar labels 

.. autoattribute:: geosoft.gxapi.BARCHART_LABEL_NO

::

   No label 

.. autoattribute:: geosoft.gxapi.BARCHART_LABEL_BELOWX

::

   Label below X axis 

.. autoattribute:: geosoft.gxapi.BARCHART_LABEL_ABOVEX

::

   Label above X axis 

.. autoattribute:: geosoft.gxapi.BARCHART_LABEL_PEND

::

   Label at positive end of bar 

.. autoattribute:: geosoft.gxapi.BARCHART_LABEL_NEND

::

   Label at negative end of bar 

.. autoattribute:: geosoft.gxapi.BARCHART_LABEL_ALTERNAT1

::

   Label at alternative ends,1st label at positive end 

.. autoattribute:: geosoft.gxapi.BARCHART_LABEL_ALTERNAT2

::

   Label at alternative ends,1st label at negative end 

.. _COLORBAR_LABEL:

COLORBAR_LABEL constants
-----------------------------------------------------------------------

::

   Label text orientation 

.. autoattribute:: geosoft.gxapi.COLORBAR_LABEL_HORIZONTAL

::

   (default) 

.. autoattribute:: geosoft.gxapi.COLORBAR_LABEL_VERTICAL

::

   Gives text an orientation of -90 degrees 

.. _COLORBAR_STYLE:

COLORBAR_STYLE constants
-----------------------------------------------------------------------

::

   Label text orientation 

.. autoattribute:: geosoft.gxapi.COLORBAR_STYLE_NONE

::

   Don't draw 

.. autoattribute:: geosoft.gxapi.COLORBAR_STYLE_MAXMIN

::

   Post max/min values 

.. _MVU_ORIENTATION:

MVU_ORIENTATION constants
-----------------------------------------------------------------------

::

   Orientation (of whatever) 

.. autoattribute:: geosoft.gxapi.MVU_ORIENTATION_VERTICAL

::

   Vertical 

.. autoattribute:: geosoft.gxapi.MVU_ORIENTATION_HORIZONTAL

::

   Horizontal 

.. _MVU_DIVISION_STYLE:

MVU_DIVISION_STYLE constants
-----------------------------------------------------------------------

::

   Orientation (of whatever) 

.. autoattribute:: geosoft.gxapi.MVU_DIVISION_STYLE_NONE

::

   No division marks 

.. autoattribute:: geosoft.gxapi.MVU_DIVISION_STYLE_LINES

::

   Division line 

.. autoattribute:: geosoft.gxapi.MVU_DIVISION_STYLE_TICS

::

   Inside tics, both sides 

.. _MVU_ARROW:

MVU_ARROW constants
-----------------------------------------------------------------------

::

   
   				Type Arrow. These definitions are used as binary flags, and can be
   				used together by passing sums.
   			 

.. autoattribute:: geosoft.gxapi.MVU_ARROW_SOLID

::

   
   					Plot the head as a solid triangle, otherwise plot a "stick arrow"
   					with three lines for the tail and two barbs.
   				 

.. autoattribute:: geosoft.gxapi.MVU_ARROW_FIXED

::

   
   					If used, input the actual length of the barbs on the arrow, in
   					view X-axis units, as measured along the tail. If not used, enter the ratio
   					between the length of the barbs and full length of the arrow (e.g. 0.4).
   					In the latter case, the longer the arrow, the bigger the arrow head.
   				 

.. _MVU_FLIGHT_COMPASS:

MVU_FLIGHT_COMPASS constants
-----------------------------------------------------------------------

::

   Compass direction 

.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_COMPASS_NONE


.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_COMPASS_EAST


.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_COMPASS_NORTH


.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_COMPASS_WEST


.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_COMPASS_SOUTH


.. _MVU_FLIGHT_DUMMIES:

MVU_FLIGHT_DUMMIES constants
-----------------------------------------------------------------------

::

   Show Dummies 

.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_DUMMIES_NOTINCLUDED


.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_DUMMIES_INCLUDED


.. _MVU_FLIGHT_LOCATE:

MVU_FLIGHT_LOCATE constants
-----------------------------------------------------------------------

::

   Line label locations 

.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_LOCATE_NONE

::

   No label 

.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_LOCATE_END

::

   
   					L100.2 -------------------------- L100.2
   
   					dOffA controls distance from label to line.
   					dOffB controls verical offset from center.
   				 

.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_LOCATE_ABOVE

::

   
   					L100.2                            L100.2
   					----------------------------------------
   
   					dOffA controls label distance above the line.
   					dOffB controls offset in from line end.
   				 

.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_LOCATE_BELOW

::

   
   					----------------------------------------
   					L100.2                            L100.2
   
   					dOffA controls label distance below the line.
   					dOffB controls offset in from line end.
   				 

.. autoattribute:: geosoft.gxapi.MVU_FLIGHT_DIRECTION

::

   
   					To add '>' to label to indicate direction, for example:
   					MVU_FLIGHT_LOCATE_END+MVU_FLIGHT_DIRECTION
   				 

.. _MVU_VOX_SURFACE_METHOD:

MVU_VOX_SURFACE_METHOD constants
-----------------------------------------------------------------------

::

   TODO 

.. autoattribute:: geosoft.gxapi.MVU_VOX_SURFACE_METHOD_MARCHING_CUBES


.. _MVU_VOX_SURFACE_OPTION:

MVU_VOX_SURFACE_OPTION constants
-----------------------------------------------------------------------

::

   TODO 

.. autoattribute:: geosoft.gxapi.MVU_VOX_SURFACE_OPTION_OPEN


.. autoattribute:: geosoft.gxapi.MVU_VOX_SURFACE_OPTION_CLOSED


.. _MVU_TEXTBOX:

MVU_TEXTBOX constants
-----------------------------------------------------------------------

::

   Type of Box 

.. autoattribute:: geosoft.gxapi.MVU_TEXTBOX_LEFT


.. autoattribute:: geosoft.gxapi.MVU_TEXTBOX_CENTER


.. autoattribute:: geosoft.gxapi.MVU_TEXTBOX_RIGHT


.. _MVU_VPOINT:

MVU_VPOINT constants
-----------------------------------------------------------------------

::

   Head Acuteness 

.. autoattribute:: geosoft.gxapi.MVU_VPOINT_SHARP


.. autoattribute:: geosoft.gxapi.MVU_VPOINT_MEDIUM


.. autoattribute:: geosoft.gxapi.MVU_VPOINT_BLUNT


.. _MVU_VPOS:

MVU_VPOS constants
-----------------------------------------------------------------------

::

   Head Position 

.. autoattribute:: geosoft.gxapi.MVU_VPOS_HEAD


.. autoattribute:: geosoft.gxapi.MVU_VPOS_MIDDLE


.. autoattribute:: geosoft.gxapi.MVU_VPOS_TAIL


.. _MVU_VSIZE:

MVU_VSIZE constants
-----------------------------------------------------------------------

::

   Head Size 

.. autoattribute:: geosoft.gxapi.MVU_VSIZE_NOHEAD


.. autoattribute:: geosoft.gxapi.MVU_VSIZE_SMALLHEAD


.. autoattribute:: geosoft.gxapi.MVU_VSIZE_MEDIUMHEAD


.. autoattribute:: geosoft.gxapi.MVU_VSIZE_LARGEHEAD


.. autoattribute:: geosoft.gxapi.MVU_VSIZE_NOTAIL


.. _MVU_VSTYLE:

MVU_VSTYLE constants
-----------------------------------------------------------------------

::

   Head Style 

.. autoattribute:: geosoft.gxapi.MVU_VSTYLE_LINES


.. autoattribute:: geosoft.gxapi.MVU_VSTYLE_BARB


.. autoattribute:: geosoft.gxapi.MVU_VSTYLE_TRIANGLE


	