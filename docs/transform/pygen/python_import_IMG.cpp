#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXIMG_wrap_average2(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXIMG::average2(arg1, arg2);
}
inline void GXIMG_wrap_copy(GXIMGPtr self, GXIMGPtr arg1)
{
    self->copy(arg1);
}
inline GXIMGPtr GXIMG_wrap_create(int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXIMGPtr ret = GXIMG::create((GS_TYPES)arg1, arg2, arg3, arg4);
    return ret;
}
inline GXIMGPtr GXIMG_wrap_create_file(int32_t arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXIMGPtr ret = GXIMG::create_file((GS_TYPES)arg1, arg2, (IMG_FILE)arg3);
    return ret;
}
inline GXIMGPtr GXIMG_wrap_create_mem(int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXIMGPtr ret = GXIMG::create_mem((GS_TYPES)arg1, arg2, arg3, arg4);
    return ret;
}
inline GXIMGPtr GXIMG_wrap_create_new_file(int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5)
{
    GXIMGPtr ret = GXIMG::create_new_file((GS_TYPES)arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline GXIMGPtr GXIMG_wrap_create_out_file(int32_t arg1, const gx_string_type& arg2, GXIMGPtr arg3)
{
    GXIMGPtr ret = GXIMG::create_out_file((GS_TYPES)arg1, arg2, arg3);
    return ret;
}
inline void GXIMG_wrap_create_projected(GXIMGPtr self, GXIPJPtr arg1)
{
    self->create_projected(arg1);
}
inline void GXIMG_wrap_create_projected2(GXIMGPtr self, GXIPJPtr arg1, double arg2)
{
    self->create_projected2(arg1, arg2);
}
inline void GXIMG_wrap_create_projected3(GXIMGPtr self, GXIPJPtr arg1, double arg2, double arg3)
{
    self->create_projected3(arg1, arg2, arg3);
}
inline GXPGPtr GXIMG_wrap_geth_pg(GXIMGPtr self)
{
    GXPGPtr ret = self->geth_pg();
    return ret;
}
inline void GXIMG_wrap_get_info(GXIMGPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    self->get_info(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMG_wrap_get_ipj(GXIMGPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXIMG_wrap_get_meta(GXIMGPtr self, GXMETAPtr arg1)
{
    self->get_meta(arg1);
}
inline void GXIMG_wrap_get_pg(GXIMGPtr self, GXPGPtr arg1)
{
    self->get_pg(arg1);
}
inline void GXIMG_wrap_get_projected_cell_size(GXIMGPtr self, GXIPJPtr arg1, float_ref& arg2)
{
    self->get_projected_cell_size(arg1, arg2);
}
inline void GXIMG_wrap_get_tr(GXIMGPtr self, GXTRPtr arg1)
{
    self->get_tr(arg1);
}
inline int32_t GXIMG_wrap_element_type(GXIMGPtr self, int32_t arg1)
{
    int32_t ret = self->element_type(arg1);
    return ret;
}
inline int32_t GXIMG_wrap_e_type(GXIMGPtr self)
{
    int32_t ret = self->e_type();
    return ret;
}
inline int32_t GXIMG_wrap_get_def_itr(GXIMGPtr self, GXITRPtr arg1)
{
    int32_t ret = self->get_def_itr(arg1);
    return ret;
}
inline bool GXIMG_wrap_is_colour(GXIMGPtr self)
{
    bool ret = self->is_colour();
    return ret;
}
inline bool GXIMG_wrap_is_valid_img_file(const gx_string_type& arg1)
{
    bool ret = GXIMG::is_valid_img_file(arg1);
    return ret;
}
inline bool GXIMG_wrap_is_valid_img_file_ex(const gx_string_type& arg1, str_ref& arg2)
{
    bool ret = GXIMG::is_valid_img_file_ex(arg1, arg2);
    return ret;
}
inline int32_t GXIMG_wrap_ne(GXIMGPtr self)
{
    int32_t ret = self->ne();
    return ret;
}
inline void GXIMG_wrap_inherit(GXIMGPtr self, GXIPJPtr arg1, double arg2)
{
    self->inherit(arg1, arg2);
}
inline void GXIMG_wrap_inherit_img(GXIMGPtr self, GXIMGPtr arg1)
{
    self->inherit_img(arg1);
}
inline int32_t GXIMG_wrap_nv(GXIMGPtr self)
{
    int32_t ret = self->nv();
    return ret;
}
inline int32_t GXIMG_wrap_nx(GXIMGPtr self)
{
    int32_t ret = self->nx();
    return ret;
}
inline int32_t GXIMG_wrap_ny(GXIMGPtr self)
{
    int32_t ret = self->ny();
    return ret;
}
inline int32_t GXIMG_wrap_query_int(GXIMGPtr self, int32_t arg1)
{
    int32_t ret = self->query_int((IMG_QUERY)arg1);
    return ret;
}
inline int32_t GXIMG_wrap_query_kx(GXIMGPtr self)
{
    int32_t ret = self->query_kx();
    return ret;
}
inline int32_t GXIMG_wrap_set_def_itr(GXIMGPtr self, GXITRPtr arg1)
{
    int32_t ret = self->set_def_itr(arg1);
    return ret;
}
inline int32_t GXIMG_wrap_user_preference_to_plot_as_colour_shaded_grid()
{
    int32_t ret = GXIMG::user_preference_to_plot_as_colour_shaded_grid();
    return ret;
}
inline void GXIMG_wrap_load_img(GXIMGPtr self, GXIMGPtr arg1)
{
    self->load_img(arg1);
}
inline void GXIMG_wrap_load_into_pager(GXIMGPtr self)
{
    self->load_into_pager();
}
inline void GXIMG_wrap_opt_kx(GXIMGPtr self, int32_t arg1)
{
    self->opt_kx(arg1);
}
inline void GXIMG_wrap_read_v(GXIMGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->read_v(arg1, arg2, arg3, arg4);
}
inline void GXIMG_wrap_read_x(GXIMGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->read_x(arg1, arg2, arg3, arg4);
}
inline void GXIMG_wrap_read_y(GXIMGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->read_y(arg1, arg2, arg3, arg4);
}
inline void GXIMG_wrap_refresh_gi(const gx_string_type& arg1)
{
    GXIMG::refresh_gi(arg1);
}
inline void GXIMG_wrap_relocate(GXIMGPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5)
{
    self->relocate(arg1, arg2, arg3, arg4, (IMG_RELOCATE)arg5);
}
inline void GXIMG_wrap_report(const gx_string_type& arg1, GXWAPtr arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5)
{
    GXIMG::report(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMG_wrap_report_csv(const gx_string_type& arg1, GXWAPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXIMG::report_csv(arg1, arg2, arg3, arg4, arg5);
}
inline double GXIMG_wrap_get_z(GXIMGPtr self, double arg1, double arg2)
{
    double ret = self->get_z(arg1, arg2);
    return ret;
}
inline double GXIMG_wrap_query_double(GXIMGPtr self, int32_t arg1)
{
    double ret = self->query_double((IMG_QUERY)arg1);
    return ret;
}
inline void GXIMG_wrap_set_grid_unchanged(GXIMGPtr self)
{
    self->set_grid_unchanged();
}
inline void GXIMG_wrap_set_info(GXIMGPtr self, double arg1, double arg2, double arg3, double arg4, double arg5)
{
    self->set_info(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMG_wrap_set_ipj(GXIMGPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXIMG_wrap_set_meta(GXIMGPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}
inline void GXIMG_wrap_set_pg(GXIMGPtr self, GXPGPtr arg1)
{
    self->set_pg(arg1);
}
inline void GXIMG_wrap_set_tr(GXIMGPtr self, GXTRPtr arg1)
{
    self->set_tr(arg1);
}
inline void GXIMG_wrap_sync(const gx_string_type& arg1)
{
    GXIMG::sync(arg1);
}
inline void GXIMG_wrap_write_v(GXIMGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->write_v(arg1, arg2, arg3, arg4);
}
inline void GXIMG_wrap_write_x(GXIMGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->write_x(arg1, arg2, arg3, arg4);
}
inline void GXIMG_wrap_write_y(GXIMGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->write_y(arg1, arg2, arg3, arg4);
}
inline void GXIMG_wrap_set_double_parameter(GXIMGPtr self, const gx_string_type& arg1, double arg2)
{
    self->set_double_parameter(arg1, arg2);
}
inline double GXIMG_wrap_get_double_parameter(GXIMGPtr self, const gx_string_type& arg1)
{
    double ret = self->get_double_parameter(arg1);
    return ret;
}

void gxPythonImportGXIMG()
{

    class_<GXIMG, GXIMGPtr> pyClass("GXIMG",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The IMG class performs read and write operations on grid\n"
                                    "   		file data. When efficient access along both rows and columns\n"
                                    "   		is desired the PG class is recommended (see PG and PGU);\n"
                                    "   		the IMG is first created, then the PG is obtained from\n"
                                    "   		the IMG using \\ :func:`geosoft.gxapi.GXIMG.get_pg`\\ .\n"
                                    "   	\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The IMG methods use the XGD DATs to access grid files in different\n"
                                    "   		formats.  The characteristics of a grid can be controlled using\n"
                                    "   		decorations on a grid file name.  For example:\n"
                                    "   \n"
                                    "   		\\ :func:`geosoft.gxapi.GXIMG.create_new_file`\\ (GS_DOUBLE,1,100,100,\"mag.grd\");\n"
                                    "   		-> creates a new grid file \"mag.grd\" with all defaults.\n"
                                    "   \n"
                                    "   		\\ :func:`geosoft.gxapi.GXIMG.create_new_file`\\ (GS_DOUBLE,1,100,100,\"mag.grd(GRD;comp=none)\");\n"
                                    "   		-> creates a new grid file \"mag.grd\" with no compression.\n"
                                    "   \n"
                                    "   		\\ :func:`geosoft.gxapi.GXIMG.create_new_file`\\ (GS_DOUBLE,1,100,100,\"mag.grd(GRD;comp=size;type=short\");\n"
                                    "   		-> creates a new grid file \"mag.grd\" compressed for size, numbers\n"
                                    "   		stored as 2-byte integers..\n"
                                    "   \n"
                                    "   		See DAT_XGD.DOC for information about file name decorations available\n"
                                    "   		for all DAT types.\n"
                                    "   \n"
                                    "   		Different grid types support different features.  For example, not all\n"
                                    "   		grid types support projection information.  Geosoft will always create\n"
                                    "   		a \\ `*`\\ .gi file that is used to store all such information that we require\n"
                                    "   		from a grid.  If the grid does support this information, both the grid\n"
                                    "   		and the \\ `*`\\ .gi file will contain the information.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXIMG::null, "null() -> GXIMG\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXIMG`\n\n:returns: A null :class:`geosoft.gxapi.GXIMG`\n:rtype: :class:`geosoft.gxapi.GXIMG`\n").staticmethod("null");
    pyClass.def("is_null", &GXIMG::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXIMG is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXIMG`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXIMG::_internal_handle);
    pyClass.def("average2", &GXIMG_wrap_average2,
                "average2((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reduce the dimensions in a 2D pager by a factor of 2\n\n"

                ":param arg1: Name of source Grid\n"
                ":type arg1: str\n"
                ":param arg2: Name of output Grid\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method is useful for reducing the dimensions in a 2D pager by a factor of 2.\n"
                "   					The output pager retains the same origin, but the X and Y spacing is double that of the original. Essentially,\n"
                "   					the process removes all the even-indexed rows and columns, while leaving the locations of all the remaining\n"
                "   					data points in the \"odd\" rows and columns unchanged.\n"
                "   \n"
                "   					The output values at the output data locations are created by performing an average of the original data point and\n"
                "   					its valid surrounding data points; what is essentially a 3x3 smoothing filter.\n"
                "   				\n\n"
               ).staticmethod("average2");
    pyClass.def("copy", &GXIMG_wrap_copy,
                "copy((GXIMG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy IMGs.\n\n"

                ":param arg1: target IMG\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXIMG_wrap_create,
                "create((int)arg1, (int)arg2, (int)arg3, (int)arg4) -> GXIMG:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an IMG not tied to a file at all\n\n"

                ":param arg1: Data type \\ :ref:`GS_TYPES`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Grid orientation (KX): 1 (rows in X) -1 (rows in Y)\n"
                ":type arg2: int\n"
                ":param arg3: Grid width\n"
                ":type arg3: int\n"
                ":param arg4: Grid height\n"
                ":type arg4: int\n"
                ":returns: IMG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIMG`\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Once destroyed all the data in this IMG is lost.\n\n"
               ).staticmethod("create");
    pyClass.def("create_file", &GXIMG_wrap_create_file,
                "create_file((int)arg1, (str)arg2, (int)arg3) -> GXIMG:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an Image object tied to a grid file.\n\n"

                ":param arg1: Data type, \\ :ref:`GS_TYPES`\\  or GS_TYPE_DEFAULT to use native DAT type.\n"
                ":type arg1: int\n"
                ":param arg2: Name of the Grid to link to\n"
                ":type arg2: str\n"
                ":param arg3: Grid File Open Mode \\ :ref:`IMG_FILE`\\ \n"
                ":type arg3: int\n"
                ":returns: IMG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIMG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					When the GS_DOUBLE data type is chosen the actual on-disk\n"
                "   					type of the input image will be used instead of GS_DOUBLE\n"
                "   					if the on-disk values represent colour data as opposed\n"
                "   					to real numbers.\n"
                "   				\n\n"
               ).staticmethod("create_file");
    pyClass.def("create_mem", &GXIMG_wrap_create_mem,
                "create_mem((int)arg1, (int)arg2, (int)arg3, (int)arg4) -> GXIMG:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an IMG object that is backed only by memory.\n\n"

                ":param arg1: Data type, \\ :ref:`GS_TYPES`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Grid orientation (KX): 1 (rows in X) -1 (rows in Y)\n"
                ":type arg2: int\n"
                ":param arg3: Grid width\n"
                ":type arg3: int\n"
                ":param arg4: Grid height\n"
                ":type arg4: int\n"
                ":returns: IMG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIMG`\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Once destroyed all the data is lost. This is temporary.\n\n"
               ).staticmethod("create_mem");
    pyClass.def("create_new_file", &GXIMG_wrap_create_new_file,
                "create_new_file((int)arg1, (int)arg2, (int)arg3, (int)arg4, (str)arg5) -> GXIMG:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an output image file using User defined info.\n\n"

                ":param arg1: Data type, \\ :ref:`GS_TYPES`\\  Cannot be GS_TYPE_DEFAULT\n"
                ":type arg1: int\n"
                ":param arg2: Grid orientation (KX): 1 (rows in X) -1 (rows in Y)\n"
                ":type arg2: int\n"
                ":param arg3: Grid width\n"
                ":type arg3: int\n"
                ":param arg4: Grid height\n"
                ":type arg4: int\n"
                ":param arg5: Name of the Grid to link to\n"
                ":type arg5: str\n"
                ":returns: IMG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIMG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Special Note for developers who use this function and\n"
                "   					related functions to output ERMapper image (ERS, ECW) files:\n"
                "   \n"
                "   					This function internally called ERMapper plugin to create ERS header\n"
                "   					files. To find the location of ERMapper plugin library, a registry setting\n"
                "   					needs to set. The key in the registry is HKEY_LOCAL_MACHINE\\SOFTWARE\\\"MyProgram(libversion7.0)\"\n"
                "   					and in that key register a string BASE_PATH = D:\\Oasismontaj\\plugins\\er_mapper.\n"
                "   					MyProgram is the name of your application and D:\\Oasismontaj\\plugins\\er_mapper\n"
                "   					is the location of ERMapper library.\n"
                "   \n"
                "   					It is recommended that this registry key is set during the installation\n"
                "   					of your application.\n"
                "   				\n\n"
               ).staticmethod("create_new_file");
    pyClass.def("create_out_file", &GXIMG_wrap_create_out_file,
                "create_out_file((int)arg1, (str)arg2, (GXIMG)arg3) -> GXIMG:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an output image file using input image info.\n\n"

                ":param arg1: Data type, \\ :ref:`GS_TYPES`\\  or GS_TYPE_DEFAULT\n"
                ":type arg1: int\n"
                ":param arg2: Name of the Grid to link to\n"
                ":type arg2: str\n"
                ":param arg3: Input Image for new image creation\n"
                ":type arg3: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: IMG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIMG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					When the GS_DOUBLE data type is chosen the actual on-disk\n"
                "   					type of the input image will be used instead of GS_DOUBLE\n"
                "   					if the on-disk values represent colour data as opposed\n"
                "   					to real numbers.\n"
                "   				\n\n"
               ).staticmethod("create_out_file");
    pyClass.def("create_projected", &GXIMG_wrap_create_projected,
                "create_projected((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Applies a projection to an image.\n\n"

                ":param arg1: Projection to apply\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG now appears to be in the projected coordinate\n"
                "   					system space.\n"
                "   				\n\n"
               );
    pyClass.def("create_projected2", &GXIMG_wrap_create_projected2,
                "create_projected2((GXIPJ)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Applies a projection to an image, specify cell size.\n\n"

                ":param arg1: Projection to apply\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Cell size\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG now appears to be in the projected coordinate\n"
                "   					system space, with the specified cell size. If the cell\n"
                "   					size is rDUMMY (GS_R8DM), one is automatically calculated,\n"
                "   					as with \\ :func:`geosoft.gxapi.GXIMG.create_projected`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("create_projected3", &GXIMG_wrap_create_projected3,
                "create_projected3((GXIPJ)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIMG.create_projected2`\\ , but set expansion of bounds.\n\n"

                ":param arg1: Projection to apply\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Cell size\n"
                ":type arg2: float\n"
                ":param arg3: Expansion percent (>=0).\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG now appears to be in the projected coordinate\n"
                "   					system space, with the specified cell size. If the cell\n"
                "   					size is rDUMMY (GS_R8DM), one is automatically calculated,\n"
                "   					as with \\ :func:`geosoft.gxapi.GXIMG.create_projected`\\ .\n"
                "   					The expansion percent expands the bounds of the projected grid\n"
                "   					in order to allow for the curving of bounding edges. Normally,\n"
                "   					edges are sampled in order to allow for curving, but this\n"
                "   					parameter is set to 1.0 (for 1 percent) in the \\ :func:`geosoft.gxapi.GXIMG.create_projected`\\ \n"
                "   					and \\ :func:`geosoft.gxapi.GXIMG.create_projected2`\\  wrappers, and will generally create a\n"
                "   					white/dummy border around the new grid. This new method allows\n"
                "   					you to specify the expansion, or turn it off (by setting it to 0).\n"
                "   					If the value is set to rDUMMY, then expansion is left at 1.0,\n"
                "   					the legacy behaviour.\n"
                "   				\n\n"
               );
    pyClass.def("geth_pg", &GXIMG_wrap_geth_pg,
                "geth_pg() -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the actual pager of a grid.\n\n"

                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXIMG.get_pg`\\  to get just a copy of the grid's pager.\n\n"
               );
    pyClass.def("get_info", &GXIMG_wrap_get_info,
                "get_info((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieves location information about this image.\n\n"

                ":param arg1: X element separation\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y element separation\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: X location of first point\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y location of first point\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: grid X axis rotation deg. CCW from reference X\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_ipj", &GXIMG_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the projection of a grid.\n\n"

                ":param arg1: Projection of the grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_meta", &GXIMG_wrap_get_meta,
                "get_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the metadata of a grid.\n\n"

                ":param arg1: Metadata of the grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("get_pg", &GXIMG_wrap_get_pg,
                "get_pg((GXPG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a copy of the pager of a grid.\n\n"

                ":param arg1: PG object to hold pager of the grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXIMG.geth_pg`\\  to get the actual pager of the grid.\n\n"
               );
    pyClass.def("get_projected_cell_size", &GXIMG_wrap_get_projected_cell_size,
                "get_projected_cell_size((GXIPJ)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns default cell size from projected image.\n\n"

                ":param arg1: Projection to apply\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Returned cell size\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns the cell size calculated by CreateProjected_PJIMG, or by\n"
                "   					\\ :func:`geosoft.gxapi.GXIMG.create_projected2`\\  when\n"
                "   					GS_R8DM is entered as the optional cell size. No inheritance\n"
                "   					is actually performed to the input IMG.\n"
                "   				\n\n"
               );
    pyClass.def("get_tr", &GXIMG_wrap_get_tr,
                "get_tr((GXTR)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the trend information from a grid.\n\n"

                ":param arg1: Trend information from the grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXTR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("element_type", &GXIMG_wrap_element_type,
                "element_type((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the element type.\n\n"

                ":param arg1: 0 for XGD, 1 for IMG\n"
                ":type arg1: int\n"
                ":returns: Element type\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               );
    pyClass.def("e_type", &GXIMG_wrap_e_type,
                "e_type() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the element type.\n\n"

                ":returns: Element type\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as sElementType_IMG(img,1)\n\n"
               );
    pyClass.def("get_def_itr", &GXIMG_wrap_get_def_itr,
                "get_def_itr((GXITR)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get default transform, if it exists\n\n"

                ":param arg1: transform\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: 0 - Okay\n"
                "          						1 - No default possible/available\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.2\n\n"
               );
    pyClass.def("is_colour", &GXIMG_wrap_is_colour,
                "is_colour() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a Geosoft colour grid?\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("is_valid_img_file", &GXIMG_wrap_is_valid_img_file,
                "is_valid_img_file((str)arg1) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a valid IMG file?\n\n"

                ":param arg1: File to check\n"
                ":type arg1: str\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("is_valid_img_file");
    pyClass.def("is_valid_img_file_ex", &GXIMG_wrap_is_valid_img_file_ex,
                "is_valid_img_file_ex((str)arg1, (str_ref)arg2) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a valid IMG file? Returns error message if it cannot be opened for any reason.\n\n"

                ":param arg1: File to check\n"
                ":type arg1: str\n"
                ":param arg2: Error message registered if unable to open\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("is_valid_img_file_ex");
    pyClass.def("ne", &GXIMG_wrap_ne,
                "ne() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the # of elements in the optimal KX direction.\n\n"

                ":returns: # of elements in the optimal KX direction\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("inherit", &GXIMG_wrap_inherit,
                "inherit((GXIPJ)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Inherit a projection/new cell size on the IMG.\n\n"

                ":param arg1: Projection\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Optional cell size\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If cell size is GS_R8DM, then \"nice\" values for the cell\n"
                "   					size of the new projected grid will be determined so that\n"
                "   					the new grid has about the same number of cells as the old.\n"
                "   					If the cell size is specified, the inheritance will always\n"
                "   					work, even if the input IPJ is identical to the original\n"
                "   					IPJ, and the cell boundaries will be forced to be aligned\n"
                "   					with the new cell size.\n"
                "   				\n\n"
               );
    pyClass.def("inherit_img", &GXIMG_wrap_inherit_img,
                "inherit_img((GXIMG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a grids match in size and coordinate system\n\n"

                ":param arg1: source IMG\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("nv", &GXIMG_wrap_nv,
                "nv() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the # of vectors in the optimal KX direction.\n\n"

                ":returns: # of vectors in the optimal KX direction\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("nx", &GXIMG_wrap_nx,
                "nx() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the # of X elements.\n\n"

                ":returns: # of X elements.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("ny", &GXIMG_wrap_ny,
                "ny() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the # of Y elements.\n\n"

                ":returns: # of Y elements.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("query_int", &GXIMG_wrap_query_int,
                "query_int((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Query information about the IMG\n\n"

                ":param arg1: \\ :ref:`IMG_QUERY`\\ \n"
                ":type arg1: int\n"
                ":returns: Information requested, dummy if unknown or invalid.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					You can call either funtion to retrieve any data,\n"
                "   					int or real.\n"
                "   				\n\n"
               );
    pyClass.def("query_kx", &GXIMG_wrap_query_kx,
                "query_kx() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Asks the IMG for the most efficient way to access the data.\n\n"

                ":returns: -1  - by Columns\n"
                "          						0  - Rows or Columns are equally efficient.\n"
                "          						1  - by Rows\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_def_itr", &GXIMG_wrap_set_def_itr,
                "set_def_itr((GXITR)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Set default transform\n\n"

                ":param arg1: transform\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: 0 - Okay\n"
                "          						1 - No default possible/available\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.2\n\n"
               );
    pyClass.def("user_preference_to_plot_as_colour_shaded_grid", &GXIMG_wrap_user_preference_to_plot_as_colour_shaded_grid,
                "user_preference_to_plot_as_colour_shaded_grid() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the global setting.\n\n"

                ":returns: 0 - User wishes to plot grids as regular (flat) grid\n"
                "          						1 - User wishes to plot grids as colour-shaded grids\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               ).staticmethod("user_preference_to_plot_as_colour_shaded_grid");
    pyClass.def("load_img", &GXIMG_wrap_load_img,
                "load_img((GXIMG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads an IMG into a master IMG.\n\n"

                ":param arg1: IMG to load\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Cell sizes and projections must be the same.\n\n"
               );
    pyClass.def("load_into_pager", &GXIMG_wrap_load_into_pager,
                "load_into_pager() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Load IMG data from file into a pager to increase\n"
                "   					access time.\n"
                "   				\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("opt_kx", &GXIMG_wrap_opt_kx,
                "opt_kx((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Force optimal KX as desired.\n\n"

                ":param arg1: KX -1 by column 1 by row\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This will force loading an image into a PG if it is not already\n"
                "   					accessible in the direction requested.\n"
                "   \n"
                "   					Subsequent calls to methods that use the optimal KX will use the\n"
                "   					KX set here.\n"
                "   				\n\n"
               );
    pyClass.def("read_v", &GXIMG_wrap_read_v,
                "read_v((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a vector in the optimal KX direction.\n\n"

                ":param arg1: Vector to Read\n"
                ":type arg1: int\n"
                ":param arg2: begining element # to read (0 is the first)\n"
                ":type arg2: int\n"
                ":param arg3: # elements to read (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: VV handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_x", &GXIMG_wrap_read_x,
                "read_x((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a column (constant X)\n\n"

                ":param arg1: X column\n"
                ":type arg1: int\n"
                ":param arg2: start Y to read\n"
                ":type arg2: int\n"
                ":param arg3: # Y to read (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: VV\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_y", &GXIMG_wrap_read_y,
                "read_y((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a row (constant Y)\n\n"

                ":param arg1: Y row\n"
                ":type arg1: int\n"
                ":param arg2: start X to read\n"
                ":type arg2: int\n"
                ":param arg3: # X to read (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: VV\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("refresh_gi", &GXIMG_wrap_refresh_gi,
                "refresh_gi((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Refresh the GI of a grid after it has moved or changed.\n\n"

                ":param arg1: grid name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("refresh_gi");
    pyClass.def("relocate", &GXIMG_wrap_relocate,
                "relocate((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-locate a grid image.\n\n"

                ":param arg1: area X minimum\n"
                ":type arg1: float\n"
                ":param arg2: area Y minimum\n"
                ":type arg2: float\n"
                ":param arg3: area X maximum\n"
                ":type arg3: float\n"
                ":param arg4: area Y maximum\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`IMG_RELOCATE`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("report", &GXIMG_wrap_report,
                "report((str)arg1, (GXWA)arg2, (int)arg3, (int)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes grid info report to a file\n\n"

                ":param arg1: Grid name\n"
                ":type arg1: str\n"
                ":param arg2: Text file to write to\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: recalc statistics (0 - no; 1 - yes)\n"
                ":type arg3: int\n"
                ":param arg4: number of decimals to put in results\n"
                ":type arg4: int\n"
                ":param arg5: Title for report\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("report");
    pyClass.def("report_csv", &GXIMG_wrap_report_csv,
                "report_csv((str)arg1, (GXWA)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes grid info as a line to a CSV file\n\n"

                ":param arg1: Grid name\n"
                ":type arg1: str\n"
                ":param arg2: Text file to write to\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: recalc statistics (0 - no; 1 - yes)\n"
                ":type arg3: int\n"
                ":param arg4: number of decimals to put in results\n"
                ":type arg4: int\n"
                ":param arg5: Write header line (0 - no; 1 - yes)?\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Appends the stats as a CSV line to the input text file.\n"
                "   					The header line should only be written to a new text file.\n"
                "   				\n\n"
               ).staticmethod("report_csv");
    pyClass.def("get_z", &GXIMG_wrap_get_z,
                "get_z((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the grid value at a point\n\n"

                ":param arg1: X location in the grid projection\n"
                ":type arg1: float\n"
                ":param arg2: Y location in the grid projection\n"
                ":type arg2: float\n"
                ":returns: Grid value\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("query_double", &GXIMG_wrap_query_double,
                "query_double((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Query information about the IMG\n\n"

                ":param arg1: \\ :ref:`IMG_QUERY`\\ \n"
                ":type arg1: int\n"
                ":returns: Information requested, dummy if unknown or invalid.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					You can call either funtion to retrieve any data,\n"
                "   					int or real.\n"
                "   				\n\n"
               );
    pyClass.def("set_grid_unchanged", &GXIMG_wrap_set_grid_unchanged,
                "set_grid_unchanged() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mark the grid as unchanged so it will not output lineage\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_info", &GXIMG_wrap_set_info,
                "set_info((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets location information about this image.\n\n"

                ":param arg1: X element separation\n"
                ":type arg1: float\n"
                ":param arg2: Y element separation\n"
                ":type arg2: float\n"
                ":param arg3: X location of first point\n"
                ":type arg3: float\n"
                ":param arg4: Y location of first point\n"
                ":type arg4: float\n"
                ":param arg5: grid X axis rotation deg. CCW from reference X\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Calls to this function should be made BEFORE calls to \\ :func:`geosoft.gxapi.GXIMG.set_ipj`\\ ,\n"
                "   					as the latter function sets up the bounding rectangle in the metadata.\n"
                "   				\n\n"
               );
    pyClass.def("set_ipj", &GXIMG_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the projection of a grid.\n\n"

                ":param arg1: Projection\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Calls to this function should be made AFTER calls to \\ :func:`geosoft.gxapi.GXIMG.set_info`\\ ,\n"
                "   					as \\ :func:`geosoft.gxapi.GXIMG.set_ipj`\\  sets up the bounding rectangle in the metadata.\n"
                "   				\n\n"
               );
    pyClass.def("set_meta", &GXIMG_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the metadata of a grid.\n\n"

                ":param arg1: Metadata to add to the grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("set_pg", &GXIMG_wrap_set_pg,
                "set_pg((GXPG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a pager into the pager of a grid.\n\n"

                ":param arg1: Pager object to copy into the pager of the grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_tr", &GXIMG_wrap_set_tr,
                "set_tr((GXTR)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the trend information to a grid.\n\n"

                ":param arg1: Trend information to set for the grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXTR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("sync", &GXIMG_wrap_sync,
                "sync((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize the Metadata for this Grid\n\n"

                ":param arg1: grid name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("sync");
    pyClass.def("write_v", &GXIMG_wrap_write_v,
                "write_v((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a vector in the optimal KX direction.\n\n"

                ":param arg1: vector to write\n"
                ":type arg1: int\n"
                ":param arg2: begining element to write (0 is the first)\n"
                ":type arg2: int\n"
                ":param arg3: # elements to write (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: VV handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_x", &GXIMG_wrap_write_x,
                "write_x((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a column (constant X)\n\n"

                ":param arg1: X column\n"
                ":type arg1: int\n"
                ":param arg2: start Y to write\n"
                ":type arg2: int\n"
                ":param arg3: # Y to write (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: VV\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_y", &GXIMG_wrap_write_y,
                "write_y((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a row (constant Y)\n\n"

                ":param arg1: Y row\n"
                ":type arg1: int\n"
                ":param arg2: start X to write\n"
                ":type arg2: int\n"
                ":param arg3: # X write (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: VV\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_double_parameter", &GXIMG_wrap_set_double_parameter,
                "set_double_parameter((str)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Store a real parameter in an IMG object\n\n"

                ":param arg1: Parameter name (case insensitive)\n"
                ":type arg1: str\n"
                ":param arg2: Parameter value to store\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               );
    pyClass.def("get_double_parameter", &GXIMG_wrap_get_double_parameter,
                "get_double_parameter((str)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Store a real parameter in an IMG object\n\n"

                ":param arg1: Parameter name (case insensitive)\n"
                ":type arg1: str\n"
                ":returns: Parameter value, rDUMMY if not found.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               );

    scope().attr("IMG_FILE_READONLY") = (int32_t)0;
    scope().attr("IMG_FILE_READWRITE") = (int32_t)2;
    scope().attr("IMG_FILE_READORWRITE") = (int32_t)3;
    scope().attr("IMG_QUERY_iWRITE") = (int32_t)0;
    scope().attr("IMG_QUERY_iPG") = (int32_t)1;
    scope().attr("IMG_QUERY_iWRITEPG") = (int32_t)2;
    scope().attr("IMG_QUERY_iIMGTYPE") = (int32_t)3;
    scope().attr("IMG_QUERY_iDATTYPE") = (int32_t)4;
    scope().attr("IMG_QUERY_iRENDER") = (int32_t)5;
    scope().attr("IMG_QUERY_iKX") = (int32_t)6;
    scope().attr("IMG_QUERY_iNX") = (int32_t)7;
    scope().attr("IMG_QUERY_iNY") = (int32_t)8;
    scope().attr("IMG_QUERY_iNV") = (int32_t)9;
    scope().attr("IMG_QUERY_iNE") = (int32_t)10;
    scope().attr("IMG_QUERY_rXO") = (int32_t)11;
    scope().attr("IMG_QUERY_rYO") = (int32_t)12;
    scope().attr("IMG_QUERY_rDX") = (int32_t)13;
    scope().attr("IMG_QUERY_rDY") = (int32_t)14;
    scope().attr("IMG_QUERY_rROT") = (int32_t)15;
    scope().attr("IMG_QUERY_rBASE") = (int32_t)16;
    scope().attr("IMG_QUERY_rMULT") = (int32_t)17;
    scope().attr("IMG_QUERY_rCOMPRESSION_RATIO") = (int32_t)18;
    scope().attr("IMG_RELOCATE_FIT") = (int32_t)0;
    scope().attr("IMG_RELOCATE_ASPECT") = (int32_t)1;

}
