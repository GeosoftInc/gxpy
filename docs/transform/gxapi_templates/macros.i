{% macro export_ref(type_name, ref_type, default_value) -%}
{{ ref_type }}::by_ref_value() : value_({{ default_value }}) {}
void gxExport{{ref_type}}()
{
class_<{{ ref_type }}>("{{ ref_type }}")
    .def(init<>())
	.def(init<{{ type_name }}>())
    .add_property("value", &{{ ref_type }}::get_value, &{{ ref_type }}::set_value);
}

{%- endmacro %}
