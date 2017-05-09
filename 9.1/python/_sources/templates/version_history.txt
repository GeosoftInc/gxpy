{% for mod  in modules %}
{{ mod.__name__ }} module history
==========================================

{% for ver in mod._versions %}{% set contents = mod._version_history[ver] %} {% set classes = contents['classes'] %} {% set funcs = contents['functions'] %}

Version {{ ver }}
-----------------

New Classes
^^^^^^^^^^^

{% for cl in classes %}
{{ cl }}

{% endfor %}

New Functions
^^^^^^^^^^^^^

{% for fn in funcs %}
{{ fn }}

{% endfor %}

{% endfor %}
{% endfor %}
