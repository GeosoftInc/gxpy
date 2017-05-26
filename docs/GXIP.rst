
.. _GXIP:

 
GXIP class
==================================

.. autoclass:: geosoft.gxapi.GXIP
   :members:

.. _IP_ARRAY:

IP_ARRAY constants
-----------------------------------------------------------------------

::

   IP Array options 

.. autoattribute:: geosoft.gxapi.IP_ARRAY_DPDP


.. autoattribute:: geosoft.gxapi.IP_ARRAY_PLDP


.. autoattribute:: geosoft.gxapi.IP_ARRAY_PLPL


.. autoattribute:: geosoft.gxapi.IP_ARRAY_GRAD


.. autoattribute:: geosoft.gxapi.IP_ARRAY_WENNER


.. autoattribute:: geosoft.gxapi.IP_ARRAY_SCHLUMBERGER


.. autoattribute:: geosoft.gxapi.IP_ARRAY_UNKNOWN


.. autoattribute:: geosoft.gxapi.IP_ARRAY_3D


.. autoattribute:: geosoft.gxapi.IP_ARRAY_3D_PLDP


.. autoattribute:: geosoft.gxapi.IP_ARRAY_3D_PLPL


.. _IP_CHANNELS:

IP_CHANNELS constants
-----------------------------------------------------------------------

::

   Channels to display 

.. autoattribute:: geosoft.gxapi.IP_CHANNELS_DISPLAYED


.. autoattribute:: geosoft.gxapi.IP_CHANNELS_SELECTED


.. autoattribute:: geosoft.gxapi.IP_CHANNELS_ALL


.. _IP_DOMAIN:

IP_DOMAIN constants
-----------------------------------------------------------------------

::

   Types of Domains 

.. autoattribute:: geosoft.gxapi.IP_DOMAIN_NONE


.. autoattribute:: geosoft.gxapi.IP_DOMAIN_TIME


.. autoattribute:: geosoft.gxapi.IP_DOMAIN_FREQUENCY


.. autoattribute:: geosoft.gxapi.IP_DOMAIN_BOTH


.. _IP_DUPLICATE:

IP_DUPLICATE constants
-----------------------------------------------------------------------

::

   How to handle duplicates 

.. autoattribute:: geosoft.gxapi.IP_DUPLICATE_APPEND


.. autoattribute:: geosoft.gxapi.IP_DUPLICATE_OVERWRITE


.. _IP_FILTER:

IP_FILTER constants
-----------------------------------------------------------------------

::

   Fraser Filters 

.. autoattribute:: geosoft.gxapi.IP_FILTER_PANTLEG

::

   Regular pant-leg filter:    _!_  maxn:
   /\ `*`\ _\ `*`\ \   n1
   /\ `*`\ / \\ `*`\ \  n2
   /\ `*`\ /   \\ `*`\ \ n3
   :  : 

.. autoattribute:: geosoft.gxapi.IP_FILTER_PANTLEGP

::

   Regular pant-leg filter with top at first point:
   !  nscp:
   /\ `*`\ \   n1
   /\ `*`\ _\ `*`\ \  n2
   /\ `*`\ / \\ `*`\ \ n3
   :  : 

.. autoattribute:: geosoft.gxapi.IP_FILTER_PYRIAMID

::

   Regular pyramid filter:     _!_  maxn:
   /\ `*`\  \ `*`\ \   n1
   /\ `*`\  \ `*`\  \ `*`\ \  n2
   /\ `*`\  \ `*`\  \ `*`\  \ `*`\ \ n3
   :  : 

.. autoattribute:: geosoft.gxapi.IP_FILTER_PYRIAMIDP

::

   Regular pyramid filter      !  maxn:
   with peak on a point:      /\ `*`\ \   n1
   /\ `*`\  \ `*`\ \  n2
   /\ `*`\  \ `*`\  \ `*`\ \ n3
   :  : 

.. _IP_I2XIMPMODE:

IP_I2XIMPMODE constants
-----------------------------------------------------------------------

::

   Interpext Import Mode 

.. autoattribute:: geosoft.gxapi.IP_I2XIMPMODE_REPLACE

::

   Recreates the line from scratch. 

.. autoattribute:: geosoft.gxapi.IP_I2XIMPMODE_MERGE

::

   Looks for matching Tx1 and N values and
   replaces data in matching lines only. 

.. _IP_I2XINV:

IP_I2XINV constants
-----------------------------------------------------------------------

::

   Type of Inversion 

.. autoattribute:: geosoft.gxapi.IP_I2XINV_IMAGE


.. autoattribute:: geosoft.gxapi.IP_I2XINV_ZONGE


.. _IP_LINES:

IP_LINES constants
-----------------------------------------------------------------------

::

   Lines to display 

.. autoattribute:: geosoft.gxapi.IP_LINES_DISPLAYED


.. autoattribute:: geosoft.gxapi.IP_LINES_SELECTED


.. autoattribute:: geosoft.gxapi.IP_LINES_ALL


.. _IP_PLOT:

IP_PLOT constants
-----------------------------------------------------------------------

::

   Type of Plot 

.. autoattribute:: geosoft.gxapi.IP_PLOT_PSEUDOSECTION


.. autoattribute:: geosoft.gxapi.IP_PLOT_STACKEDSECTION


.. _IP_QCTYPE:

IP_QCTYPE constants
-----------------------------------------------------------------------

::

   Type of Measurement 

.. autoattribute:: geosoft.gxapi.IP_QCTYPE_RESISTIVITY

::

   Resistivity 

.. autoattribute:: geosoft.gxapi.IP_QCTYPE_IP

::

   IP 

.. _IP_STACK_TYPE:

IP_STACK_TYPE constants
-----------------------------------------------------------------------

::

   Spacing Types 

.. autoattribute:: geosoft.gxapi.IP_STACK_TYPE_MAP

::

   Use map-based spacing, and preserve the directions of the
   original lines by rotating the sections as desired to their true
   locations. (At present only N-S and E-W sections are supported). 

.. autoattribute:: geosoft.gxapi.IP_STACK_TYPE_EQUAL

::

   Spaces the sections equally, with enough room to
   guarantee no overlap with high N-values or closely spaced lines. 

.. autoattribute:: geosoft.gxapi.IP_STACK_TYPE_GEOGRAPHIC

::

   Now the same as IP_STACK_MAP 

.. _IP_STNSCALE:

IP_STNSCALE constants
-----------------------------------------------------------------------

::

   Station Scaling 

.. autoattribute:: geosoft.gxapi.IP_STNSCALE_NONE

::

   Station numbers become X or Y locations 

.. autoattribute:: geosoft.gxapi.IP_STNSCALE_ASPACE

::

   Multiply station numbers by the A spacing 

.. autoattribute:: geosoft.gxapi.IP_STNSCALE_VALUE

::

   Multiply by an input value. 

.. autoattribute:: geosoft.gxapi.IP_STNSCALE_FILE

::

   Look up locations from a CSV Line/Station/X/Y file 

.. _IP_SYS:

IP_SYS constants
-----------------------------------------------------------------------

::

   Instrument 

.. autoattribute:: geosoft.gxapi.IP_SYS_IPDATA


.. autoattribute:: geosoft.gxapi.IP_SYS_IP2


.. autoattribute:: geosoft.gxapi.IP_SYS_IP6


.. autoattribute:: geosoft.gxapi.IP_SYS_IP10


.. autoattribute:: geosoft.gxapi.IP_SYS_SYSCALR2


.. autoattribute:: geosoft.gxapi.IP_SYS_IPR11


.. autoattribute:: geosoft.gxapi.IP_SYS_IPR12


.. autoattribute:: geosoft.gxapi.IP_SYS_PHOENIX


.. autoattribute:: geosoft.gxapi.IP_SYS_PHOENIX_V2


.. autoattribute:: geosoft.gxapi.IP_SYS_ELREC_PRO


.. _IP_UBC_CONTROL:

IP_UBC_CONTROL constants
-----------------------------------------------------------------------

::

   Types of Domains 

.. autoattribute:: geosoft.gxapi.IP_UBC_CONTROL_NONE


.. autoattribute:: geosoft.gxapi.IP_UBC_CONTROL_DEFAULT


.. autoattribute:: geosoft.gxapi.IP_UBC_CONTROL_FILE


.. autoattribute:: geosoft.gxapi.IP_UBC_CONTROL_VALUE


.. autoattribute:: geosoft.gxapi.IP_UBC_CONTROL_LENGTH


.. _IP_PLDP_CONV:

IP_PLDP_CONV constants
-----------------------------------------------------------------------

::

   Types of Domains 

.. autoattribute:: geosoft.gxapi.IP_PLDP_CONV_CLOSE_RX


.. autoattribute:: geosoft.gxapi.IP_PLDP_CONV_MID_RX


.. autoattribute:: geosoft.gxapi.IP_PLDP_CONV_DISTANT_RX


	