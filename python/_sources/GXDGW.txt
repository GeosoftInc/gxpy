 

.. _GXDGW:

GXDGW class
==================================

.. autoclass:: geosoft.gxapi.GXDGW
   :members:

.. _DGW_OBJECT:

DGW_OBJECT constants
-----------------------------------------------------------------------

::

   Dialog object defines
   \ `*`\  Labels cannot be made larger. They can only
   be the size of the original label.
   INFO TYPE   EDIT   FEDIT  LEDIT  CEDIT  EBUT
   =========   =====  =====  =====  =====  =====
   LABEL\ `*`\       RW     RW     RW     RW     RW          R - can use GetInfo_DGW
   TEXT        RW     RW     RW     RW     .           W - can use \ :func:`geosoft.gxapi.GXDGW.set_info`\ 
   PATH        .      RW     .      .      .
   FILEPATH    .      RW     .      .      .
   LISTVAL     .      .      R      .      .
   LISTALIAS   .      .      RW     .      . 

.. autoattribute:: geosoft.gxapi.DGW_LABEL

::

   The text label tied to each dialogue component. 

.. autoattribute:: geosoft.gxapi.DGW_TEXT

::

   The edit field text. 

.. autoattribute:: geosoft.gxapi.DGW_PATH

::

   The file edit path. 

.. autoattribute:: geosoft.gxapi.DGW_FILEPATH

::

   The complete file name, path included. 

.. autoattribute:: geosoft.gxapi.DGW_LISTVAL

::

   The alias value associated with the list entry. 

.. autoattribute:: geosoft.gxapi.DGW_LISTALIAS

::

   The text value associated with the list entry. 

.. autoattribute:: geosoft.gxapi.DGW_EXT

::

   The extension associated with a filename entry. 

.. autoattribute:: geosoft.gxapi.DGW_HIDE

::

   Hide the button or entry and its label, if string is not "0" 

	