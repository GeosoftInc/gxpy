 

.. _GXMAP:

GXMAP class
==================================

.. autoclass:: geosoft.gxapi.GXMAP
   :members:

.. _DUPMAP:

DUPMAP constants
-----------------------------------------------------------------------

::

   Duplicate Modes 

.. autoattribute:: geosoft.gxapi.DUPMAP_BLANK

::

   Blank 

.. autoattribute:: geosoft.gxapi.DUPMAP_COPY

::

   Copy all current contents 

.. autoattribute:: geosoft.gxapi.DUPMAP_COPY_PRE62

::

   Copy all current contents and save text for pre-6.2 versions. 

.. _MAP_EXPORT_BITS:

MAP_EXPORT_BITS constants
-----------------------------------------------------------------------

::

   Color Types 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_BITS_24

::

   24 Bit Color 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_BITS_GREY8

::

   8 Bit Gray Scale 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_BITS_8

::

   8 Bit Color 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_BITS_GREY4

::

   4 Bit Gray Scale 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_BITS_4

::

   4 Bit Color 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_BITS_GREY1

::

   1 Bit Gray Scale 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_BITS_DEFAULT

::

   Default Resolution 

.. _MAP_EXPORT_FORMAT:

MAP_EXPORT_FORMAT constants
-----------------------------------------------------------------------

::

   
   				Export Formats
   				Format   Description                  Type
   				=======  ==========================   ====
   			 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_PLT

::

   "PLT"    Geosoft Plot (\ `*`\ .plt)         Plot 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_SHP

::

   "SHP"    ArcView Shapfile (\ `*`\ .shp)     Plot 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_DXF12

::

   "DXF12"  AutoCad12 (\ `*`\ .dxf)            Plot 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_DXF13

::

   "DXF13"  AutoCad13 (\ `*`\ .dxf)            Plot 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_GTIFF

::

   "GTIFF"  GeoTIFF (\ `*`\ .tif),             Color Image 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_MTIFF

::

   "MTIFF"  MapInfo TIFF (\ `*`\ .tif)         Color Image 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_ATIFF

::

   "ATIFF"  ArcView TIFF (\ `*`\ .tif)         Color Image 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_GEO

::

   "GEO"    Geosoft COLOR grid (\ `*`\ .grd)   Color Image 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_ERM

::

   "ERM"    ER Mapper RGB (\ `*`\ .ers)        Color Image 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_FORMAT_KMZ

::

   "KMZ"    Keyhole Markup (\ `*`\ .kmz)       Zipped XML/Image files 

.. _MAP_EXPORT_METHOD:

MAP_EXPORT_METHOD constants
-----------------------------------------------------------------------

::

   Dithering Methods 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_METHOD_STANDARD

::

   Standard Dither 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_METHOD_DIFFUSE

::

   Error Diffusion Dither 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_METHOD_NONE

::

   No Dither 

.. _MAP_EXPORT_RASTER_FORMAT:

MAP_EXPORT_RASTER_FORMAT constants
-----------------------------------------------------------------------

::

   
   				Export Raster Formats
   				.
   				Format  Description                      Type           B/W  B/W  COL  B/W  COL  COL
   				======= ==========================       ===========    ===  ===  ===  ===  ===  ===
   			 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_EMF

::

   "EMF"   Enhanced Metafile (\ `*`\ .emf)        Plot 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_BMP

::

   "BMP"   Bitmap (\ `*`\ .bmp)                   Color Image     X    X    X    X    X    X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_JPEGL

::

   "JPEGL" JPEG Low Quality (\ `*`\ .jpg)         Color Image                              X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_JPEG

::

   "JPEG" JPEG (\ `*`\ .jpg)                     Color Image                              X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_JPEGH

::

   "JPEGH" JPEG High Quality (\ `*`\ .jpg)        Color Image                              X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_GIF

::

   "GIF"   GIF (\ `*`\ .gif)                      Color Image     X    X    X    X    X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_PCX

::

   "PCX"   PCX (\ `*`\ .pcx)                      Color Image     X    X    X    X    X    X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_PNG

::

   "PNG"   PNG (\ `*`\ .png)                      Color Image     X    X    X    X    X    X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_EPS

::

   "EPS"   Encasulated PostScript (\ `*`\ .eps)   Color Image                    X 

.. autoattribute:: geosoft.gxapi.MAP_EXPORT_RASTER_FORMAT_TIFF

::

   "TIFF"  TIFF (\ `*`\ .tif)                     Color Image     X    X    X    X    X    X 

.. _MAP_LIST_MODE:

MAP_LIST_MODE constants
-----------------------------------------------------------------------

::

   Map List modes 

.. autoattribute:: geosoft.gxapi.MAP_LIST_MODE_ALL


.. autoattribute:: geosoft.gxapi.MAP_LIST_MODE_3D


.. autoattribute:: geosoft.gxapi.MAP_LIST_MODE_NOT3D


.. _MAP_OPEN:

MAP_OPEN constants
-----------------------------------------------------------------------

::

   Open Modes 

.. autoattribute:: geosoft.gxapi.MAP_WRITENEW


.. autoattribute:: geosoft.gxapi.MAP_WRITEOLD


	