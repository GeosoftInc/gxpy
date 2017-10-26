### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMETA:
    """
    GXMETA class.

    A `GXMETA` object contains hierarchical organized metadata
    of any type, including other objects.  `GXMETA` information
    is organized in an XML-like structure based on a data
    schema that describes the data hierarchy.   `GXMETA` objects
    are used by many entities that need to store metadata
    specific to the entities or to the application.
    
    Metadata can be saved in databases and maps, as well as in
    channels, lines, views and groups.  Oasis montaj objects
    can be queried for their associated metadata, and if it
    exists, the metadata can be retrieved and utilized by
    other Oasis montaj processes.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMETA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMETA`
        
        :returns: A null `GXMETA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMETA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMETA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Attribute



    def create_attrib(self, name, ph_class, ph_type):
        """
        Create an attribute
        """
        ret_val = self._wrapper.create_attrib(name.encode(), ph_class, ph_type)
        return ret_val




    def delete_attrib(self, ph_attribute):
        """
        Delete Attrib from `GXMETA`.
        """
        self._wrapper.delete_attrib(ph_attribute)
        




# Browser



    def set_attribute_editable(self, ph_attribute, editable):
        """
        Allow/disallow an attribute to be editable in the browser
        """
        self._wrapper.set_attribute_editable(ph_attribute, editable)
        




    def set_attribute_visible(self, ph_attribute, visible):
        """
        Allow/disallow an attribute to be visible in the browser
        """
        self._wrapper.set_attribute_visible(ph_attribute, visible)
        




# Class



    def create_class(self, name, ph_class):
        """
        Create a class
        """
        ret_val = self._wrapper.create_class(name.encode(), ph_class)
        return ret_val




    def delete_class(self, ph_class):
        """
        Delete Class from `GXMETA`.
        """
        self._wrapper.delete_class(ph_class)
        




# Core



    def copy(self, source_meta):
        """
        Copy a `GXMETA` to another
        """
        self._wrapper.copy(source_meta._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create
        """
        ret_val = gxapi_cy.WrapMETA.create(GXContext._get_tls_geo())
        return GXMETA(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create a `GXMETA` Object from a `GXBF`
        """
        ret_val = gxapi_cy.WrapMETA.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXMETA(ret_val)






    def serial(self, bf):
        """
        Serialize an `GXMETA` to a `GXBF`
        """
        self._wrapper.serial(bf._wrapper)
        




# Get Data



    def find_data(self, ph_object, ph_attrib):
        """
        Does this meta/attribute have a value ?
        """
        ret_val = self._wrapper.find_data(ph_object, ph_attrib)
        return ret_val




    def get_attrib_bool(self, ph_object, ph_attrib, value):
        """
        Get a boolean value to an attribute
        """
        value.value = self._wrapper.get_attrib_bool(ph_object, ph_attrib, value.value)
        




    def get_attrib_enum(self, ph_object, ph_attrib, value):
        """
        Get an enum value to an attribute (as an integer)
        """
        value.value = self._wrapper.get_attrib_enum(ph_object, ph_attrib, value.value)
        




    def get_attrib_int(self, ph_object, ph_attrib, value):
        """
        Get an integer value to an attribute
        """
        value.value = self._wrapper.get_attrib_int(ph_object, ph_attrib, value.value)
        




    def get_attrib_double(self, ph_object, ph_attrib, value):
        """
        Get an integer value to an attribute
        """
        value.value = self._wrapper.get_attrib_double(ph_object, ph_attrib, value.value)
        




    def get_attrib_string(self, ph_object, ph_attrib, value):
        """
        Get a string value to an attribute
        """
        value.value = self._wrapper.get_attrib_string(ph_object, ph_attrib, value.value.encode())
        




    def has_value(self, ph_object, ph_attrib):
        """
        Does this meta/attribute have a value set?
        """
        ret_val = self._wrapper.has_value(ph_object, ph_attrib)
        return ret_val




# Import/Export



    def export_table_csv(self, ph_class, file):
        """
        Export all items in a class as a CSV
        """
        self._wrapper.export_table_csv(ph_class, file.encode())
        




    def import_table_csv(self, ph_class, file):
        """
        Import a CSV into a class as items.

        **Note:**

        Field names in the CSV file that match attribute names in the class will be
        imported into table entries in the class.  Usually this will be used with
        a class created using the hCreateTable_SCHEMA method so that the contents of
        class can be viewed as a table.
        """
        self._wrapper.import_table_csv(ph_class, file.encode())
        




    def write_text(self, wa):
        """
        Write the entire meta as a text file
        """
        self._wrapper.write_text(wa._wrapper)
        




# Item



    def delete_all_items(self, ph_class):
        """
        Delete all items in this class.
        """
        self._wrapper.delete_all_items(ph_class)
        




    def delete_item(self, ph_item):
        """
        Delete item from `GXMETA`.
        """
        self._wrapper.delete_item(ph_item)
        




    def h_creat_item(self, name, p3):
        """
        Creates item in Class.
        """
        ret_val = self._wrapper.h_creat_item(name.encode(), p3)
        return ret_val




    def h_get_next_item(self, ph_class, ph_token):
        """
        Count the number of items in a class
        """
        ret_val = self._wrapper.h_get_next_item(ph_class, ph_token)
        return ret_val




# Object



    def get_attrib_obj(self, ph_object, ph_attrib, obj):
        """
        Get an object from an attribute
        """
        self._wrapper.get_attrib_obj(ph_object, ph_attrib, obj)
        




    def set_attrib_obj(self, ph_object, ph_attrib, obj):
        """
        Set an object to an attribute
        """
        self._wrapper.set_attrib_obj(ph_object, ph_attrib, obj)
        




# Set Data



    def set_attrib_bool(self, ph_object, ph_attrib, value):
        """
        Set a boolean value to an attribute
        """
        self._wrapper.set_attrib_bool(ph_object, ph_attrib, value)
        




    def set_attrib_enum(self, ph_object, ph_attrib, value):
        """
        Set an enum value to an attribute (as an integer)
        """
        self._wrapper.set_attrib_enum(ph_object, ph_attrib, value)
        




    def set_attrib_int(self, ph_object, ph_attrib, value):
        """
        Set an integer value to an attribute
        """
        self._wrapper.set_attrib_int(ph_object, ph_attrib, value)
        




    def set_attrib_double(self, ph_object, ph_attrib, value):
        """
        Set an integer value to an attribute
        """
        self._wrapper.set_attrib_double(ph_object, ph_attrib, value)
        




    def set_attrib_string(self, ph_object, ph_attrib, value):
        """
        Set a string value to an attribute
        """
        self._wrapper.set_attrib_string(ph_object, ph_attrib, value.encode())
        




    def set_empty_attrib(self, ph_object, ph_attrib):
        """
        Set an empty attribute data holder
        """
        self._wrapper.set_empty_attrib(ph_object, ph_attrib)
        




# Transfer



    def h_copy_across_attribute(self, source_meta, ph_attribute):
        """
        Copy an Attribute from one `GXMETA` to another
        """
        ret_val = self._wrapper.h_copy_across_attribute(source_meta._wrapper, ph_attribute)
        return ret_val




    def h_copy_across_class(self, source_meta, ph_class):
        """
        Copy a Class from one `GXMETA` to another

        **Note:**

        This will copy all parent classes as well.
        """
        ret_val = self._wrapper.h_copy_across_class(source_meta._wrapper, ph_class)
        return ret_val




    def h_copy_across_data(self, source_meta, ph_data):
        """
        Copy a Data value from one `GXMETA` to another
        """
        ret_val = self._wrapper.h_copy_across_data(source_meta._wrapper, ph_data)
        return ret_val




    def h_copy_across_item(self, source_meta, ph_item):
        """
        Copy an Item from one `GXMETA` to another
        """
        ret_val = self._wrapper.h_copy_across_item(source_meta._wrapper, ph_item)
        return ret_val




    def h_copy_across_type(self, source_meta, ph_type):
        """
        Copy a Type from one `GXMETA` to another

        **Note:**

        Classes and parent types will also be copied.
        """
        ret_val = self._wrapper.h_copy_across_type(source_meta._wrapper, ph_type)
        return ret_val




    def move_datas_across(self, source_meta, ph_i_obj, ph_o_obj):
        """
        Moves data items from one `GXMETA` to another
        """
        self._wrapper.move_datas_across(source_meta._wrapper, ph_i_obj, ph_o_obj)
        




# Type



    def create_type(self, name, ph_class, ph_type):
        """
        Create an attribute
        """
        ret_val = self._wrapper.create_type(name.encode(), ph_class, ph_type)
        return ret_val




    def delete_data(self, ph_data):
        """
        Delete Data from `GXMETA`.
        """
        self._wrapper.delete_data(ph_data)
        




    def delete_type(self, ph_type):
        """
        Delete Type from `GXMETA`.
        """
        self._wrapper.delete_type(ph_type)
        




# UMN



    def get_obj_name(self, ph_object, name):
        """
        Get the name of this item.
        """
        name.value = self._wrapper.get_obj_name(ph_object, name.value.encode())
        




    def resolve_umn(self, umn):
        """
        Resolve a Unique Meta Name (UMN) and find the token
        """
        ret_val = self._wrapper.resolve_umn(umn.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer