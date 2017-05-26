
.. _GXARCMAP:

 
GXARCMAP class
==================================

.. autoclass:: geosoft.gxapi.GXARCMAP
   :members:

.. _ARCMAP_LOAD_FLAGS:

ARCMAP_LOAD_FLAGS constants
-----------------------------------------------------------------------

::

   Flags that can be combined and passed to iLoadMap_ARCMAP 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_DELFRAME

::

   If an exisiting frame is found delete it 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_DELLAYER

::

   If an exisiting layer is found delete it 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_EXISTFRAME

::

   If an exisiting frame is found add new layers to it 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_COPYLAYER

::

   If an exisiting layer is found make a copy 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_HIDESIBLINGS

::

   Hide all other existing layers in frame 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_PREFIXMAPFRAME

::

   Prefix the map filename part as part of the frame name 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_PREFIXMAPLAYER

::

   Prefix the map filename part as part of the layer name 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_MERGETOSINGLEVIEW

::

   Will render all views in single layer with the data view defining the coordinate system 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_INTOCURRENTFRAME

::

   Load everything into the current data frame 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_NOMAPLAYERS

::

   Use the map only for sizing data frames in layout, only load extra datasets. 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_ACTIVATE

::

   Activates the main quickmap layer when done (e.g. 3D Viewer) 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_NEW

::

   New method for loading maps introduced in 7.1. Will mimic what happens in montaj (i.e. base groups and 3D become graphics and views gets split into separate LYRs). 

.. autoattribute:: geosoft.gxapi.ARCMAP_LOAD_NAMETAGISPREFIX

::

   Use a provided name tag as prefix when naming a newly created map layer. 

	