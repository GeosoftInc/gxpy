 

.. _GXIMG:

GXIMG class
==================================

.. autoclass:: geosoft.gxapi.GXIMG
   :members:

.. _IMG_FILE:

IMG_FILE constants
-----------------------------------------------------------------------

::

   Image open modes 

.. autoattribute:: geosoft.gxapi.IMG_FILE_READONLY

::

   Reading only 

.. autoattribute:: geosoft.gxapi.IMG_FILE_READWRITE

::

   Reading and writting 

.. autoattribute:: geosoft.gxapi.IMG_FILE_READORWRITE

::

   
   					Allows you to open read-only grids to change the
   					projection or location information.  If you can write
   					to the original grid (dat), the changed projection
   					or location information will be passed on to the grid,
   					otherwise changes will only occur in the .gi file.
   				 

.. _IMG_QUERY:

IMG_QUERY constants
-----------------------------------------------------------------------

::

   Information to Query 

.. autoattribute:: geosoft.gxapi.IMG_QUERY_iWRITE


.. autoattribute:: geosoft.gxapi.IMG_QUERY_iPG


.. autoattribute:: geosoft.gxapi.IMG_QUERY_iWRITEPG


.. autoattribute:: geosoft.gxapi.IMG_QUERY_iIMGTYPE

::

   The element type used to open the IMG. 

.. autoattribute:: geosoft.gxapi.IMG_QUERY_iDATTYPE

::

   
   					DATTYPE is the native element type of the DAT.
   					Types are:   0 - byte
   					1 - unsigned 16-bit short
   					2 - 16-bit short
   					3 - 32-bit long
   					4 - 32-bit float
   					5 - 64-bit double
   				 

.. autoattribute:: geosoft.gxapi.IMG_QUERY_iRENDER

::

   
   					Render modes are:    0 - interpolate
   					1 - pixelate
   					2 - colour
   				 

.. autoattribute:: geosoft.gxapi.IMG_QUERY_iKX


.. autoattribute:: geosoft.gxapi.IMG_QUERY_iNX


.. autoattribute:: geosoft.gxapi.IMG_QUERY_iNY


.. autoattribute:: geosoft.gxapi.IMG_QUERY_iNV


.. autoattribute:: geosoft.gxapi.IMG_QUERY_iNE


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rXO


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rYO


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rDX


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rDY


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rROT


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rBASE


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rMULT


.. autoattribute:: geosoft.gxapi.IMG_QUERY_rCOMPRESSION_RATIO


.. _IMG_RELOCATE:

IMG_RELOCATE constants
-----------------------------------------------------------------------

::

   Relocation Style 

.. autoattribute:: geosoft.gxapi.IMG_RELOCATE_FIT

::

   will fit the image to fill the specified area 

.. autoattribute:: geosoft.gxapi.IMG_RELOCATE_ASPECT

::

   will maintain aspect ratio 

	