Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
* :ref:`toc`

Introduction
============

The geosoft.gxpy package
------------------------

.. note::
   This package is a work in progress to wrap the generated GX API in an API that can be used to write 
   code in a more pythonic style. For this reason the classes in module do not have the same degree of stability
   between different release versions. That being said, a reasonable effort will be made to maintain API stability 
   unless there is a good enough reason to break it.

:doc:`More... </geosoft.gxpy>`


The GXContext class
-------------------

.. autoclass:: geosoft.gxapi.GXContext
   :members:

.. note::
	There should be a single instance of this class constructed in a global location prior to using any other GX API 
	classes and their methods. By default the module will only function if an installed *Oasis montaj* product is found since
	it loads the dlls that are shipped with *Oasis montaj* for the actual functionality.

	It is possible to redirect the location of dlls used by setting the ``GX_GEOSOFT_BIN_PATH`` environment variable. 
	This can be done either using the normal *Windows* mechanisms (i.e. via ``set`` command line or *Advanced System Settings->Environment Variables*)
	or directly in Python code by using ``os.putenv("GX_GEOSOFT_BIN_PATH", ...)``. If the intention is to use the public standalone API that is shipped with *GX Developer* then this should be set to wherever
	the ``GeosoftFiles`` redistributable folder is copied or installed.
	
Exceptions
----------

.. autoexception:: geosoft.gxapi.GXRunTimeError


Helper classed to pass immutable values by reference
----------------------------------------------------

.. autoclass:: geosoft.gxapi.str_ref

.. autoclass:: geosoft.gxapi.bool_ref

.. autoclass:: geosoft.gxapi.int_ref

.. autoclass:: geosoft.gxapi.float_ref


Each of the classes above can be used to pass these immutable types by reference to the GX API.
Instances of the objects has a ``value`` property holding a reference to the immutable object.

Default instances will be intialized with dummy values for ``float_ref`` and ``int_ref``, an empty string
for ``str_ref`` and ``False`` for ``bool_ref``. One can also set the value during intialization or assigning 
to the ``value`` property. 

Example usage:

.. code-block:: python

   import geosoft.gxapi as gxapi

	ctx = gxapi.GXContext.create("sample", "1.0")
	_3dn = gxapi.GX3DN.create(ctx)

	distance = gxapi.float_ref() # value property will be equal to gxapi.rDUMMY
	rot1 = gxapi.float_ref(1.01) # value property will be equal to 1.01
	rot2 = gxapi.float_ref(2.0)  # value property will be equal to 2.0
	rot2.value = 4  # value property will be equal to 4.0
	
	_3dn.get_point_of_view(distance, rot1, rot2)

	print(distance.value) # value property will now be 8.0
	print(rot1.value) # value property will now be 0.0 
	print(rot2.value) # value property will now be 0.0

Other Classes in the GX API
---------------------------

{% for gxclass in classes %}{% if not gxclass.name == "GEO" and not gxclass.name == "GEOSOFT" %} 
{% set class_name = "GX" ~ gxclass.name %}

{{ class_name }} class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.{{ class_name }}
	:noindex:
	
:ref:`More... <{{ class_name }}>`

{% endif %}{% endfor %}
   

Global Constants
================

.. include:: GXGEOSOFT.rst


