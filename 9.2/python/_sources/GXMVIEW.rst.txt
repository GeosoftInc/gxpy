 

.. _GXMVIEW:

GXMVIEW class
==================================

.. autoclass:: geosoft.gxapi.GXMVIEW
   :members:

.. _MAKER:

MAKER constants
-----------------------------------------------------------------------

::

   Maker defines 

.. autoattribute:: geosoft.gxapi.MAKER_GX

::

   GX 

.. _MVIEW_CLIP:

MVIEW_CLIP constants
-----------------------------------------------------------------------

::

   Boolean clipping defines 

.. autoattribute:: geosoft.gxapi.CLIP_ON

::

   Turn ON clipping 

.. autoattribute:: geosoft.gxapi.CLIP_OFF

::

   Turn OFF clipping 

.. _MVIEW_COLOR:

MVIEW_COLOR constants
-----------------------------------------------------------------------

::

   
   				24-bit color defines
   				The \ :func:`geosoft.gxapi.GXMVIEW.color`\  function can be used to create a color int from a
   				color string description.
   				The iColorXXX_MVIEW macros can be used to create colors from component
   				intensities.
   			 

.. autoattribute:: geosoft.gxapi.C_BLACK

::

   Black 

.. autoattribute:: geosoft.gxapi.C_RED

::

   Red 

.. autoattribute:: geosoft.gxapi.C_GREEN

::

   Green 

.. autoattribute:: geosoft.gxapi.C_BLUE

::

   Blue 

.. autoattribute:: geosoft.gxapi.C_CYAN

::

   Cyan 

.. autoattribute:: geosoft.gxapi.C_MAGENTA

::

   Magenta 

.. autoattribute:: geosoft.gxapi.C_YELLOW

::

   Yellow 

.. autoattribute:: geosoft.gxapi.C_GREY

::

   Grey 

.. autoattribute:: geosoft.gxapi.C_LT_RED

::

   Light Red 

.. autoattribute:: geosoft.gxapi.C_LT_GREEN

::

   Light Green 

.. autoattribute:: geosoft.gxapi.C_LT_BLUE

::

   Light Blue 

.. autoattribute:: geosoft.gxapi.C_LT_CYAN

::

   Light Cyan 

.. autoattribute:: geosoft.gxapi.C_LT_MAGENTA

::

   Light Magenta 

.. autoattribute:: geosoft.gxapi.C_LT_YELLOW

::

   Light Yellow 

.. autoattribute:: geosoft.gxapi.C_LT_GREY

::

   Light Grey 

.. autoattribute:: geosoft.gxapi.C_GREY10

::

   Grey 10% 

.. autoattribute:: geosoft.gxapi.C_GREY25

::

   Grey 25% 

.. autoattribute:: geosoft.gxapi.C_GREY50

::

   Grey 50% 

.. autoattribute:: geosoft.gxapi.C_WHITE

::

   White 

.. autoattribute:: geosoft.gxapi.C_TRANSPARENT

::

   Transparent or no-draw 

.. _MVIEW_CYLINDER3D:

MVIEW_CYLINDER3D constants
-----------------------------------------------------------------------

::

   What parts of the cylinder are closed 

.. autoattribute:: geosoft.gxapi.MVIEW_CYLINDER3D_OPEN


.. autoattribute:: geosoft.gxapi.MVIEW_CYLINDER3D_CLOSESTART


.. autoattribute:: geosoft.gxapi.MVIEW_CYLINDER3D_CLOSEEND


.. autoattribute:: geosoft.gxapi.MVIEW_CYLINDER3D_CLOSEALL


.. _MVIEW_DRAW:

MVIEW_DRAW constants
-----------------------------------------------------------------------

::

   Polygon drawing defines 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAW_POLYLINE

::

   Draw Polylines 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAW_POLYGON

::

   Draw Polygons 

.. _MVIEW_DRAWOBJ3D_ENTITY:

MVIEW_DRAWOBJ3D_ENTITY constants
-----------------------------------------------------------------------

::

   What types of entities to draw 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_POINTS

::

   Draw 3D Points (no normals) [1 verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_LINES

::

   Draw 3D Lines (no normals) [2 verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_LINE_STRIPS

::

   Draw 3D Line strip (no normals) [2+x verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_LINE_LOOPS

::

   Draw 3D Line loop (no normals, closes loop with first point) [2+x verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_TRIANGLES

::

   Draw 3D Triangles [3 verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_STRIPS

::

   Draw 3D Triangle strips [3+x verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_FANS

::

   Draw 3D Triangle fans [3+x verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_QUADS

::

   Draw 3D Quads (Must be in the same plane) [4 verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_QUADS_STRIPS

::

   Draw 3D Quad Strips (Must be in the same plane) [4+2x verticies per object] 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_ENTITY_POLYGONS

::

   Draw 3D Quad Polygones (Must be in the same plane, must be convex and cannot intersect itself) 

.. _MVIEW_DRAWOBJ3D_MODE:

MVIEW_DRAWOBJ3D_MODE constants
-----------------------------------------------------------------------

::

   What types of entities to draw 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_MODE_FLAT

::

   Draw flat shaded faces (one normal and color per object) 

.. autoattribute:: geosoft.gxapi.MVIEW_DRAWOBJ3D_MODE_SMOOTH

::

   Draw smooth shaded faces (one normal and color per vertex) 

.. _MVIEW_EXTENT:

MVIEW_EXTENT constants
-----------------------------------------------------------------------

::

   Types of extents defines 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_ALL

::

   All objects 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_CLIP

::

   Clipping regions 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_MAP

::

   Map extents 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_VISIBLE

::

   Visible objects 

.. _MVIEW_FIT:

MVIEW_FIT constants
-----------------------------------------------------------------------

::

   Fit area defines 

.. autoattribute:: geosoft.gxapi.MVIEW_FIT_MAP

::

   Fit it to the map area 

.. autoattribute:: geosoft.gxapi.MVIEW_FIT_VIEW

::

   Fit it to the view area 

.. _MVIEW_FONT_WEIGHT:

MVIEW_FONT_WEIGHT constants
-----------------------------------------------------------------------

::

   Font weight defines 

.. autoattribute:: geosoft.gxapi.MVIEW_FONT_WEIGHT_NORMAL


.. autoattribute:: geosoft.gxapi.MVIEW_FONT_WEIGHT_ULTRALIGHT


.. autoattribute:: geosoft.gxapi.MVIEW_FONT_WEIGHT_LIGHT


.. autoattribute:: geosoft.gxapi.MVIEW_FONT_WEIGHT_MEDIUM


.. autoattribute:: geosoft.gxapi.MVIEW_FONT_WEIGHT_BOLD


.. autoattribute:: geosoft.gxapi.MVIEW_FONT_WEIGHT_XBOLD


.. autoattribute:: geosoft.gxapi.MVIEW_FONT_WEIGHT_XXBOLD


.. _MVIEW_GRID:

MVIEW_GRID constants
-----------------------------------------------------------------------

::

   Grid Drawing defines 

.. autoattribute:: geosoft.gxapi.MVIEW_GRID_DOT


.. autoattribute:: geosoft.gxapi.MVIEW_GRID_LINE


.. autoattribute:: geosoft.gxapi.MVIEW_GRID_CROSS


.. _MVIEW_GROUP:

MVIEW_GROUP constants
-----------------------------------------------------------------------

::

   Open Group defines 

.. autoattribute:: geosoft.gxapi.MVIEW_GROUP_NEW

::

   New Group (destroy any existing group) 

.. autoattribute:: geosoft.gxapi.MVIEW_GROUP_APPEND

::

   Append to an existing Group 

.. _MVIEW_GROUP_LIST:

MVIEW_GROUP_LIST constants
-----------------------------------------------------------------------

::

   What groups to list 

.. autoattribute:: geosoft.gxapi.MVIEW_GROUP_LIST_ALL

::

   All the groups. 

.. autoattribute:: geosoft.gxapi.MVIEW_GROUP_LIST_MARKED

::

   Those groups marked using the various mark functions. 

.. autoattribute:: geosoft.gxapi.MVIEW_GROUP_LIST_VISIBLE

::

   Those groups checked as visible in the view/group manager. 

.. _MVIEW_HIDE:

MVIEW_HIDE constants
-----------------------------------------------------------------------

::

   Boolean hidding defines 

.. autoattribute:: geosoft.gxapi.HIDE_ON

::

   Turn ON hidding 

.. autoattribute:: geosoft.gxapi.HIDE_OFF

::

   Turn OFF hidding 

.. _MVIEW_IS:

MVIEW_IS constants
-----------------------------------------------------------------------

::

   Defines for mview types 

.. autoattribute:: geosoft.gxapi.MVIEW_IS_AGG


.. autoattribute:: geosoft.gxapi.MVIEW_IS_MOVABLE


.. autoattribute:: geosoft.gxapi.MVIEW_IS_CSYMB


.. autoattribute:: geosoft.gxapi.MVIEW_IS_LINKED


.. autoattribute:: geosoft.gxapi.MVIEW_IS_MADE


.. autoattribute:: geosoft.gxapi.MVIEW_IS_HIDDEN


.. autoattribute:: geosoft.gxapi.MVIEW_IS_CLIPPED


.. autoattribute:: geosoft.gxapi.MVIEW_IS_META


.. autoattribute:: geosoft.gxapi.MVIEW_IS_VOXD


.. _MVIEW_LABEL_BOUND:

MVIEW_LABEL_BOUND constants
-----------------------------------------------------------------------

::

   Label Binding Defines 

.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_BOUND_NO

::

   Label Not Bound 

.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_BOUND_YES

::

   Label Bound 

.. _MVIEW_LABEL_JUST:

MVIEW_LABEL_JUST constants
-----------------------------------------------------------------------

::

   Label Justification Defines 

.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_JUST_TOP


.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_JUST_BOTTOM


.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_JUST_LEFT


.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_JUST_RIGHT


.. _MVIEW_LABEL_ORIENT:

MVIEW_LABEL_ORIENT constants
-----------------------------------------------------------------------

::

   Label Orientation Defines 

.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_ORIENT_HORIZONTAL


.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_ORIENT_TOP_RIGHT


.. autoattribute:: geosoft.gxapi.MVIEW_LABEL_ORIENT_TOP_LEFT


.. _MVIEW_NAME_LENGTH:

MVIEW_NAME_LENGTH constant
-----------------------------------------------------------------------


.. autoattribute:: geosoft.gxapi.MVIEW_NAME_LENGTH

::

   maximum length for view and group names 

.. _MVIEW_OPEN:

MVIEW_OPEN constants
-----------------------------------------------------------------------

::

   Open MVIEW define 

.. autoattribute:: geosoft.gxapi.MVIEW_READ

::

   Read Only - No changes 

.. autoattribute:: geosoft.gxapi.MVIEW_WRITENEW

::

   Create new MVIEW - destroys any existing MVIEW 

.. autoattribute:: geosoft.gxapi.MVIEW_WRITEOLD

::

   Open existing MVIEW for read/write (must exist) 

.. _MVIEW_PJ:

MVIEW_PJ constants
-----------------------------------------------------------------------

::

   Projection modes 

.. autoattribute:: geosoft.gxapi.MVIEW_PJ_OFF

::

   
   					No reprojection is used and all locations and
   					attributes are assumed to be in the view coordinate
   					system.
   				 

.. autoattribute:: geosoft.gxapi.MVIEW_PJ_LOCATION

::

   
   					Only locations will be transformed to the view
   					coordinate system.
   				 

.. autoattribute:: geosoft.gxapi.MVIEW_PJ_ALL

::

   
   					Locations and attributes (sizes, thicknesses, angles)
   					will be transformed to the view coordinate system.
   				 

.. autoattribute:: geosoft.gxapi.MVIEW_PJ_ON

::

   mode before the last MVIEW_PJ_OFF. 

.. _MVIEW_RELOCATE:

MVIEW_RELOCATE constants
-----------------------------------------------------------------------

::

   Relocation Defines 

.. autoattribute:: geosoft.gxapi.MVIEW_RELOCATE_FIT

::

   Will fit the image to fill the specified area 

.. autoattribute:: geosoft.gxapi.MVIEW_RELOCATE_ASPECT

::

   Will maintain aspect ratio 

.. autoattribute:: geosoft.gxapi.MVIEW_RELOCATE_ASPECT_CENTER

::

   Will maintain aspect ratio and center in specified area 

.. _MVIEW_SMOOTH:

MVIEW_SMOOTH constants
-----------------------------------------------------------------------

::

   Interpolation method to use for drawing line and polygon edges 

.. autoattribute:: geosoft.gxapi.MVIEW_SMOOTH_NEAREST

::

   Nearest neighbour 

.. autoattribute:: geosoft.gxapi.MVIEW_SMOOTH_CUBIC

::

   Cubic Spline 

.. autoattribute:: geosoft.gxapi.MVIEW_SMOOTH_AKIMA

::

   Akima 

.. _MVIEW_TILE:

MVIEW_TILE constants
-----------------------------------------------------------------------

::

   Tiling defines 

.. autoattribute:: geosoft.gxapi.MVIEW_TILE_RECTANGULAR


.. autoattribute:: geosoft.gxapi.MVIEW_TILE_DIAGONAL


.. autoattribute:: geosoft.gxapi.MVIEW_TILE_TRIANGULAR


.. autoattribute:: geosoft.gxapi.MVIEW_TILE_RANDOM


.. _MVIEW_UNIT:

MVIEW_UNIT constants
-----------------------------------------------------------------------

::

   Coordinate systems defines 

.. autoattribute:: geosoft.gxapi.MVIEW_UNIT_VIEW

::

   view coordinates 

.. autoattribute:: geosoft.gxapi.MVIEW_UNIT_PLOT

::

   plot hi-metric (mm\ `*`\ 100) on the map. 

.. autoattribute:: geosoft.gxapi.MVIEW_UNIT_MM

::

   plot mm on the map. 

.. autoattribute:: geosoft.gxapi.MVIEW_UNIT_VIEW_UNWARPED

::

   view coordinates without a warp if there is one 

.. _MVIEW_EXTENT_UNIT:

MVIEW_EXTENT_UNIT constants
-----------------------------------------------------------------------

::

   
   				Types of units for extents (these map to the
   				MVIEW_UNIT defines directly)
   			 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_UNIT_VIEW

::

   MVIEW_UNIT_VIEW 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_UNIT_PLOT

::

   MVIEW_UNIT_PLOT 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_UNIT_MM

::

   MVIEW_UNIT_MM 

.. autoattribute:: geosoft.gxapi.MVIEW_EXTENT_UNIT_VIEW_UNWARPED

::

   MVIEW_UNIT_VIEW_UNWARPED 

.. _TEXT_REF:

TEXT_REF constants
-----------------------------------------------------------------------

::

   Text reference locations 

.. autoattribute:: geosoft.gxapi.TEXT_REF_BOTTOM_LEFT


.. autoattribute:: geosoft.gxapi.TEXT_REF_BOTTOM_CENTER


.. autoattribute:: geosoft.gxapi.TEXT_REF_BOTTOM_RIGHT


.. autoattribute:: geosoft.gxapi.TEXT_REF_MIDDLE_LEFT


.. autoattribute:: geosoft.gxapi.TEXT_REF_MIDDLE_CENTER


.. autoattribute:: geosoft.gxapi.TEXT_REF_MIDDLE_RIGHT


.. autoattribute:: geosoft.gxapi.TEXT_REF_TOP_LEFT


.. autoattribute:: geosoft.gxapi.TEXT_REF_TOP_CENTER


.. autoattribute:: geosoft.gxapi.TEXT_REF_TOP_RIGHT


.. _MVIEW_3D_RENDER:

MVIEW_3D_RENDER constants
-----------------------------------------------------------------------

::

   
   				3D Geometry rendering defines. These flags only affect mixed geometry groups and not the data
   				specific groups (e.g. voxels, vector voxels surfaces etc.). Each of those groups 
   				has predefined optimum behaviour and any changes to these flags are ignored.
   			 

.. autoattribute:: geosoft.gxapi.MVIEW_3D_RENDER_BACKFACES

::

   This flag is enabled if the backfaces of geometry should be rendered 

.. autoattribute:: geosoft.gxapi.MVIEW_3D_DONT_SCALE_GEOMETRY

::

   
   					If the exaggeration scales of the 3D view in X, Y and/or Z is set to anything other than 1.0
   					any geometric objects (spheres, cubes etc.) for 3D groups with the following flags 
   					will render untransformed while only the centers of the objects are changed.
   					This ensures the objects appear in the correct place with respect to other data being rendered (and scaled).
   				 

	