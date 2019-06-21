### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXPG import GXPG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIMG(gxapi_cy.WrapIMG):
    """
    GXIMG class.

    The `GXIMG <geosoft.gxapi.GXIMG>` class performs read and write operations on grid
    file data. When efficient access along both rows and columns
    is desired the `GXPG <geosoft.gxapi.GXPG>` class is recommended (see `GXPG <geosoft.gxapi.GXPG>` and `GXPGU <geosoft.gxapi.GXPGU>`);
    the `GXIMG <geosoft.gxapi.GXIMG>` is first created, then the `GXPG <geosoft.gxapi.GXPG>` is obtained from
    the `GXIMG <geosoft.gxapi.GXIMG>` using `get_pg <geosoft.gxapi.GXIMG.get_pg>`.

    **Note:**

    The `GXIMG <geosoft.gxapi.GXIMG>` methods use the XGD DATs to access grid files in different
    formats.  The characteristics of a grid can be controlled using
    decorations on a grid file name.  For example:

    `create_new_file <geosoft.gxapi.GXIMG.create_new_file>`(`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`,1,100,100,"mag.grd");
    -> creates a new grid file "mag.grd" with all defaults.

    `create_new_file <geosoft.gxapi.GXIMG.create_new_file>`(`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`,1,100,100,"mag.grd(GRD;comp=none)");
    -> creates a new grid file "mag.grd" with no compression.

    `create_new_file <geosoft.gxapi.GXIMG.create_new_file>`(`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`,1,100,100,"mag.grd(GRD;comp=size;type=short");
    -> creates a new grid file "mag.grd" compressed for size, numbers
    stored as 2-byte integers..

    See :ref:`DAT_XGD`.DOC for information about file name decorations available
    for all `GXDAT <geosoft.gxapi.GXDAT>` types.

    Different grid types support different features.  For example, not all
    grid types support projection information.  Geosoft will always create
    a ``*.gi`` file that is used to store all such information that we require
    from a grid.  If the grid does support this information, both the grid
    and the ``*.gi`` file will contain the information.
    """

    def __init__(self, handle=0):
        super(GXIMG, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIMG <geosoft.gxapi.GXIMG>`
        
        :returns: A null `GXIMG <geosoft.gxapi.GXIMG>`
        :rtype:   GXIMG
        """
        return GXIMG()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def average2(cls, grid_in, grid_out):
        """
        Reduce the dimensions in a 2D pager by a factor of 2
        
        :param grid_in:   Name of source Grid
        :param grid_out:  Name of output Grid
        :type  grid_in:   str
        :type  grid_out:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method is useful for reducing the dimensions in a 2D pager by a factor of 2.
        The output pager retains the same origin, but the X and Y spacing is double that of the original. Essentially,
        the process removes all the even-indexed rows and columns, while leaving the locations of all the remaining
        data points in the "odd" rows and columns unchanged.

        The output values at the output data locations are created by performing an average of the original data point and
        its valid surrounding data points; what is essentially a 3x3 smoothing filter.
        """
        gxapi_cy.WrapIMG._average2(GXContext._get_tls_geo(), grid_in.encode(), grid_out.encode())
        




    def copy(self, im_go):
        """
        Copy IMGs.
        
        :param im_go:  Target `GXIMG <geosoft.gxapi.GXIMG>`
        :type  im_go:  GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(im_go)
        



    @classmethod
    def create(cls, type, kx, width, height):
        """
        Creates an `GXIMG <geosoft.gxapi.GXIMG>` not tied to a file at all
        
        :param type:    Data type :ref:`GS_TYPES`
        :param kx:      Grid orientation (KX): 1 (rows in X) -1 (rows in Y)
        :param width:   Grid width
        :param height:  Grid height
        :type  type:    int
        :type  kx:      int
        :type  width:   int
        :type  height:  int

        :returns:       `GXIMG <geosoft.gxapi.GXIMG>` object
        :rtype:         GXIMG

        .. versionadded:: 5.0.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Once destroyed all the data in this `GXIMG <geosoft.gxapi.GXIMG>` is lost.
        """
        ret_val = gxapi_cy.WrapIMG._create(GXContext._get_tls_geo(), type, kx, width, height)
        return GXIMG(ret_val)



    @classmethod
    def create_file(cls, type, grid, mode):
        """
        Creates an Image object tied to a grid file.
        
        :param type:  Data type, :ref:`GS_TYPES` or `GS_TYPE_DEFAULT <geosoft.gxapi.GS_TYPE_DEFAULT>` to use native `GXDAT <geosoft.gxapi.GXDAT>` type.
        :param grid:  Name of the Grid to link to
        :param mode:  Grid file open mode :ref:`IMG_FILE`
        :type  type:  int
        :type  grid:  str
        :type  mode:  int

        :returns:     `GXIMG <geosoft.gxapi.GXIMG>` object
        :rtype:       GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** When the `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` data type is chosen the actual on-disk
        type of the input image will be used instead of `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        if the on-disk values represent color data as opposed
        to real numbers.
        """
        ret_val = gxapi_cy.WrapIMG._create_file(GXContext._get_tls_geo(), type, grid.encode(), mode)
        return GXIMG(ret_val)



    @classmethod
    def create_mem(cls, type, kx, width, height):
        """
        Creates an `GXIMG <geosoft.gxapi.GXIMG>` object that is backed only by memory.
        
        :param type:    Data type, :ref:`GS_TYPES`
        :param kx:      Grid orientation (KX): 1 (rows in X) -1 (rows in Y)
        :param width:   Grid width
        :param height:  Grid height
        :type  type:    int
        :type  kx:      int
        :type  width:   int
        :type  height:  int

        :returns:       `GXIMG <geosoft.gxapi.GXIMG>` object
        :rtype:         GXIMG

        .. versionadded:: 5.0.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Once destroyed all the data is lost. This is temporary.
        """
        ret_val = gxapi_cy.WrapIMG._create_mem(GXContext._get_tls_geo(), type, kx, width, height)
        return GXIMG(ret_val)



    @classmethod
    def create_new_file(cls, type, kx, width, height, grid):
        """
        Creates a new image file
        
        :param type:    Data type, :ref:`GS_TYPES` Cannot be `GS_TYPE_DEFAULT <geosoft.gxapi.GS_TYPE_DEFAULT>`
        :param kx:      Grid orientation (KX): 1 (rows in X) -1 (rows in Y)
        :param width:   Grid width
        :param height:  Grid height
        :param grid:    Name of the Grid to link to
        :type  type:    int
        :type  kx:      int
        :type  width:   int
        :type  height:  int
        :type  grid:    str

        :returns:       `GXIMG <geosoft.gxapi.GXIMG>` object
        :rtype:         GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIMG._create_new_file(GXContext._get_tls_geo(), type, kx, width, height, grid.encode())
        return GXIMG(ret_val)



    @classmethod
    def create_out_file(cls, type, grid, img):
        """
        Creates an output image file using input image info.
        
        :param type:  Data type, :ref:`GS_TYPES` or `GS_TYPE_DEFAULT <geosoft.gxapi.GS_TYPE_DEFAULT>`
        :param grid:  Name of the Grid to link to
        :param img:   Input Image for new image creation
        :type  type:  int
        :type  grid:  str
        :type  img:   GXIMG

        :returns:     `GXIMG <geosoft.gxapi.GXIMG>` object
        :rtype:       GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** When the `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` data type is chosen the actual on-disk
        type of the input image will be used instead of `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        if the on-disk values represent color data as opposed
        to real numbers.
        """
        ret_val = gxapi_cy.WrapIMG._create_out_file(GXContext._get_tls_geo(), type, grid.encode(), img)
        return GXIMG(ret_val)




    def create_projected(self, ipj):
        """
        Applies a projection to an image.
        
        :param ipj:  Projection to apply
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` now appears to be in the projected coordinate
        system space.
        """
        self._create_projected(ipj)
        




    def create_projected2(self, ipj, cell_size):
        """
        Applies a projection to an image, specify cell size.
        
        :param ipj:        Projection to apply
        :param cell_size:  Cell size
        :type  ipj:        GXIPJ
        :type  cell_size:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` now appears to be in the projected coordinate
        system space, with the specified cell size. If the cell
        size is `rDUMMY <geosoft.gxapi.rDUMMY>` (`GS_R8DM <geosoft.gxapi.GS_R8DM>`), one is automatically calculated,
        as with `create_projected <geosoft.gxapi.GXIMG.create_projected>`.
        """
        self._create_projected2(ipj, cell_size)
        




    def create_projected3(self, ipj, cell_size, exp_pct):
        """
        Same as `create_projected2 <geosoft.gxapi.GXIMG.create_projected2>`, but set expansion of bounds.
        
        :param ipj:        Projection to apply
        :param cell_size:  Cell size
        :param exp_pct:    Expansion percent (>=0).
        :type  ipj:        GXIPJ
        :type  cell_size:  float
        :type  exp_pct:    float

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXIMG <geosoft.gxapi.GXIMG>` now appears to be in the projected coordinate
        system space, with the specified cell size. If the cell
        size is `rDUMMY <geosoft.gxapi.rDUMMY>` (`GS_R8DM <geosoft.gxapi.GS_R8DM>`), one is automatically calculated,
        as with `create_projected <geosoft.gxapi.GXIMG.create_projected>`.
        The expansion percent expands the bounds of the projected grid
        in order to allow for the curving of bounding edges. Normally,
        edges are sampled in order to allow for curving, but this
        parameter is set to 1.0 (for 1 percent) in the `create_projected <geosoft.gxapi.GXIMG.create_projected>`
        and `create_projected2 <geosoft.gxapi.GXIMG.create_projected2>` wrappers, and will generally create a
        white/dummy border around the new grid. This new method allows
        you to specify the expansion, or turn it off (by setting it to 0).
        If the value is set to `rDUMMY <geosoft.gxapi.rDUMMY>`, then expansion is left at 1.0,
        the legacy behaviour.
        """
        self._create_projected3(ipj, cell_size, exp_pct)
        






    def geth_pg(self):
        """
        Get the actual pager of a grid.
        

        :returns:    `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:      GXPG

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `get_pg <geosoft.gxapi.GXIMG.get_pg>` to get just a copy of the grid's pager.
        """
        ret_val = self._geth_pg()
        return GXPG(ret_val)




    def get_info(self, dx, dy, xo, yo, rot):
        """
        Retrieves location information about this image.
        
        :param dx:   X element separation
        :param dy:   Y element separation
        :param xo:   X location of first point
        :param yo:   Y location of first point
        :param rot:  Grid X axis rotation deg. CCW from reference X
        :type  dx:   float_ref
        :type  dy:   float_ref
        :type  xo:   float_ref
        :type  yo:   float_ref
        :type  rot:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        dx.value, dy.value, xo.value, yo.value, rot.value = self._get_info(dx.value, dy.value, xo.value, yo.value, rot.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection of a grid.
        
        :param ipj:  Projection of the grid
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def get_meta(self, meta):
        """
        Get the metadata of a grid.
        
        :param meta:  Metadata of the grid
        :type  meta:  GXMETA

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_meta(meta)
        




    def get_pg(self, pg):
        """
        Get a copy of the pager of a grid.
        
        :param pg:   `GXPG <geosoft.gxapi.GXPG>` object to hold pager of the grid
        :type  pg:   GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `geth_pg <geosoft.gxapi.GXIMG.geth_pg>` to get the actual pager of the grid.
        """
        self._get_pg(pg)
        




    def get_projected_cell_size(self, ipj, cell):
        """
        Returns default cell size from projected image.
        
        :param ipj:   Projection to apply
        :param cell:  Returned cell size
        :type  ipj:   GXIPJ
        :type  cell:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the cell size calculated by CreateProjected_PJIMG, or by
        `create_projected2 <geosoft.gxapi.GXIMG.create_projected2>` when
        `GS_R8DM <geosoft.gxapi.GS_R8DM>` is entered as the optional cell size. No inheritance
        is actually performed to the input `GXIMG <geosoft.gxapi.GXIMG>`.
        """
        cell.value = self._get_projected_cell_size(ipj, cell.value)
        




    def get_tr(self, tr):
        """
        Get the trend information from a grid.
        
        :param tr:   Trend information from the grid
        :type  tr:   GXTR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_tr(tr)
        




    def element_type(self, xg_dor_img):
        """
        Returns the element type.
        
        :param xg_dor_img:  0 for XGD, 1 for `GXIMG <geosoft.gxapi.GXIMG>`
        :type  xg_dor_img:  int

        :returns:           Element type
        :rtype:             int

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._element_type(xg_dor_img)
        return ret_val




    def e_type(self):
        """
        Returns the element type.
        

        :returns:    Element type
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Same as sElementType_IMG(img,1)
        """
        ret_val = self._e_type()
        return ret_val




    def get_def_itr(self, itr):
        """
        Get default transform, if it exists
        
        :param itr:  Transform
        :type  itr:  GXITR

        :returns:    0 - Okay
                     1 - No default possible/available
        :rtype:      int

        .. versionadded:: 5.0.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_def_itr(itr)
        return ret_val




    def is_colour(self):
        """
        Is this a Geosoft color grid?
        
        :rtype:      bool

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_colour()
        return ret_val



    @classmethod
    def is_valid_img_file(cls, file):
        """
        Is this a valid `GXIMG <geosoft.gxapi.GXIMG>` file?
        
        :param file:  File to check
        :type  file:  str
        :rtype:       bool

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIMG._is_valid_img_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def is_valid_img_file_ex(cls, file, err_msg):
        """
        Is this a valid `GXIMG <geosoft.gxapi.GXIMG>` file? Returns error message if it cannot be opened for any reason.
        
        :param file:     File to check
        :param err_msg:  Error message registered if unable to open
        :type  file:     str
        :type  err_msg:  str_ref
        :rtype:          bool

        .. versionadded:: 8.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, err_msg.value = gxapi_cy.WrapIMG._is_valid_img_file_ex(GXContext._get_tls_geo(), file.encode(), err_msg.value.encode())
        return ret_val




    def ne(self):
        """
        Gets the # of elements in the optimal KX direction.
        

        :returns:    # of elements in the optimal KX direction
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._ne()
        return ret_val




    def inherit(self, ipj, cell):
        """
        Inherit a projection/new cell size on the `GXIMG <geosoft.gxapi.GXIMG>`.
        
        :param ipj:   Projection
        :param cell:  Optional cell size
        :type  ipj:   GXIPJ
        :type  cell:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If cell size is `GS_R8DM <geosoft.gxapi.GS_R8DM>`, then "nice" values for the cell
        size of the new projected grid will be determined so that
        the new grid has about the same number of cells as the old.
        If the cell size is specified, the inheritance will always
        work, even if the input `GXIPJ <geosoft.gxapi.GXIPJ>` is identical to the original
        `GXIPJ <geosoft.gxapi.GXIPJ>`, and the cell boundaries will be forced to be aligned
        with the new cell size.
        """
        self._inherit(ipj, cell)
        




    def inherit_img(self, im_gs):
        """
        Make a grids match in size and coordinate system
        
        :param im_gs:  Source `GXIMG <geosoft.gxapi.GXIMG>`
        :type  im_gs:  GXIMG

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._inherit_img(im_gs)
        




    def nv(self):
        """
        Gets the # of vectors in the optimal KX direction.
        

        :returns:    # of vectors in the optimal KX direction
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._nv()
        return ret_val




    def nx(self):
        """
        Gets the # of X elements.
        

        :returns:    # of X elements.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._nx()
        return ret_val




    def ny(self):
        """
        Gets the # of Y elements.
        

        :returns:    # of Y elements.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._ny()
        return ret_val




    def query_int(self, query):
        """
        Query information about the `GXIMG <geosoft.gxapi.GXIMG>`
        
        :param query:  :ref:`IMG_QUERY`
        :type  query:  int

        :returns:      Information requested, dummy if unknown or invalid.
        :rtype:        int

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** You can call either funtion to retrieve any data,
        int or real.
        """
        ret_val = self._query_int(query)
        return ret_val




    def query_kx(self):
        """
        Asks the `GXIMG <geosoft.gxapi.GXIMG>` for the most efficient way to access the data.
        

        :returns:    -1 by columns, 1 by rows, 0 rows and columns are equally efficient.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._query_kx()
        return ret_val




    def set_def_itr(self, itr):
        """
        Set default transform
        
        :param itr:  Transform
        :type  itr:  GXITR

        :returns:    0 - Okay
                     1 - No default possible/available
        :rtype:      int

        .. versionadded:: 5.0.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._set_def_itr(itr)
        return ret_val



    @classmethod
    def user_preference_to_plot_as_colour_shaded_grid(cls):
        """
        Returns the global setting.
        

        :returns:    0 - User wishes to plot grids as regular (flat) grid
                  1 - User wishes to plot grids as color-shaded grids
        :rtype:      int

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIMG._user_preference_to_plot_as_colour_shaded_grid(GXContext._get_tls_geo())
        return ret_val




    def load_img(self, im_gi):
        """
        Loads an `GXIMG <geosoft.gxapi.GXIMG>` into a master `GXIMG <geosoft.gxapi.GXIMG>`.
        
        :param im_gi:  `GXIMG <geosoft.gxapi.GXIMG>` to load
        :type  im_gi:  GXIMG

        .. versionadded:: 5.0.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The cell sizes and projections must be the same.
        """
        self._load_img(im_gi)
        




    def load_into_pager(self):
        """
        Load `GXIMG <geosoft.gxapi.GXIMG>` data from file into a pager to increase
        access time.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._load_into_pager()
        




    def opt_kx(self, kx):
        """
        Force optimal KX as desired.
        
        :param kx:   KX -1 by column 1 by row
        :type  kx:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This will force loading an image into a `GXPG <geosoft.gxapi.GXPG>` if it is not already
        accessible in the direction requested.

        Subsequent calls to methods that use the optimal KX will use the
        KX set here.
        """
        self._opt_kx(kx)
        




    def read_v(self, v, be, ne, vv):
        """
        Read a vector in the optimal KX direction.
        
        :param v:    Vector to Read
        :param be:   Begining element # to read (0 is the first)
        :param ne:   # elements to read (0 for whole vector)
        :param vv:   `GXVV <geosoft.gxapi.GXVV>` handle
        :type  v:    int
        :type  be:   int
        :type  ne:   int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_v(v, be, ne, vv)
        




    def read_x(self, bx, by, ny, vv):
        """
        Read a column (constant X)
        
        :param bx:   X column
        :param by:   Start Y to read
        :param ny:   # Y to read (0 for whole vector)
        :type  bx:   int
        :type  by:   int
        :type  ny:   int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_x(bx, by, ny, vv)
        




    def read_y(self, by, bx, nx, vv):
        """
        Read a row (constant Y)
        
        :param by:   Y row
        :param bx:   Start X to read
        :param nx:   # X to read (0 for whole vector)
        :type  by:   int
        :type  bx:   int
        :type  nx:   int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_y(by, bx, nx, vv)
        



    @classmethod
    def refresh_gi(cls, grid):
        """
        Refresh the GI of a grid after it has moved or changed.
        
        :param grid:  Grid name
        :type  grid:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMG._refresh_gi(GXContext._get_tls_geo(), grid.encode())
        




    def relocate(self, min_x, min_y, max_x, max_y, asp):
        """
        Re-locate a grid image.
        
        :param min_x:  Area X minimum
        :param min_y:  Area Y minimum
        :param max_x:  Area X maximum
        :param max_y:  Area Y maximum
        :param asp:    :ref:`IMG_RELOCATE`
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  asp:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._relocate(min_x, min_y, max_x, max_y, asp)
        



    @classmethod
    def report(cls, grid, wa, force, decimals, title):
        """
        Writes grid info report to a file
        
        :param grid:      Grid name
        :param wa:        Text file to write to
        :param force:     Recalc statistics (0 - no; 1 - yes)
        :param decimals:  Number of decimals to put in results
        :param title:     Title for report
        :type  grid:      str
        :type  wa:        GXWA
        :type  force:     int
        :type  decimals:  int
        :type  title:     str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMG._report(GXContext._get_tls_geo(), grid.encode(), wa, force, decimals, title.encode())
        



    @classmethod
    def report_csv(cls, grid, wa, force, decimals, header):
        """
        Writes grid info as a line to a CSV file
        
        :param grid:      Grid name
        :param wa:        Text file to write to
        :param force:     Recalc statistics (0 - no; 1 - yes)
        :param decimals:  Number of decimals to put in results
        :param header:    Write header line (0 - no; 1 - yes)?
        :type  grid:      str
        :type  wa:        GXWA
        :type  force:     int
        :type  decimals:  int
        :type  header:    int

        .. versionadded:: 6.4.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Appends the stats as a CSV line to the input text file.
        The header line should only be written to a new text file.
        """
        gxapi_cy.WrapIMG._report_csv(GXContext._get_tls_geo(), grid.encode(), wa, force, decimals, header)
        




    def get_z(self, x, y):
        """
        Gets the grid value at a point
        
        :param x:    X location in the grid projection
        :param y:    Y location in the grid projection
        :type  x:    float
        :type  y:    float

        :returns:    Grid value
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_z(x, y)
        return ret_val




    def query_double(self, query):
        """
        Query information about the `GXIMG <geosoft.gxapi.GXIMG>`
        
        :param query:  :ref:`IMG_QUERY`
        :type  query:  int

        :returns:      Information requested, dummy if unknown or invalid.
        :rtype:        float

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** You can call either funtion to retrieve any data,
        int or real.
        """
        ret_val = self._query_double(query)
        return ret_val




    def set_grid_unchanged(self):
        """
        Mark the grid as unchanged so it will not output lineage
        

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_grid_unchanged()
        




    def set_info(self, dx, dy, xo, yo, rot):
        """
        Sets location information about this image.
        
        :param dx:   X element separation
        :param dy:   Y element separation
        :param xo:   X location of first point
        :param yo:   Y location of first point
        :param rot:  Grid X axis rotation deg. CCW from reference X
        :type  dx:   float
        :type  dy:   float
        :type  xo:   float
        :type  yo:   float
        :type  rot:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Calls to this function should be made BEFORE calls to `set_ipj <geosoft.gxapi.GXIMG.set_ipj>`,
        as the latter function sets up the bounding rectangle in the metadata.
        """
        self._set_info(dx, dy, xo, yo, rot)
        




    def set_ipj(self, ipj):
        """
        Set the projection of a grid.
        
        :param ipj:  Projection
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Calls to this function should be made AFTER calls to `set_info <geosoft.gxapi.GXIMG.set_info>`,
        as `set_ipj <geosoft.gxapi.GXIMG.set_ipj>` sets up the bounding rectangle in the metadata.
        """
        self._set_ipj(ipj)
        




    def set_meta(self, meta):
        """
        Set the metadata of a grid.
        
        :param meta:  Metadata to add to the grid
        :type  meta:  GXMETA

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta(meta)
        




    def set_pg(self, pg):
        """
        Copy a pager into the pager of a grid.
        
        :param pg:   Pager object to copy into the pager of the grid
        :type  pg:   GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_pg(pg)
        




    def set_tr(self, tr):
        """
        Set the trend information to a grid.
        
        :param tr:   Trend information to set for the grid
        :type  tr:   GXTR

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_tr(tr)
        



    @classmethod
    def sync(cls, grid):
        """
        Syncronize the Metadata for this Grid
        
        :param grid:  Grid name
        :type  grid:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapIMG._sync(GXContext._get_tls_geo(), grid.encode())
        




    def write_v(self, v, be, ne, vv):
        """
        Write a vector in the optimal KX direction.
        
        :param v:    Vector to write
        :param be:   Begining element to write (0 is the first)
        :param ne:   # elements to write (0 for whole vector)
        :param vv:   `GXVV <geosoft.gxapi.GXVV>` handle
        :type  v:    int
        :type  be:   int
        :type  ne:   int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_v(v, be, ne, vv)
        




    def write_x(self, bx, by, ny, vv):
        """
        Write a column (constant X)
        
        :param bx:   X column
        :param by:   Start Y to write
        :param ny:   # Y to write (0 for whole vector)
        :type  bx:   int
        :type  by:   int
        :type  ny:   int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_x(bx, by, ny, vv)
        




    def write_y(self, by, bx, nx, vv):
        """
        Write a row (constant Y)
        
        :param by:   Y row
        :param bx:   Start X to write
        :param nx:   # X write (0 for whole vector)
        :type  by:   int
        :type  bx:   int
        :type  nx:   int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_y(by, bx, nx, vv)
        




    def set_double_parameter(self, name, value):
        """
        Store a real parameter in an `GXIMG <geosoft.gxapi.GXIMG>` object
        
        :param name:   Parameter name (case insensitive)
        :param value:  Parameter value to store
        :type  name:   str
        :type  value:  float

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_double_parameter(name.encode(), value)
        




    def get_double_parameter(self, name):
        """
        Store a real parameter in an `GXIMG <geosoft.gxapi.GXIMG>` object
        
        :param name:  Parameter name (case insensitive)
        :type  name:  str

        :returns:     Parameter value, `rDUMMY <geosoft.gxapi.rDUMMY>` if not found.
        :rtype:       float

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_double_parameter(name.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer