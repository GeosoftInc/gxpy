### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXPG import GXPG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIMG:
    """
    GXIMG class.

    The `GXIMG` class performs read and write operations on grid
    file data. When efficient access along both rows and columns
    is desired the `GXPG` class is recommended (see `GXPG` and `GXPGU`);
    the `GXIMG` is first created, then the `GXPG` is obtained from
    the `GXIMG` using `get_pg`.

    **Note:**

    The `GXIMG` methods use the XGD DATs to access grid files in different
    formats.  The characteristics of a grid can be controlled using
    decorations on a grid file name.  For example:
    
    `create_new_file`(`GS_DOUBLE`,1,100,100,"mag.grd");
    -> creates a new grid file "mag.grd" with all defaults.
    
    `create_new_file`(`GS_DOUBLE`,1,100,100,"mag.grd(GRD;comp=none)");
    -> creates a new grid file "mag.grd" with no compression.
    
    `create_new_file`(`GS_DOUBLE`,1,100,100,"mag.grd(GRD;comp=size;type=short");
    -> creates a new grid file "mag.grd" compressed for size, numbers
    stored as 2-byte integers..
    
    See `DAT_XGD`.DOC for information about file name decorations available
    for all `GXDAT` types.
    
    Different grid types support different features.  For example, not all
    grid types support projection information.  Geosoft will always create
    a ``*.gi`` file that is used to store all such information that we require
    from a grid.  If the grid does support this information, both the grid
    and the ``*.gi`` file will contain the information.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIMG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIMG`
        
        :returns: A null `GXIMG`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXIMG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXIMG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def average2(cls, grid_in, grid_out):
        """
        Reduce the dimensions in a 2D pager by a factor of 2

        **Note:**

        This method is useful for reducing the dimensions in a 2D pager by a factor of 2.
        The output pager retains the same origin, but the X and Y spacing is double that of the original. Essentially,
        the process removes all the even-indexed rows and columns, while leaving the locations of all the remaining
        data points in the "odd" rows and columns unchanged.
        
        The output values at the output data locations are created by performing an average of the original data point and
        its valid surrounding data points; what is essentially a 3x3 smoothing filter.
        """
        gxapi_cy.WrapIMG.average2(GXContext._get_tls_geo(), grid_in.encode(), grid_out.encode())
        




    def copy(self, im_go):
        """
        Copy IMGs.
        """
        self._wrapper.copy(im_go._wrapper)
        



    @classmethod
    def create(cls, type, p2, p3, p4):
        """
        Creates an `GXIMG` not tied to a file at all

        **Note:**

        Once destroyed all the data in this `GXIMG` is lost.
        """
        ret_val = gxapi_cy.WrapIMG.create(GXContext._get_tls_geo(), type, p2, p3, p4)
        return GXIMG(ret_val)



    @classmethod
    def create_file(cls, type, p2, p3):
        """
        Creates an Image object tied to a grid file.

        **Note:**

        When the `GS_DOUBLE` data type is chosen the actual on-disk
        type of the input image will be used instead of `GS_DOUBLE`
        if the on-disk values represent color data as opposed
        to real numbers.
        """
        ret_val = gxapi_cy.WrapIMG.create_file(GXContext._get_tls_geo(), type, p2.encode(), p3)
        return GXIMG(ret_val)



    @classmethod
    def create_mem(cls, type, p2, p3, p4):
        """
        Creates an `GXIMG` object that is backed only by memory.

        **Note:**

        Once destroyed all the data is lost. This is temporary.
        """
        ret_val = gxapi_cy.WrapIMG.create_mem(GXContext._get_tls_geo(), type, p2, p3, p4)
        return GXIMG(ret_val)



    @classmethod
    def create_new_file(cls, type, p2, p3, p4, p5):
        """
        Creates an output image file using User defined info.

        **Note:**

        Special Note for developers who use this function and
        related functions to output ERMapper image (ERS, ECW) files:
        
        This function internally called ERMapper plugin to create ERS header
        files. To find the location of ERMapper plugin library, a registry setting
        needs to set. The key in the registry is HKEY_LOCAL_MACHINE\\SOFTWARE\\"MyProgram(libversion7.0)"
        and in that key register a string BASE_PATH = D:\\Oasismontaj\\plugins\\er_mapper.
        MyProgram is the name of your application and D:\\Oasismontaj\\plugins\\er_mapper
        is the location of ERMapper library.
        
        It is recommended that this registry key is set during the installation
        of your application.
        """
        ret_val = gxapi_cy.WrapIMG.create_new_file(GXContext._get_tls_geo(), type, p2, p3, p4, p5.encode())
        return GXIMG(ret_val)



    @classmethod
    def create_out_file(cls, type, p2, p3):
        """
        Creates an output image file using input image info.

        **Note:**

        When the `GS_DOUBLE` data type is chosen the actual on-disk
        type of the input image will be used instead of `GS_DOUBLE`
        if the on-disk values represent color data as opposed
        to real numbers.
        """
        ret_val = gxapi_cy.WrapIMG.create_out_file(GXContext._get_tls_geo(), type, p2.encode(), p3._wrapper)
        return GXIMG(ret_val)




    def create_projected(self, ipj):
        """
        Applies a projection to an image.

        **Note:**

        The `GXIMG` now appears to be in the projected coordinate
        system space.
        """
        self._wrapper.create_projected(ipj._wrapper)
        




    def create_projected2(self, ipj, cell_size):
        """
        Applies a projection to an image, specify cell size.

        **Note:**

        The `GXIMG` now appears to be in the projected coordinate
        system space, with the specified cell size. If the cell
        size is `rDUMMY` (`GS_R8DM`), one is automatically calculated,
        as with `create_projected`.
        """
        self._wrapper.create_projected2(ipj._wrapper, cell_size)
        




    def create_projected3(self, ipj, cell_size, exp_pct):
        """
        Same as `create_projected2`, but set expansion of bounds.

        **Note:**

        The `GXIMG` now appears to be in the projected coordinate
        system space, with the specified cell size. If the cell
        size is `rDUMMY` (`GS_R8DM`), one is automatically calculated,
        as with `create_projected`.
        The expansion percent expands the bounds of the projected grid
        in order to allow for the curving of bounding edges. Normally,
        edges are sampled in order to allow for curving, but this
        parameter is set to 1.0 (for 1 percent) in the `create_projected`
        and `create_projected2` wrappers, and will generally create a
        white/dummy border around the new grid. This new method allows
        you to specify the expansion, or turn it off (by setting it to 0).
        If the value is set to `rDUMMY`, then expansion is left at 1.0,
        the legacy behaviour.
        """
        self._wrapper.create_projected3(ipj._wrapper, cell_size, exp_pct)
        






    def geth_pg(self):
        """
        Get the actual pager of a grid.

        .. seealso::

            `get_pg` to get just a copy of the grid's pager.
        """
        ret_val = self._wrapper.geth_pg()
        return GXPG(ret_val)




    def get_info(self, dx, dy, xo, yo, rot):
        """
        Retrieves location information about this image.
        """
        dx.value, dy.value, xo.value, yo.value, rot.value = self._wrapper.get_info(dx.value, dy.value, xo.value, yo.value, rot.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection of a grid.
        """
        self._wrapper.get_ipj(ipj._wrapper)
        




    def get_meta(self, meta):
        """
        Get the metadata of a grid.
        """
        self._wrapper.get_meta(meta._wrapper)
        




    def get_pg(self, pg):
        """
        Get a copy of the pager of a grid.

        .. seealso::

            `geth_pg` to get the actual pager of the grid.
        """
        self._wrapper.get_pg(pg._wrapper)
        




    def get_projected_cell_size(self, ipj, cell):
        """
        Returns default cell size from projected image.

        **Note:**

        Returns the cell size calculated by CreateProjected_PJIMG, or by
        `create_projected2` when
        `GS_R8DM` is entered as the optional cell size. No inheritance
        is actually performed to the input `GXIMG`.
        """
        cell.value = self._wrapper.get_projected_cell_size(ipj._wrapper, cell.value)
        




    def get_tr(self, tr):
        """
        Get the trend information from a grid.
        """
        self._wrapper.get_tr(tr._wrapper)
        




    def element_type(self, xg_dor_img):
        """
        Returns the element type.
        """
        ret_val = self._wrapper.element_type(xg_dor_img)
        return ret_val




    def e_type(self):
        """
        Returns the element type.

        **Note:**

        Same as sElementType_IMG(img,1)
        """
        ret_val = self._wrapper.e_type()
        return ret_val




    def get_def_itr(self, itr):
        """
        Get default transform, if it exists
        """
        ret_val = self._wrapper.get_def_itr(itr._wrapper)
        return ret_val




    def is_colour(self):
        """
        Is this a Geosoft color grid?
        """
        ret_val = self._wrapper.is_colour()
        return ret_val



    @classmethod
    def is_valid_img_file(cls, file):
        """
        Is this a valid `GXIMG` file?
        """
        ret_val = gxapi_cy.WrapIMG.is_valid_img_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def is_valid_img_file_ex(cls, file, err_msg):
        """
        Is this a valid `GXIMG` file? Returns error message if it cannot be opened for any reason.
        """
        ret_val, err_msg.value = gxapi_cy.WrapIMG.is_valid_img_file_ex(GXContext._get_tls_geo(), file.encode(), err_msg.value.encode())
        return ret_val




    def ne(self):
        """
        Gets the # of elements in the optimal KX direction.
        """
        ret_val = self._wrapper.ne()
        return ret_val




    def inherit(self, ipj, cell):
        """
        Inherit a projection/new cell size on the `GXIMG`.

        **Note:**

        If cell size is `GS_R8DM`, then "nice" values for the cell
        size of the new projected grid will be determined so that
        the new grid has about the same number of cells as the old.
        If the cell size is specified, the inheritance will always
        work, even if the input `GXIPJ` is identical to the original
        `GXIPJ`, and the cell boundaries will be forced to be aligned
        with the new cell size.
        """
        self._wrapper.inherit(ipj._wrapper, cell)
        




    def inherit_img(self, im_gs):
        """
        Make a grids match in size and coordinate system
        """
        self._wrapper.inherit_img(im_gs._wrapper)
        




    def nv(self):
        """
        Gets the # of vectors in the optimal KX direction.
        """
        ret_val = self._wrapper.nv()
        return ret_val




    def nx(self):
        """
        Gets the # of X elements.
        """
        ret_val = self._wrapper.nx()
        return ret_val




    def ny(self):
        """
        Gets the # of Y elements.
        """
        ret_val = self._wrapper.ny()
        return ret_val




    def query_int(self, query):
        """
        Query information about the `GXIMG`

        **Note:**

        You can call either funtion to retrieve any data,
        int or real.
        """
        ret_val = self._wrapper.query_int(query)
        return ret_val




    def query_kx(self):
        """
        Asks the `GXIMG` for the most efficient way to access the data.
        """
        ret_val = self._wrapper.query_kx()
        return ret_val




    def set_def_itr(self, itr):
        """
        Set default transform
        """
        ret_val = self._wrapper.set_def_itr(itr._wrapper)
        return ret_val



    @classmethod
    def user_preference_to_plot_as_colour_shaded_grid(cls):
        """
        Returns the global setting.
        """
        ret_val = gxapi_cy.WrapIMG.user_preference_to_plot_as_colour_shaded_grid(GXContext._get_tls_geo())
        return ret_val




    def load_img(self, im_gi):
        """
        Loads an `GXIMG` into a master `GXIMG`.

        **Note:**

        The cell sizes and projections must be the same.
        """
        self._wrapper.load_img(im_gi._wrapper)
        




    def load_into_pager(self):
        """
        Load `GXIMG` data from file into a pager to increase
        access time.
        """
        self._wrapper.load_into_pager()
        




    def opt_kx(self, kx):
        """
        Force optimal KX as desired.

        **Note:**

        This will force loading an image into a `GXPG` if it is not already
        accessible in the direction requested.
        
        Subsequent calls to methods that use the optimal KX will use the
        KX set here.
        """
        self._wrapper.opt_kx(kx)
        




    def read_v(self, v, be, p4, p5):
        """
        Read a vector in the optimal KX direction.
        """
        self._wrapper.read_v(v, be, p4, p5._wrapper)
        




    def read_x(self, bx, p3, p4, p5):
        """
        Read a column (constant X)
        """
        self._wrapper.read_x(bx, p3, p4, p5._wrapper)
        




    def read_y(self, by, p3, p4, p5):
        """
        Read a row (constant Y)
        """
        self._wrapper.read_y(by, p3, p4, p5._wrapper)
        



    @classmethod
    def refresh_gi(cls, grid):
        """
        Refresh the GI of a grid after it has moved or changed.
        """
        gxapi_cy.WrapIMG.refresh_gi(GXContext._get_tls_geo(), grid.encode())
        




    def relocate(self, min_x, min_y, max_x, max_y, asp):
        """
        Re-locate a grid image.
        """
        self._wrapper.relocate(min_x, min_y, max_x, max_y, asp)
        



    @classmethod
    def report(cls, grid, wa, force, decimals, title):
        """
        Writes grid info report to a file
        """
        gxapi_cy.WrapIMG.report(GXContext._get_tls_geo(), grid.encode(), wa._wrapper, force, decimals, title.encode())
        



    @classmethod
    def report_csv(cls, grid, wa, force, decimals, header):
        """
        Writes grid info as a line to a CSV file

        **Note:**

        Appends the stats as a CSV line to the input text file.
        The header line should only be written to a new text file.
        """
        gxapi_cy.WrapIMG.report_csv(GXContext._get_tls_geo(), grid.encode(), wa._wrapper, force, decimals, header)
        




    def get_z(self, x, y):
        """
        Gets the grid value at a point
        """
        ret_val = self._wrapper.get_z(x, y)
        return ret_val




    def query_double(self, query):
        """
        Query information about the `GXIMG`

        **Note:**

        You can call either funtion to retrieve any data,
        int or real.
        """
        ret_val = self._wrapper.query_double(query)
        return ret_val




    def set_grid_unchanged(self):
        """
        Mark the grid as unchanged so it will not output lineage
        """
        self._wrapper.set_grid_unchanged()
        




    def set_info(self, dx, dy, xo, yo, rot):
        """
        Sets location information about this image.

        **Note:**

        Calls to this function should be made BEFORE calls to `set_ipj`,
        as the latter function sets up the bounding rectangle in the metadata.
        """
        self._wrapper.set_info(dx, dy, xo, yo, rot)
        




    def set_ipj(self, ipj):
        """
        Set the projection of a grid.

        **Note:**

        Calls to this function should be made AFTER calls to `set_info`,
        as `set_ipj` sets up the bounding rectangle in the metadata.
        """
        self._wrapper.set_ipj(ipj._wrapper)
        




    def set_meta(self, meta):
        """
        Set the metadata of a grid.
        """
        self._wrapper.set_meta(meta._wrapper)
        




    def set_pg(self, pg):
        """
        Copy a pager into the pager of a grid.
        """
        self._wrapper.set_pg(pg._wrapper)
        




    def set_tr(self, tr):
        """
        Set the trend information to a grid.
        """
        self._wrapper.set_tr(tr._wrapper)
        



    @classmethod
    def sync(cls, grid):
        """
        Syncronize the Metadata for this Grid
        """
        gxapi_cy.WrapIMG.sync(GXContext._get_tls_geo(), grid.encode())
        




    def write_v(self, v, be, p4, p5):
        """
        Write a vector in the optimal KX direction.
        """
        self._wrapper.write_v(v, be, p4, p5._wrapper)
        




    def write_x(self, bx, p3, p4, p5):
        """
        Write a column (constant X)
        """
        self._wrapper.write_x(bx, p3, p4, p5._wrapper)
        




    def write_y(self, by, p3, p4, p5):
        """
        Write a row (constant Y)
        """
        self._wrapper.write_y(by, p3, p4, p5._wrapper)
        




    def set_double_parameter(self, name, value):
        """
        Store a real parameter in an `GXIMG` object
        """
        self._wrapper.set_double_parameter(name.encode(), value)
        




    def get_double_parameter(self, name):
        """
        Store a real parameter in an `GXIMG` object
        """
        ret_val = self._wrapper.get_double_parameter(name.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer