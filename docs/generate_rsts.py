import os
import inspect
import pydoc
from pkg_resources import parse_version
import geosoft.gxpy as gxpy
import geosoft.gxapi as gxa
import re

ver_add_re = re.compile(".*versionadded\:\:\s+([0-9\.]+)", re.MULTILINE)

def add_object_to_history(mod, object, name, collection, parent_name=None):
    if hasattr(object, '__doc__'):
        doc = str(object.__doc__)
        match = ver_add_re.search(doc)
        if match:
            ver_string = match.group(1)
            version = parse_version(ver_string)
            mod._version_history[version] = mod._version_history.get(version, {'classes': [], 'functions': []})
            if parent_name:
                mod._version_history[version][collection].append(":func:`{}.{}.{}`".format(mod.__name__, parent_name, name))
            else:
                if issubclass(object, BaseException):
                    mod._version_history[version][collection].append(":exc:`{}.{}`".format(mod.__name__, name))
                else:
                    mod._version_history[version][collection].append(":class:`{}.{}`".format(mod.__name__, name))

def sort_version_history(version_history):
    for key, val in version_history.items():
        val['classes'].sort()
        val['functions'].sort()

def parse_module_history(mod):
    mod._version_history = {}
    for fn_key, fn_value in inspect.getmembers(mod, pydoc._is_some_method):
        add_object_to_history(mod, fn_value, fn_key, 'functions')
    for cl_key, cl_value in inspect.getmembers(mod, inspect.isclass):
        add_object_to_history(mod, cl_value, cl_key, 'classes')
        for fn_key, fn_value in inspect.getmembers(cl_value, pydoc._is_some_method):
            add_object_to_history(mod, fn_value, fn_key, 'functions', parent_name=cl_key)
    sort_version_history(mod._version_history)
    mod._versions = reversed(sorted(mod._version_history.keys()))


def gen_version_history(j2env, output_dir):
    parse_module_history(gxa)
    parse_module_history(gxpy)
    modules = [gxa, gxpy]
    template = j2env.get_template('version_history.rst')
    output_file = os.path.join(output_dir, 'version_history.rst')
    with open(output_file, 'w+') as f:
        f.write(template.render(modules=modules))


def generate():
    from jinja2 import Environment, FileSystemLoader
    global __global_collection

    dir = os.path.split(__file__)[0]
    templates_dir = os.path.join(dir,'templates')
    j2env = Environment(loader=FileSystemLoader(templates_dir), 
						trim_blocks = True,
						lstrip_blocks = True)

    gen_version_history(j2env, dir)
