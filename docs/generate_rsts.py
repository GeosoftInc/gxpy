import os
import inspect
from pkg_resources import parse_version

import geosoft.gxpy as gxpy
import geosoft.gxapi as gxa
import re

from docstring_info import parse_docstring

min_version = parse_version("8.5")
ver_add_re = re.compile(".*versionadded\:\:\s+([0-9\.]+)", re.MULTILINE)

def _is_some_method(obj):
    return (inspect.isfunction(obj) or
            inspect.ismethod(obj) or
            inspect.isbuiltin(obj) or
            inspect.ismethoddescriptor(obj))

def get_short_desc(str):
    lines = [str.strip() for str in str.splitlines()]
    for line in lines:
        if line and not (
                (line.endswith(':') and '->' in line) or
                'parsed-literal' in line):
            return line
    return ''

def get_short_desc_from_object(object):
    if not object.__doc__:
        return ''
    info = parse_docstring(object.__doc__)
    short_desc = get_short_desc(info['short_description'])
    if not short_desc:
        short_desc = get_short_desc(info['long_description'])
    return short_desc

def add_object_to_history(mod, version_history, object, name, collection, parent_name=None):
    if not name.startswith('_') and hasattr(object, '__doc__'):
        doc = str(object.__doc__)
        match = ver_add_re.search(doc)
        if match:
            ver_string = match.group(1)
            version = parse_version(ver_string)
            if version >= min_version:
                version_history[version] = version_history.get(version, {'classes': [], 'functions': []})

                short_desc = get_short_desc_from_object(object)
                if parent_name:
                    version_history[version][collection].append(":func:`{}.{}.{}` {}"\
                                                                .format(mod.__name__, parent_name, name, short_desc))
                else:
                    if _is_some_method(object):
                        version_history[version][collection].append(":func:`{}.{}` {}"
                                                                    .format(mod.__name__, name, short_desc))
                    elif inspect.isclass(object) and issubclass(object, BaseException):
                        version_history[version][collection].append(":exc:`{}.{}` {}"
                                                                    .format(mod.__name__, name, short_desc))
                    else:
                        version_history[version][collection].append(":class:`{}.{}` {}"\
                                                                    .format(mod.__name__, name, short_desc))

def sort_version_history(version_history):
    for key, val in version_history.items():
        val['classes'].sort()
        val['functions'].sort()

# get_class_that_defined_method implementation from here:
# http://stackoverflow.com/questions/3589311/get-defining-class-of-unbound-method-object-in-python-3/25959545#25959545
def get_class_that_defined_method(meth):
    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
            if cls.__dict__.get(meth.__name__) is meth:
                return cls
        meth = meth.__func__ # fallback to __qualname__ parsing
    if inspect.isfunction(meth):
        mod = inspect.getmodule(meth)
        if mod is None:
            return None
        cls = getattr(mod,
                      meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0], None)
        if cls is not None and isinstance(cls, type):
            return cls
    return None # not required since None would have been implicitly returned anyway

def does_class_implement_method(cls, meth):
    cls_from_meth = get_class_that_defined_method(meth)
    return cls_from_meth is None or cls is cls_from_meth

def parse_module_history(mod, version_history):
    functions = inspect.getmembers(mod, _is_some_method)
    for fn_key, fn_value in functions:
        if does_class_implement_method(mod, fn_value):
            add_object_to_history(mod, version_history, fn_value, fn_key, 'functions')
    classes = inspect.getmembers(mod, inspect.isclass)
    for cl_key, cl_value in classes:
        if not cl_key.startswith('_'):
            add_object_to_history(mod, version_history, cl_value, cl_key, 'classes')
            cl_functions = inspect.getmembers(cl_value, _is_some_method)
            for fn_key, fn_value in cl_functions:
                if does_class_implement_method(cl_value, fn_value):
                    add_object_to_history(mod, version_history, fn_value, fn_key, 'functions', parent_name=cl_key)
    sort_version_history(version_history)

def collect_gxa_version_history():
    gxa._version_history = {}
    parse_module_history(gxa, gxa._version_history)
    gxa._versions = reversed(sorted(gxa._version_history.keys()))

def collect_gxpy_version_history():
    gxpy._version_history = {}
    for attr, value in gxpy.__dict__.items():
        if not attr.startswith("_") and inspect.ismodule(value):
            parse_module_history(value, gxpy._version_history)
    gxpy._versions = reversed(sorted(gxpy._version_history.keys()))

def gen_version_history(j2env, output_dir):
    collect_gxpy_version_history()
    collect_gxa_version_history()
    modules = [gxpy, gxa]
    template = j2env.get_template('version_history.rst')
    output_file = os.path.join(output_dir, 'version_history.rst')
    with open(output_file, 'w+') as f:
        f.write(template.render(modules=modules))

def gen_version_history(j2env, output_dir):
    collect_gxpy_version_history()
    collect_gxa_version_history()
    modules = [gxpy, gxa]
    template = j2env.get_template('version_history.rst')
    output_file = os.path.join(output_dir, 'version_history.rst')
    with open(output_file, 'w+') as f:
        f.write(template.render(modules=modules))


def gen_gxapi_rsts(j2env, output_dir):
    template = j2env.get_template('gxapi_class.rst')
    classes = inspect.getmembers(gxa, inspect.isclass)
    for cl_key, cl_value in classes:
        if (cl_key.startswith("GX") 
            and not cl_key == "GXContext"
            and not cl_key == "GXCancel" 
            and not cl_key == "GXExit" 
            and not cl_key == "GXError" 
            and not cl_key == "GXAPIError"): 
             with open(cl_key + '.rst', 'w+') as f:
                 f.write(template.render(class_name=cl_key, definitions = {}))

def gen_gxapi_toc(j2env, output_dir):
    template = j2env.get_template('geosoft.gxapi.classes.rst')
    gxa_classes = inspect.getmembers(gxa, inspect.isclass)
    classes = [c for c, _ in gxa_classes if not c.startswith('_') and not c.startswith('ref_') and not c.endswith('_ref') and
               c != 'GXCancel' and c != 'GXAPIError' and c != 'GXError' and c != 'GXExit' and c != 'GXContext']
    with open('geosoft.gxapi.classes.rst', 'w+') as f:
        f.write(template.render(classes=['geosoft.gxapi', 'GXGEOSOFT'] + classes))

def gen_gxpy_rsts(j2env, output_dir):

    # remove stale rst files
    for fn in list(os.listdir()):
        if not os.path.isdir(fn):
            if fn.startswith('geosoft.gxpy.') and fn.endswith('.rst'):
                os.remove(fn)

    modules = sorted([(k, get_short_desc_from_object(v)) for k, v in gxpy.__dict__.items() if not k.startswith("_") and inspect.ismodule(v)])
    with open('geosoft.gxpy.rst', 'w+') as f:
        template = j2env.get_template('geosoft.gxpy.rst')
        f.write(template.render(modules=modules))
    template = j2env.get_template('geosoft.gxpy.mod.rst')
    for module in modules:
        with open('geosoft.gxpy.' + module[0] + '.rst', 'w+') as f:
            f.write(template.render(module=module))

def generate():
    from jinja2 import Environment, FileSystemLoader
    global __global_collection

    dir = os.path.split(__file__)[0]
    templates_dir = os.path.join(dir,'templates')
    j2env = Environment(loader=FileSystemLoader(templates_dir), 
						trim_blocks = True,
						lstrip_blocks = True)


    gen_gxpy_rsts(j2env, dir)
    #gen_gxapi_rsts(j2env, dir)
    gen_gxapi_toc(j2env, dir)
    gen_version_history(j2env, dir)

if __name__ == "__main__":
    generate()
