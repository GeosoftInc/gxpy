#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXPJ_wrap_clip_ply(GXPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, GXPLYPtr arg6)
{
    self->clip_ply(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXPJ_wrap_convert_vv(GXPJPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->convert_vv(arg1, arg2);
}
inline void GXPJ_wrap_convert_vv3(GXPJPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->convert_vv3(arg1, arg2, arg3);
}
inline void GXPJ_wrap_convert_xy(GXPJPtr self, float_ref& arg1, float_ref& arg2)
{
    self->convert_xy(arg1, arg2);
}
inline void GXPJ_wrap_convert_xy_from_xyz(GXPJPtr self, float_ref& arg1, float_ref& arg2, double arg3)
{
    self->convert_xy_from_xyz(arg1, arg2, arg3);
}
inline void GXPJ_wrap_convert_xyz(GXPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3)
{
    self->convert_xyz(arg1, arg2, arg3);
}
inline GXPJPtr GXPJ_wrap_create(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXPJPtr ret = GXPJ::create(arg1, arg2);
    return ret;
}
inline GXPJPtr GXPJ_wrap_create_ipj(GXIPJPtr arg1, GXIPJPtr arg2)
{
    GXPJPtr ret = GXPJ::create_ipj(arg1, arg2);
    return ret;
}
inline GXPJPtr GXPJ_wrap_create_rectified(double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int32_t arg7)
{
    GXPJPtr ret = GXPJ::create_rectified(arg1, arg2, arg3, arg4, arg5, arg6, (PJ_RECT)arg7);
    return ret;
}
inline int32_t GXPJ_wrap_elevation(GXPJPtr self)
{
    PJ_ELEVATION ret = self->elevation();
    return ret;
}
inline int32_t GXPJ_wrap_is_input_ll(GXPJPtr self)
{
    int32_t ret = self->is_input_ll();
    return ret;
}
inline int32_t GXPJ_wrap_is_output_ll(GXPJPtr self)
{
    int32_t ret = self->is_output_ll();
    return ret;
}
inline void GXPJ_wrap_project_bounding_rectangle(GXPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->project_bounding_rectangle(arg1, arg2, arg3, arg4);
}
inline void GXPJ_wrap_project_bounding_rectangle2(GXPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, double arg5)
{
    self->project_bounding_rectangle2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPJ_wrap_project_bounding_rectangle_res(GXPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    self->project_bounding_rectangle_res(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPJ_wrap_project_bounding_rectangle_res2(GXPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, double arg6)
{
    self->project_bounding_rectangle_res2(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXPJ_wrap_project_limited_bounding_rectangle(GXPJPtr self, double arg1, double arg2, double arg3, double arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8)
{
    self->project_limited_bounding_rectangle(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXPJ_wrap_setup_ldt(GXPJPtr self)
{
    self->setup_ldt();
}

void gxPythonImportGXPJ()
{

    class_<GXPJ, GXPJPtr> pyClass("GXPJ",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The PJ object is created from two IPJ objects,\n"
                                  "   		and is used for converting data in an OASIS database\n"
                                  "   		or map object from one map coordinate (projection)\n"
                                  "   		system to another.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXPJ::null, "null() -> GXPJ\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXPJ`\n\n:returns: A null :class:`geosoft.gxapi.GXPJ`\n:rtype: :class:`geosoft.gxapi.GXPJ`\n").staticmethod("null");
    pyClass.def("is_null", &GXPJ::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXPJ is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXPJ`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXPJ::_internal_handle);
    pyClass.def("clip_ply", &GXPJ_wrap_clip_ply,
                "clip_ply((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (GXPLY)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a clip polygon from a projected area.\n\n"

                ":param arg1: Min X (or Longitude...)\n"
                ":type arg1: float\n"
                ":param arg2: Min Y (or Latitude...)\n"
                ":type arg2: float\n"
                ":param arg3: Max X\n"
                ":type arg3: float\n"
                ":param arg4: Max Y\n"
                ":type arg4: float\n"
                ":param arg5: Max deviation in degrees\n"
                ":type arg5: float\n"
                ":param arg6: PLY to be filled\n"
                ":type arg6: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A rectangular area from (MinX, MinY) to (MaxX, MaxY)\n"
                "   					is projected throught the PJ. The resulting (non-rectangular)\n"
                "   					area is then digitized along its edges, then thinned to\n"
                "   					remove near-collinear points. The thinning is done to any\n"
                "   					point whose neighbors subtend an angle greater than\n"
                "   					(180 degrees - maximum deviation).  (i.e. if max. dev = 0,\n"
                "   					only co-linear points would be removed).\n"
                "   				\n\n"
               );
    pyClass.def("convert_vv", &GXPJ_wrap_convert_vv,
                "convert_vv((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert VVx/VVy from input projection to output projection.\n\n"

                ":param arg1: VVx\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VVy\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function is equivalent to \\ :func:`geosoft.gxapi.GXVV.project`\\ .\n\n"
               );
    pyClass.def("convert_vv3", &GXPJ_wrap_convert_vv3,
                "convert_vv3((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert VVx/VVy/VVz projections\n\n"

                ":param arg1: VVx\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VVy\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VVz\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function is equivalent to \\ :func:`geosoft.gxapi.GXVV.project_3d`\\ .\n\n"
               );
    pyClass.def("convert_xy", &GXPJ_wrap_convert_xy,
                "convert_xy((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert X, Y from input projection to output projection.\n\n"

                ":param arg1: X  (or Longitude)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y  (or Latitude)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("convert_xy_from_xyz", &GXPJ_wrap_convert_xy_from_xyz,
                "convert_xy_from_xyz((float_ref)arg1, (float_ref)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert X, Y from input projection to output projection, taking Z into account\n\n"

                ":param arg1: X  (or Longitude)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y  (or Latitude)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z  (or Depth - unchanged)\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function is used (for instance) when projecting voxel model locations\n"
                "   					where the user expects that the vertical position will not change. The\n"
                "   					regular \\ :func:`geosoft.gxapi.GXPJ.convert_xyz`\\  may result in shifts of hundreds, even a thousand\n"
                "   					meters in case where you are going from the geoid to an ellipsoid.\n"
                "   					The value of Z can have an important effect on the accuracy of the results, as\n"
                "   					the normal \\ :func:`geosoft.gxapi.GXPJ.convert_xy`\\  assumes a value of Z=0 internally and calls\n"
                "   					\\ :func:`geosoft.gxapi.GXPJ.convert_xyz`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("convert_xyz", &GXPJ_wrap_convert_xyz,
                "convert_xyz((float_ref)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert X,Y,Z from input projection to output projection.\n\n"

                ":param arg1: X  (or Longitude)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y  (or Latitude)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z  (or Depth)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("create", &GXPJ_wrap_create,
                "create((str)arg1, (str)arg2) -> GXPJ:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates a projection object.\n\n"

                ":param arg1: Input PRJ file name, \"\" for geodetic\n"
                ":type arg1: str\n"
                ":param arg2: Ouput PRJ file name, \"\" for geodetic\n"
                ":type arg2: str\n"
                ":returns: PJ Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPJ`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_ipj", &GXPJ_wrap_create_ipj,
                "create_ipj((GXIPJ)arg1, (GXIPJ)arg2) -> GXPJ:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates a projection object from IPJs.\n\n"

                ":param arg1: Input Projection, (IPJ)0 for long/lat\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Output Projection, (IPJ)0 for long/lat\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: PJ Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPJ`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If converting to/from long/lat in the natural coordinate\n"
                "   					system of the source/target, only the long/lat system\n"
                "   					can be passed as (IPJ)0.\n"
                "   				\n\n"
               ).staticmethod("create_ipj");
    pyClass.def("create_rectified", &GXPJ_wrap_create_rectified,
                "create_rectified((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (int)arg7) -> GXPJ:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a rectified PJ from lon,lat,rotation\n\n"

                ":param arg1: longitude  at (X,Y) origin\n"
                ":type arg1: float\n"
                ":param arg2: latitude   at (X,Y) origin\n"
                ":type arg2: float\n"
                ":param arg3: (X,Y) origin\n"
                ":type arg3: float\n"
                ":param arg4: \n"
                ":type arg4: float\n"
                ":param arg5: coordinate Y relative to geographic N (deg azm)\n"
                ":type arg5: float\n"
                ":param arg6: scale to convert X,Y to m.\n"
                ":type arg6: float\n"
                ":param arg7: \\ :ref:`PJ_RECT`\\ \n"
                ":type arg7: int\n"
                ":returns: PJ Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPJ`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Given an X,Y coordinate system, the lat/lon origin and\n"
                "   					angle of the coordinate system, this will create a PJ\n"
                "   					to convert between X,Y coordinates and Lon,Lat.\n"
                "   					The Lon/Lat is determined using a Transverse Mercator\n"
                "   					projection with central meridian through the center\n"
                "   					of the coordinates on a WGS 84 datum.\n"
                "   				\n\n"
               ).staticmethod("create_rectified");
    pyClass.def("elevation", &GXPJ_wrap_elevation,
                "elevation() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get elevation correction method\n\n"

                ":returns: \\ :ref:`PJ_ELEVATION`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To determine the model in use, refer to the datum_trf column in the\n"
                "   					user\\csv\\datumtrf.csv file.  The datum and geoid model are named in\n"
                "   					the sqare brackets following the transform name as follows:\n"
                "   \n"
                "   					name [datum_model:geoid]\n"
                "   \n"
                "   					The datum_model is the name of the datum transformation model which will\n"
                "   					be in a file with extension .ll2 in the \\etc directory.  The geoid is the\n"
                "   					name of the geoid model which will be in a grid file with extension .grd\n"
                "   					in the \\etc directory.  If the geoid model is missing, this method will\n"
                "   					return PJ_ELEVATION_NONE and elevation coordinates will not be changed.\n"
                "   				\n\n"
               );
    pyClass.def("is_input_ll", &GXPJ_wrap_is_input_ll,
                "is_input_ll() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the input projection a lat/long.\n\n"

                ":returns: 1 - Yes\n"
                "          						0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("is_output_ll", &GXPJ_wrap_is_output_ll,
                "is_output_ll() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the output projection a lat/long.\n\n"

                ":returns: 1 - Yes\n"
                "          						0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("project_bounding_rectangle", &GXPJ_wrap_project_bounding_rectangle,
                "project_bounding_rectangle((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project a bounding rectangle.\n\n"

                ":param arg1: Bounding Region Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Bounding Region Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Bounding Region Max X\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Bounding Region Max Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A rectangular area from (dMinX, dMinY) to (dMaxX, dMaxY)\n"
                "   					is projected throught the PJ. The resulting region area is\n"
                "   					then digitized along its edges and a new bounding rectangle\n"
                "   					is computed.  If there is a lot of curve through the\n"
                "   					projection the resulting bounding region may be slightly\n"
                "   					smaller than the true region.\n"
                "   				\n\n"
               );
    pyClass.def("project_bounding_rectangle2", &GXPJ_wrap_project_bounding_rectangle2,
                "project_bounding_rectangle2((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project a bounding rectangle with error tolerance.\n\n"

                ":param arg1: Bounding Region Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Bounding Region Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Bounding Region Max X\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Bounding Region Max Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: maximum allowable projection error if <= 0.0, will use 0.005% of smallest dimension\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the same as \\ :func:`geosoft.gxapi.GXPJ.project_bounding_rectangle`\\  except that the bounding\n"
                "   					rectangle will be limited to an area within which the projection can be\n"
                "   					performed to an accuracy better than the specified error tolerance.\n"
                "   				\n\n"
               );
    pyClass.def("project_bounding_rectangle_res", &GXPJ_wrap_project_bounding_rectangle_res,
                "project_bounding_rectangle_res((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project a bounding rectangle with resolution.\n\n"

                ":param arg1: Bounding Region Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Bounding Region Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Bounding Region Max X\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Bounding Region Max Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Resolution\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function behaves just like ProjBoundingRectangle_PJ\n"
                "   					except that it also computes an approximate resolution\n"
                "   					at the reprojected coordinate system from a given original\n"
                "   					resolution.\n"
                "   				\n\n"
               );
    pyClass.def("project_bounding_rectangle_res2", &GXPJ_wrap_project_bounding_rectangle_res2,
                "project_bounding_rectangle_res2((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project a bounding rectangle with resolution and error tolerance.\n\n"

                ":param arg1: Bounding Region Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Bounding Region Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Bounding Region Max X\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Bounding Region Max Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Resolution\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: maximum allowable projection error if <= 0.0, will use 0.005% of smallest dimension\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the same as \\ :func:`geosoft.gxapi.GXPJ.project_bounding_rectangle_res`\\  except that the bounding\n"
                "   					rectangle will be limited to an area within which the projection can be\n"
                "   					performed to an accuracy better than the specified error tolerance.\n"
                "   				\n\n"
               );
    pyClass.def("project_limited_bounding_rectangle", &GXPJ_wrap_project_limited_bounding_rectangle,
                "project_limited_bounding_rectangle((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project a bounding rectangle with limits.\n\n"

                ":param arg1: Output limited bounding region Min X\n"
                ":type arg1: float\n"
                ":param arg2: Min Y\n"
                ":type arg2: float\n"
                ":param arg3: Max X\n"
                ":type arg3: float\n"
                ":param arg4: Max Y\n"
                ":type arg4: float\n"
                ":param arg5: Bounding Region Min X\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Min Y\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Max X\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Max Y\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The bounding rectangle will be limited to no larger\n"
                "   					than the area specified in the output projection.  This\n"
                "   					is useful when projecting from limits that are unreasonable\n"
                "   					in the target projection.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXPJ.project_bounding_rectangle`\\ .\n\n"
               );
    pyClass.def("setup_ldt", &GXPJ_wrap_setup_ldt,
                "setup_ldt() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Setup the PJ with LDT check.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					By default, a PJ on the same datum will not apply a LDT,\n"
                "   					is intended for transformations between datums.  However,\n"
                "   					in some instances you might want to convert between LDTs on\n"
                "   					the same datum, such as when you have two sets of coordinates\n"
                "   					that you KNOW came from WGS84 and were placed on this datum\n"
                "   					using differnt LDT's.  If you want to combine such coordinate\n"
                "   					systems, one or the other should be converted to the other's\n"
                "   					LDT.  Note that a more logical way to do this would be to\n"
                "   					convert both sets back to their original WGS84 coordinates\n"
                "   					and combine in WGS84.\n"
                "   				\n\n"
               );

    scope().attr("PJ_ELEVATION_NONE") = (int32_t)0;
    scope().attr("PJ_ELEVATION_GEOCENTRIC") = (int32_t)1;
    scope().attr("PJ_ELEVATION_GEOID") = (int32_t)2;
    scope().attr("PJ_RECT_XY2LL") = (int32_t)0;
    scope().attr("PJ_RECT_LL2XY") = (int32_t)1;

}
