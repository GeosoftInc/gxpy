import os
import re


from gxgenutils import *


def generate_api_as_yml(j2env, dir):
    pass

def generate():
    from jinja2 import Environment, FileSystemLoader
    global __global_collection

    dir = os.path.split(__file__)[0]
    templates_dir = os.path.join(dir,'templates')
    j2env = Environment(loader=FileSystemLoader(templates_dir), 
						trim_blocks = True,
						lstrip_blocks = True)


    generate_api_as_yml(j2env, dir)

if __name__ == "__main__":
    global_collection = object_from_pickled_file('pyxb_all.pickled')
    generate()