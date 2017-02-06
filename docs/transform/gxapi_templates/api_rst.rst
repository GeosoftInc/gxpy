=======================================================================================================================
{{ cl.name }}{% if cl.handlename %}({{ cl.handlename }}){% endif %} {% if cl.nogxh %}nogxh{% endif %} {% if cl.nocsharp %}nocsharp{% endif %} {% if cl.nocpp %}nocpp{% endif %}

=======================================================================================================================

{{ cl.description|clean_doc }}

{% if cl.notes and not cl.notes == 'None' %}
Notes
=======================================================================================================================
{{ cl.notes|clean_doc }}
{% endif %}

{% for definition in cl.definitions.definition %}
{% if loop.first %}
Defines
=======================================================================================================================
{% endif %}

Define {{ definition.name }} {% if definition.constant %}const{% endif %} {% if definition.single_constant %}single{% endif %} {% if definition.null_handle %}null{% endif %} {% if definition.cpp_prefix %}cpp_prefix={{ definition.cpp_prefix }}{% endif %}

-----------------------------------------------------------------------------------------------------------------------
{% if definition.description %}
{{ definition.description|clean_doc }}

{% endif %}
{% if not definition.null_handle %}{% for defined_value in definition.defined_value %}
:def:{{ defined_value.name }} type={{ defined_value.get_spec_type() }} value={{ defined_value.val }}
{% if defined_value.description %}
{{ defined_value.description|clean_doc }}
{% endif %}
{% endfor %}{% endif %}
{% endfor %}

{% for methodgroup in cl.methodgroups.methodgroup %}
Methods {% if methodgroup.name %}({{ methodgroup.name }}){% endif %}

=======================================================================================================================

{% for methodgroup in cl.methodgroups.methodgroup %}
{% for method in methodgroup.method %}
:func {{ method.name }}:
{{ method.description }}
{% for param in method.parameters.parameter %}
:param p{{ loop.index }}: {{ param.description|clean_doc }}
:type p{{ loop.index }}: {{ param.type }}
{% endfor %}
{% if method.returnval.description %}
:returns: {{ method.returnval.description|clean_doc }}
{% endif %}
:rtype: {{ method.returnval.type|clean_doc }}
{% endfor %}
{% endfor %}
{% endfor %}
