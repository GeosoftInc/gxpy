import os
import re
import textwrap
from jinja2 import Environment, FileSystemLoader

import gxgenutils

global global_collection
global_collection = gxgenutils.object_from_pickled_file('pyxb_all.pickled')

def gen_replacements():
    replace_dict = {}
    for key, _ in global_collection.known_classes.items():
        replace_dict[key] = ":class:`{}`".format(key)
    for key, _ in global_collection.known_class_handles.items():
        replace_dict[key] = ":class:`{}`".format(key)
    for key, _ in global_collection.known_definitions.items():
        replace_dict[key] = ":def:`{}`".format(key)
    for key, _ in global_collection.known_methods.items():
        replace_dict[key] = ":func:`{}`".format(key)
    for key, _ in global_collection.known_definition_values.items():
        replace_dict[key] = ":def_val:`{}`".format(key)


    # Sort by descending length to ensure correct replacement order with substring
    keys = list(replace_dict.keys())
    keys.sort(key=lambda x: len(x), reverse=True)
    pattern = re.compile(r'\b(' + '|'.join(keys) + r')\b')
    return pattern, replace_dict

repl_pat, repl_dict = gen_replacements()

def fix_doc_refs(text):
    text = text.replace('</define>', '')
    text = text.replace('<define>', '')
    text = text.replace('.GXH', '')
    text = repl_pat.sub(lambda x: repl_dict[re.escape(x.group())], text)
    return text.strip()


j2env = None
local_dir = os.path.split(__file__)[0]
templates_dir = os.path.join(local_dir, 'gxapi_templates')
j2env = Environment(loader=FileSystemLoader(templates_dir),
                    trim_blocks=True,
                    lstrip_blocks=True)
do_indent = j2env.filters['indent']


def clean_quote(value):
    value = value.strip()
    if '\n' in value:
        return '"""\n{}\n"""'.format(value)
    elif not '"' in value:
        return '"{}"'.format(value)
    elif not "'" in value:
        return "'{}'".format(value)
    else:
        return '"{}"'.format(value.replace('"', r'\"'))


def clean_doc(value, indent=0):

    #if value == 'real':
    #    return 'double'
    #if value == 'int':
    #    return 'int32_t'
    doc = textwrap.dedent(value)
    doc = fix_doc_refs(doc)

    # replace all standalone \ characters with double escapes \\
    doc = re.sub(r'(?<!\\)(\\[^\\])', r'\\\1', doc)

    # replace all end of line standalone \ characters with a double escapes \\
    doc = re.sub(r'(?<!\\)(\\$)', r'\\\1', doc)

    if '\n' in doc and indent > 0:
        doc = do_indent('{}\n"""'.format(doc), indent, True)
        return '"""\n{}'.format(doc)
    else:
        return clean_quote(doc)


j2env.filters['clean_doc'] = clean_doc
j2env.filters['clean_quote'] = clean_quote

core_set = set([
    '3DN',
    '3DV',
    'AGG',
    'BF',
    'DAT',
    'DATALINKD',
    'DATAMINE',
    'DB',
    'DBREAD',
    'DBWRITE',
    'DSEL',
    'E3DV',
    'EXT',
    'GEO',
    'GEOSOFT',
    'GEOSTRING',
    'GIS',
    'HGD',
    'HXYZ',
    'IGRF',
    'IMG',
    'IMU',
    'IPJ',
    'ITR',
    'LAYOUT',
    'LL2',
    'LPT',
    'LST',
    'LTB',
    'MAP',
    'MAPL',
    'MAPTEMPLATE',
    'MATH',
    'META',
    'MVIEW',
    'MVU',
    'MXD',
    'PAT',
    'PG',
    'PJ',
    'PLY',
    'RA',
    'REG',
    'SBF',
    'ST',
    'ST2',
    'STR',
    'SURFACE',
    'SURFACEITEM',
    'SYS',
    'TB',
    'TPAT',
    'TR',
    'USERMETA',
    'VA',
    'VECTOR3D',
    'VM',
    'VOX',
    'VOXD',
    'VOXE',
    'VULCAN',
    'VV',
    'WA'
])

def generate_class_as_rst(cl, template):
    if cl.name in core_set:
        branch = 'core'
    else:
        branch = 'desk'
    with open('../../../gxapi/spec/' + branch + '/' + cl.name + '.py', 'w+') as f:
        f.write(template.render(cl=cl))

def generate_spec():
    template = j2env.get_template('api_spec.pyj')
    for _, cl in global_collection.known_classes.items():
        generate_class_as_rst(cl, template)


if __name__ == "__main__":
    generate_spec()


