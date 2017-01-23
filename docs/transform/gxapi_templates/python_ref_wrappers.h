#pragma once

typedef std::vector<double> float_list;
typedef std::vector<int32_t> int_list;

template<typename T>
struct by_ref_value
{
public:
	inline by_ref_value();
	inline by_ref_value(const T& value) : value_(value) { }
	inline by_ref_value(const by_ref_value<T> & other) { value_ = other.value_; }

	operator const T&() const { return value_; }
	operator T&() { return value_; }

	T get_value() { return value_; }
	void set_value(const T& value) { value_ = value; }

private:
	T value_;
};

typedef by_ref_value<double> float_ref;
typedef by_ref_value<int32_t> int_ref;
typedef by_ref_value<bool> bool_ref;
typedef by_ref_value<std::wstring> str_ref;
{% for gxclass in classes %}

{% for definition in gxclass.definitions.definition %}{% if not definition.name == "GEO_BOOL" and not definition.constant and not definition.null_handle %}
typedef by_ref_value<{{ definition.name }}> {{ definition.name }}_ref;
{% endif %}{% endfor %}

{% endfor %}

