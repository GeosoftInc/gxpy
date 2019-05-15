### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMETA(gxapi_cy.WrapMETA):
    """
    GXMETA class.

    A `GXMETA <geosoft.gxapi.GXMETA>` object contains hierarchical organized metadata
    of any type, including other objects.  `GXMETA <geosoft.gxapi.GXMETA>` information
    is organized in an XML-like structure based on a data
    schema that describes the data hierarchy.   `GXMETA <geosoft.gxapi.GXMETA>` objects
    are used by many entities that need to store metadata
    specific to the entities or to the application.

    Metadata can be saved in databases and maps, as well as in
    channels, lines, views and groups.  Oasis montaj objects
    can be queried for their associated metadata, and if it
    exists, the metadata can be retrieved and utilized by
    other Oasis montaj processes.
    """

    def __init__(self, handle=0):
        super(GXMETA, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMETA <geosoft.gxapi.GXMETA>`
        
        :returns: A null `GXMETA <geosoft.gxapi.GXMETA>`
        :rtype:   GXMETA
        """
        return GXMETA()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Attribute



    def create_attrib(self, name, ph_class, ph_type):
        """
        Create an attribute
        
        :param name:      Attribute Name
        :param ph_class:  Parent class or :ref:`META_CORE_CLASS`
        :param ph_type:   Type of Attribute or :ref:`META_CORE_TYPE`
        :type  name:      str
        :type  ph_class:  int
        :type  ph_type:   int

        :returns:         x - Attribute Token
        :rtype:           int

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create_attrib(name.encode(), ph_class, ph_type)
        return ret_val




    def delete_attrib(self, ph_attribute):
        """
        Delete Attrib from `GXMETA <geosoft.gxapi.GXMETA>`.
        
        :param ph_attribute:  Attrib to delete
        :type  ph_attribute:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_attrib(ph_attribute)
        




# Browser



    def set_attribute_editable(self, ph_attribute, editable):
        """
        Allow/disallow an attribute to be editable in the browser
        
        :param ph_attribute:  Attribute or :ref:`META_CORE_ATTRIB`
        :param editable:      Editable Flag
        :type  ph_attribute:  int
        :type  editable:      int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attribute_editable(ph_attribute, editable)
        




    def set_attribute_visible(self, ph_attribute, visible):
        """
        Allow/disallow an attribute to be visible in the browser
        
        :param ph_attribute:  Attribute or :ref:`META_CORE_ATTRIB`
        :param visible:       Editable Flag
        :type  ph_attribute:  int
        :type  visible:       int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attribute_visible(ph_attribute, visible)
        




# Class



    def create_class(self, name, ph_class):
        """
        Create a class
        
        :param name:      Class Name
        :param ph_class:  Parent class or `META_CORE_CLASS_Base <geosoft.gxapi.META_CORE_CLASS_Base>`
        :type  name:      str
        :type  ph_class:  int

        :returns:         x - Class Token
        :rtype:           int

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create_class(name.encode(), ph_class)
        return ret_val




    def delete_class(self, ph_class):
        """
        Delete Class from `GXMETA <geosoft.gxapi.GXMETA>`.
        
        :param ph_class:  Class to delete
        :type  ph_class:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_class(ph_class)
        




# Core



    def copy(self, source_meta):
        """
        Copy a `GXMETA <geosoft.gxapi.GXMETA>` to another
        
        :param source_meta:  Source `GXMETA <geosoft.gxapi.GXMETA>` object.
        :type  source_meta:  GXMETA

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(source_meta)
        



    @classmethod
    def create(cls):
        """
        Create
        

        :returns:    `GXMETA <geosoft.gxapi.GXMETA>` Object
        :rtype:      GXMETA

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMETA._create(GXContext._get_tls_geo())
        return GXMETA(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create a `GXMETA <geosoft.gxapi.GXMETA>` Object from a `GXBF <geosoft.gxapi.GXBF>`
        
        :param bf:  `GXBF <geosoft.gxapi.GXBF>` to serialize from
        :type  bf:  GXBF

        :returns:    `GXMETA <geosoft.gxapi.GXMETA>` Object
        :rtype:      GXMETA

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMETA._create_s(GXContext._get_tls_geo(), bf)
        return GXMETA(ret_val)






    def serial(self, bf):
        """
        Serialize an `GXMETA <geosoft.gxapi.GXMETA>` to a `GXBF <geosoft.gxapi.GXBF>`
        
        :param bf:    `GXBF <geosoft.gxapi.GXBF>` to serialize to
        :type  bf:    GXBF

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(bf)
        




# Get Data



    def find_data(self, ph_object, ph_attrib):
        """
        Does this meta/attribute have a value ?
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :type  ph_object:  int
        :type  ph_attrib:  int

        :returns:          x  - Data Value
                           `H_META_INVALID_TOKEN <geosoft.gxapi.H_META_INVALID_TOKEN>` - No
        :rtype:            int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_data(ph_object, ph_attrib)
        return ret_val




    def get_attrib_bool(self, ph_object, ph_attrib, value):
        """
        Get a boolean value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      int_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        value.value = self._get_attrib_bool(ph_object, ph_attrib, value.value)
        




    def get_attrib_enum(self, ph_object, ph_attrib, value):
        """
        Get an enum value to an attribute (as an integer)
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      int_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        value.value = self._get_attrib_enum(ph_object, ph_attrib, value.value)
        




    def get_attrib_int(self, ph_object, ph_attrib, value):
        """
        Get an integer value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      int_ref

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        value.value = self._get_attrib_int(ph_object, ph_attrib, value.value)
        




    def get_attrib_double(self, ph_object, ph_attrib, value):
        """
        Get an integer value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      float_ref

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        value.value = self._get_attrib_double(ph_object, ph_attrib, value.value)
        




    def get_attrib_string(self, ph_object, ph_attrib, value):
        """
        Get a string value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      String value to get
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      str_ref

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        value.value = self._get_attrib_string(ph_object, ph_attrib, value.value.encode())
        




    def has_value(self, ph_object, ph_attrib):
        """
        Does this meta/attribute have a value set?
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :type  ph_object:  int
        :type  ph_attrib:  int
        :rtype:            bool

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._has_value(ph_object, ph_attrib)
        return ret_val




# Import/Export



    def export_table_csv(self, ph_class, file):
        """
        Export all items in a class as a CSV
        
        :param ph_class:  Class of items to export
        :param file:      Name of CSV file to produce
        :type  ph_class:  int
        :type  file:      str

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_table_csv(ph_class, file.encode())
        




    def import_table_csv(self, ph_class, file):
        """
        Import a CSV into a class as items.
        
        :param ph_class:  Class to import into
        :param file:      Name of CSV file to load
        :type  ph_class:  int
        :type  file:      str

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Field names in the CSV file that match attribute names in the class will be
        imported into table entries in the class.  Usually this will be used with
        a class created using the hCreateTable_SCHEMA method so that the contents of
        class can be viewed as a table.
        """
        self._import_table_csv(ph_class, file.encode())
        




    def write_text(self, wa):
        """
        Write the entire meta as a text file
        
        :param wa:    `GXWA <geosoft.gxapi.GXWA>` to write to
        :type  wa:    GXWA

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_text(wa)
        




# Item



    def delete_all_items(self, ph_class):
        """
        Delete all items in this class.
        
        :param ph_class:  Class of items to delete
        :type  ph_class:  int

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_all_items(ph_class)
        




    def delete_item(self, ph_item):
        """
        Delete item from `GXMETA <geosoft.gxapi.GXMETA>`.
        
        :param ph_item:  Item to delete
        :type  ph_item:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_item(ph_item)
        




    def h_creat_item(self, name, ph_class):
        """
        Creates item in Class.
        
        :param name:      Unique item Name
        :param ph_class:  Class (can be root)
        :type  name:      str
        :type  ph_class:  int

        :returns:         x                    - Next Item
                          `H_META_INVALID_TOKEN <geosoft.gxapi.H_META_INVALID_TOKEN>` - Error
        :rtype:           int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._h_creat_item(name.encode(), ph_class)
        return ret_val




    def h_get_next_item(self, ph_class, ph_token):
        """
        Count the number of items in a class
        
        :param ph_class:  Class
        :param ph_token:  Starting Item (must `H_META_INVALID_TOKEN <geosoft.gxapi.H_META_INVALID_TOKEN>` for first item)
        :type  ph_class:  int
        :type  ph_token:  int

        :returns:         x                    - Next Item
                          `H_META_INVALID_TOKEN <geosoft.gxapi.H_META_INVALID_TOKEN>` - No more items
        :rtype:           int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._h_get_next_item(ph_class, ph_token)
        return ret_val




# Object



    def get_attrib_obj(self, ph_object, ph_attrib, obj):
        """
        Get an object from an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param obj:        Object to get info into
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  obj:        int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_attrib_obj(ph_object, ph_attrib, obj)
        




    def set_attrib_obj(self, ph_object, ph_attrib, obj):
        """
        Set an object to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param obj:        Object to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  obj:        int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attrib_obj(ph_object, ph_attrib, obj)
        




# Set Data



    def set_attrib_bool(self, ph_object, ph_attrib, value):
        """
        Set a boolean value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attrib_bool(ph_object, ph_attrib, value)
        




    def set_attrib_enum(self, ph_object, ph_attrib, value):
        """
        Set an enum value to an attribute (as an integer)
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attrib_enum(ph_object, ph_attrib, value)
        




    def set_attrib_int(self, ph_object, ph_attrib, value):
        """
        Set an integer value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attrib_int(ph_object, ph_attrib, value)
        




    def set_attrib_double(self, ph_object, ph_attrib, value):
        """
        Set an integer value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      Value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      float

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attrib_double(ph_object, ph_attrib, value)
        




    def set_attrib_string(self, ph_object, ph_attrib, value):
        """
        Set a string value to an attribute
        
        :param ph_object:  Object
        :param ph_attrib:  Attribute
        :param value:      String value to set
        :type  ph_object:  int
        :type  ph_attrib:  int
        :type  value:      str

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attrib_string(ph_object, ph_attrib, value.encode())
        




    def set_empty_attrib(self, ph_object, ph_attrib):
        """
        Set an empty attribute data holder
        
        :param ph_object:  MetaObject to set
        :param ph_attrib:  Attribute MetaObject to set
        :type  ph_object:  int
        :type  ph_attrib:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_empty_attrib(ph_object, ph_attrib)
        




# Transfer



    def h_copy_across_attribute(self, source_meta, ph_attribute):
        """
        Copy an Attribute from one `GXMETA <geosoft.gxapi.GXMETA>` to another
        
        :param source_meta:   Source `GXMETA <geosoft.gxapi.GXMETA>` object.
        :param ph_attribute:  Attribute to copy
        :type  source_meta:   GXMETA
        :type  ph_attribute:  int

        :returns:             x                  - Handle of Attribute
                              META_INVALID_TOKEN - No visible data
        :rtype:               int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._h_copy_across_attribute(source_meta, ph_attribute)
        return ret_val




    def h_copy_across_class(self, source_meta, ph_class):
        """
        Copy a Class from one `GXMETA <geosoft.gxapi.GXMETA>` to another
        
        :param source_meta:  Source `GXMETA <geosoft.gxapi.GXMETA>` object.
        :param ph_class:     Class to copy
        :type  source_meta:  GXMETA
        :type  ph_class:     int

        :returns:            x                  - Handle of Class
                             META_INVALID_TOKEN - No visible data anywhere
        :rtype:              int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This will copy all parent classes as well.
        """
        ret_val = self._h_copy_across_class(source_meta, ph_class)
        return ret_val




    def h_copy_across_data(self, source_meta, ph_data):
        """
        Copy a Data value from one `GXMETA <geosoft.gxapi.GXMETA>` to another
        
        :param source_meta:  Source `GXMETA <geosoft.gxapi.GXMETA>` object.
        :param ph_data:      Data value to copy
        :type  source_meta:  GXMETA
        :type  ph_data:      int

        :returns:            x                  - Handle of Data value
                             META_INVALID_TOKEN - No visible data
        :rtype:              int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._h_copy_across_data(source_meta, ph_data)
        return ret_val




    def h_copy_across_item(self, source_meta, ph_item):
        """
        Copy an Item from one `GXMETA <geosoft.gxapi.GXMETA>` to another
        
        :param source_meta:  Source `GXMETA <geosoft.gxapi.GXMETA>` object.
        :param ph_item:      Item to copy
        :type  source_meta:  GXMETA
        :type  ph_item:      int

        :returns:            x                  - Handle of Item
                             META_INVALID_TOKEN - No visible data
        :rtype:              int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._h_copy_across_item(source_meta, ph_item)
        return ret_val




    def h_copy_across_type(self, source_meta, ph_type):
        """
        Copy a Type from one `GXMETA <geosoft.gxapi.GXMETA>` to another
        
        :param source_meta:  Source `GXMETA <geosoft.gxapi.GXMETA>` object.
        :param ph_type:      Type to copy
        :type  source_meta:  GXMETA
        :type  ph_type:      int

        :returns:            x                  - Handle of type
                             META_INVALID_TOKEN - No visible data anywhere
        :rtype:              int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Classes and parent types will also be copied.
        """
        ret_val = self._h_copy_across_type(source_meta, ph_type)
        return ret_val




    def move_datas_across(self, source_meta, ph_i_obj, ph_o_obj):
        """
        Moves data items from one `GXMETA <geosoft.gxapi.GXMETA>` to another
        
        :param source_meta:  Source `GXMETA <geosoft.gxapi.GXMETA>` Object
        :param ph_i_obj:     Object to copy data from
        :param ph_o_obj:     Object to copy data to
        :type  source_meta:  GXMETA
        :type  ph_i_obj:     int
        :type  ph_o_obj:     int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._move_datas_across(source_meta, ph_i_obj, ph_o_obj)
        




# Type



    def create_type(self, name, ph_class, ph_type):
        """
        Create an attribute
        
        :param name:      Attribute Name
        :param ph_class:  Parent Class or :ref:`META_CORE_CLASS`
        :param ph_type:   Parent Type or :ref:`META_CORE_TYPE`
        :type  name:      str
        :type  ph_class:  int
        :type  ph_type:   int

        :returns:         x - Type Token
        :rtype:           int

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create_type(name.encode(), ph_class, ph_type)
        return ret_val




    def delete_data(self, ph_data):
        """
        Delete Data from `GXMETA <geosoft.gxapi.GXMETA>`.
        
        :param ph_data:  Data to delete
        :type  ph_data:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_data(ph_data)
        




    def delete_type(self, ph_type):
        """
        Delete Type from `GXMETA <geosoft.gxapi.GXMETA>`.
        
        :param ph_type:  Type to delete
        :type  ph_type:  int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_type(ph_type)
        




# UMN



    def get_obj_name(self, ph_object, name):
        """
        Get the name of this item.
        
        :param ph_object:  Object
        :param name:       Name of object
        :type  ph_object:  int
        :type  name:       str_ref

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = self._get_obj_name(ph_object, name.value.encode())
        




    def resolve_umn(self, umn):
        """
        Resolve a Unique Meta Name (UMN) and find the token
        
        :param umn:   Unique Meta Name (UMN)
        :type  umn:   str

        :returns:     x                    - Token
                      `H_META_INVALID_TOKEN <geosoft.gxapi.H_META_INVALID_TOKEN>` - Not found
        :rtype:       int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._resolve_umn(umn.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer