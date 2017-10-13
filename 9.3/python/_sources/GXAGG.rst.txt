
.. _GXAGG:

 
GXAGG class
==================================

.. autoclass:: geosoft.gxapi.GXAGG
   :members:

.. _AGG_LAYER_ZONE:

AGG_LAYER_ZONE constants
-----------------------------------------------------------------------

::

   Aggregate Layer Zone defines 

.. autoattribute:: geosoft.gxapi.AGG_LAYER_ZONE_DEFAULT

::

   
   					If a color table with no color transform is passed
   					it will be used with the default zoning
   					method of the data, which is usually
   					AGG_LAYER_ZONE_EQUALAREA.
   				 

.. autoattribute:: geosoft.gxapi.AGG_LAYER_ZONE_LINEAR

::

   Linear Distribution 

.. autoattribute:: geosoft.gxapi.AGG_LAYER_ZONE_NORMAL

::

   Normal Distribution 

.. autoattribute:: geosoft.gxapi.AGG_LAYER_ZONE_EQUALAREA

::

   Equal Area Distribution 

.. autoattribute:: geosoft.gxapi.AGG_LAYER_ZONE_SHADE

::

   
   					If AGG_LAYER_ZONE_SHADE is specified, a shaded relief
   					layer is created from the specified grid.  A new grid
   					file will also be created to hold the shaded relief
   					image data.  This file will have the same name as the
   					original grid but with "_s" added to the root name.
   					It will always be located in the workspace directory
   					regardless of the location of the original source image.
   					If the file already exists, it will used as it is.
   					Shading is always at inclination = declination = 45 deg.
   					with default scaling.  If different shading is desired,
   					use the \ :func:`geosoft.gxapi.GXAGG.layer_shade_img`\  method.
   				 

.. autoattribute:: geosoft.gxapi.AGG_LAYER_ZONE_LOGLINEAR

::

   Log Linear Distribution 

.. autoattribute:: geosoft.gxapi.AGG_LAYER_ZONE_LAST

::

   
   					The last ITR used to display this
   					data will be used if it exists.  If it
   					does not exist, the behaviour is the same
   					as AGG_LAYER_ZONE_DEFAULT.
   				 

.. _AGG_MODEL:

AGG_MODEL constants
-----------------------------------------------------------------------

::

   Aggregation color model defines 

.. autoattribute:: geosoft.gxapi.AGG_MODEL_HSV

::

   Hue Saturation Value 

.. autoattribute:: geosoft.gxapi.AGG_MODEL_RGB

::

   Red Green Blue 

.. autoattribute:: geosoft.gxapi.AGG_MODEL_CMY

::

   Cyan Magenta Yellow 

.. _AGG_RENDER:

AGG_RENDER constants
-----------------------------------------------------------------------

::

   Aggregation rendering modes 

.. autoattribute:: geosoft.gxapi.AGG_RENDER_ADD

::

   Add all the colors together 

.. autoattribute:: geosoft.gxapi.AGG_RENDER_BLEND

::

   Adds and divides by the number of non-dummy colors 

.. autoattribute:: geosoft.gxapi.AGG_RENDER_BLEND_ALL

::

   Adds and divides by the number of colors 

.. autoattribute:: geosoft.gxapi.AGG_RENDER_FADE

::

   Multiplies current colors by the input's colors over 255 (input works as the percentage of color to preserve) 

	