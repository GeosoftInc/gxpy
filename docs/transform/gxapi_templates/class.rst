{% if not gxclass.name == "GEOSOFT" %} 
{% set class_name = "GX" ~ gxclass.name %}

.. _{{ class_name }}:

{{ class_name }} class
==================================

.. autoclass:: geosoft.gxapi.{{ class_name }}
   :members:
{% else %}
.. version:

version constant
----------------

.. autoattribute:: geosoft.gxapi.version

{% endif %}

{% for definition in gxclass.definitions.definition %}{% if not definition.name == "GEO_BOOL" and not definition.null_handle %}
.. _{{ definition.name }}:

{{ definition.name }} constant{% if not definition.single_constant %}s{% endif %}

-----------------------------------------------------------------------

{% if not definition.single_constant and definition.description %}
::

{{ definition.get_sphinx_docstring()|indent(3, true) }} 
{% endif %}

{% for defined_value in definition.defined_value %}
.. autoattribute:: geosoft.gxapi.{{ defined_value.name }}

{% if definition.single_constant and definition.description %}
::

{{ definition.get_sphinx_docstring()|indent(3, true) }} 
{% elif defined_value.description %}
::

{{ defined_value.get_sphinx_docstring()|indent(3, true) }} 
{% endif %}

{% endfor %}
{% endif %}{% endfor %}	
