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

    A :class:`geosoft.gxapi.GXMETA` object contains hierarchical organized metadata
    of any type, including other objects.  :class:`geosoft.gxapi.GXMETA` information
    is organized in an XML-like structure based on a data
    schema that describes the data hierarchy.   :class:`geosoft.gxapi.GXMETA` objects
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXMETA`
        
        :returns: A null :class:`geosoft.gxapi.GXMETA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMETA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMETA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Attribute



    def create_attrib(self, p2, p3, p4):
        """
        Create an attribute
        """
        ret_val = self._wrapper.create_attrib(p2.encode(), p3, p4)
        return ret_val




    def delete_attrib(self, p2):
        """
        Delete Attrib from :class:`geosoft.gxapi.GXMETA`.
        """
        self._wrapper.delete_attrib(p2)
        




# Browser



    def set_attribute_editable(self, p2, p3):
        """
        Allow/disallow an attribute to be editable in the browser
        """
        self._wrapper.set_attribute_editable(p2, p3)
        




    def set_attribute_visible(self, p2, p3):
        """
        Allow/disallow an attribute to be visible in the browser
        """
        self._wrapper.set_attribute_visible(p2, p3)
        




# Class



    def create_class(self, p2, p3):
        """
        Create a class
        """
        ret_val = self._wrapper.create_class(p2.encode(), p3)
        return ret_val




    def delete_class(self, p2):
        """
        Delete Class from :class:`geosoft.gxapi.GXMETA`.
        """
        self._wrapper.delete_class(p2)
        




# Core



    def copy(self, p2):
        """
        Copy a :class:`geosoft.gxapi.GXMETA` to another
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create
        """
        ret_val = gxapi_cy.WrapMETA.create(GXContext._get_tls_geo())
        return GXMETA(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create a :class:`geosoft.gxapi.GXMETA` Object from a :class:`geosoft.gxapi.GXBF`
        """
        ret_val = gxapi_cy.WrapMETA.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXMETA(ret_val)






    def serial(self, p2):
        """
        Serialize an :class:`geosoft.gxapi.GXMETA` to a :class:`geosoft.gxapi.GXBF`
        """
        self._wrapper.serial(p2._wrapper)
        




# Get Data



    def find_data(self, p2, p3):
        """
        Does this meta/attribute have a value ?
        """
        ret_val = self._wrapper.find_data(p2, p3)
        return ret_val




    def get_attrib_bool(self, p2, p3, p4):
        """
        Get a boolean value to an attribute
        """
        p4.value = self._wrapper.get_attrib_bool(p2, p3, p4.value)
        




    def get_attrib_enum(self, p2, p3, p4):
        """
        Get an enum value to an attribute (as an integer)
        """
        p4.value = self._wrapper.get_attrib_enum(p2, p3, p4.value)
        




    def get_attrib_int(self, p2, p3, p4):
        """
        Get an integer value to an attribute
        """
        p4.value = self._wrapper.get_attrib_int(p2, p3, p4.value)
        




    def get_attrib_double(self, p2, p3, p4):
        """
        Get an integer value to an attribute
        """
        p4.value = self._wrapper.get_attrib_double(p2, p3, p4.value)
        




    def get_attrib_string(self, p2, p3, p4):
        """
        Get a string value to an attribute
        """
        p4.value = self._wrapper.get_attrib_string(p2, p3, p4.value.encode())
        




    def has_value(self, p2, p3):
        """
        Does this meta/attribute have a value set?
        """
        ret_val = self._wrapper.has_value(p2, p3)
        return ret_val




# Import/Export



    def export_table_csv(self, p2, p3):
        """
        Export all items in a class as a CSV
        """
        self._wrapper.export_table_csv(p2, p3.encode())
        




    def import_table_csv(self, p2, p3):
        """
        Import a CSV into a class as items.

        **Note:**

        Field names in the CSV file that match attribute names in the class will be
        imported into table entries in the class.  Usually this will be used with
        a class created using the hCreateTable_SCHEMA method so that the contents of
        class can be viewed as a table.
        """
        self._wrapper.import_table_csv(p2, p3.encode())
        




    def write_text(self, p2):
        """
        Write the entire meta as a text file
        """
        self._wrapper.write_text(p2._wrapper)
        




# Item



    def delete_all_items(self, p2):
        """
        Delete all items in this class.
        """
        self._wrapper.delete_all_items(p2)
        




    def delete_item(self, p2):
        """
        Delete item from :class:`geosoft.gxapi.GXMETA`.
        """
        self._wrapper.delete_item(p2)
        




    def h_creat_item(self, p2, p3):
        """
        Creates item in Class.
        """
        ret_val = self._wrapper.h_creat_item(p2.encode(), p3)
        return ret_val




    def h_get_next_item(self, p2, p3):
        """
        Count the number of items in a class
        """
        ret_val = self._wrapper.h_get_next_item(p2, p3)
        return ret_val




# Object



    def get_attrib_obj(self, p2, p3, p4):
        """
        Get an object from an attribute
        """
        self._wrapper.get_attrib_obj(p2, p3, p4)
        




    def set_attrib_obj(self, p2, p3, p4):
        """
        Set an object to an attribute
        """
        self._wrapper.set_attrib_obj(p2, p3, p4)
        




# Set Data



    def set_attrib_bool(self, p2, p3, p4):
        """
        Set a boolean value to an attribute
        """
        self._wrapper.set_attrib_bool(p2, p3, p4)
        




    def set_attrib_enum(self, p2, p3, p4):
        """
        Set an enum value to an attribute (as an integer)
        """
        self._wrapper.set_attrib_enum(p2, p3, p4)
        




    def set_attrib_int(self, p2, p3, p4):
        """
        Set an integer value to an attribute
        """
        self._wrapper.set_attrib_int(p2, p3, p4)
        




    def set_attrib_double(self, p2, p3, p4):
        """
        Set an integer value to an attribute
        """
        self._wrapper.set_attrib_double(p2, p3, p4)
        




    def set_attrib_string(self, p2, p3, p4):
        """
        Set a string value to an attribute
        """
        self._wrapper.set_attrib_string(p2, p3, p4.encode())
        




    def set_empty_attrib(self, p2, p3):
        """
        Set an empty attribute data holder
        """
        self._wrapper.set_empty_attrib(p2, p3)
        




# Transfer



    def h_copy_across_attribute(self, p2, p3):
        """
        Copy an Attribute from one :class:`geosoft.gxapi.GXMETA` to another
        """
        ret_val = self._wrapper.h_copy_across_attribute(p2._wrapper, p3)
        return ret_val




    def h_copy_across_class(self, p2, p3):
        """
        Copy a Class from one :class:`geosoft.gxapi.GXMETA` to another

        **Note:**

        This will copy all parent classes as well.
        """
        ret_val = self._wrapper.h_copy_across_class(p2._wrapper, p3)
        return ret_val




    def h_copy_across_data(self, p2, p3):
        """
        Copy a Data value from one :class:`geosoft.gxapi.GXMETA` to another
        """
        ret_val = self._wrapper.h_copy_across_data(p2._wrapper, p3)
        return ret_val




    def h_copy_across_item(self, p2, p3):
        """
        Copy an Item from one :class:`geosoft.gxapi.GXMETA` to another
        """
        ret_val = self._wrapper.h_copy_across_item(p2._wrapper, p3)
        return ret_val




    def h_copy_across_type(self, p2, p3):
        """
        Copy a Type from one :class:`geosoft.gxapi.GXMETA` to another

        **Note:**

        Classes and parent types will also be copied.
        """
        ret_val = self._wrapper.h_copy_across_type(p2._wrapper, p3)
        return ret_val




    def move_datas_across(self, p2, p3, p4):
        """
        Moves data items from one :class:`geosoft.gxapi.GXMETA` to another
        """
        self._wrapper.move_datas_across(p2._wrapper, p3, p4)
        




# Type



    def create_type(self, p2, p3, p4):
        """
        Create an attribute
        """
        ret_val = self._wrapper.create_type(p2.encode(), p3, p4)
        return ret_val




    def delete_data(self, p2):
        """
        Delete Data from :class:`geosoft.gxapi.GXMETA`.
        """
        self._wrapper.delete_data(p2)
        




    def delete_type(self, p2):
        """
        Delete Type from :class:`geosoft.gxapi.GXMETA`.
        """
        self._wrapper.delete_type(p2)
        




# UMN



    def get_obj_name(self, p2, p3):
        """
        Get the name of this item.
        """
        p3.value = self._wrapper.get_obj_name(p2, p3.value.encode())
        




    def resolve_umn(self, p2):
        """
        Resolve a Unique Meta Name (UMN) and find the token
        """
        ret_val = self._wrapper.resolve_umn(p2.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer