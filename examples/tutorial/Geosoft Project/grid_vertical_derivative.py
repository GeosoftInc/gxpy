import geosoft.gxpy.project as gxpj
import geosoft.gxpy.grid as gxgrd
import geosoft.gxapi as gxapi

def rungx():

    project = gxpj.Geosoft_project()

    # there must be grids in the project
    if len(project.project_grids) == 0:
        raise Exception('This project contains no grids.')

    # default grid will be the current grid, or the first grid in the list of project grids
    if project.current_grid:
        default_grid = project.current_grid
    else:
        default_grid = project.project_grids[0]

    # ask the user to select a grid
    grid_name = gxpj.get_user_input(title='Vertical derivative of a grid',
                                    prompt='Grid to process',
                                    kind='list',
                                    items=project.project_grids,
                                    default=default_grid)

    # ask for a new grid file name
    new_grid = gxpj.get_user_input(title='Vertical derivative of a grid',
                                   prompt='Output vertical derivative grid name',
                                   kind='file',
                                   filemask='*.grd')

    # calculate vertical derivative
    with gxgrd.Grid(grid_name) as g_input:
        with gxgrd.Grid.new(new_grid, properties=g_input.properties(), overwrite=True) as g_output:
            gxapi.GXIMU.grid_vd(g_input.gximg, g_output.gximg)

    # open the vertical derivative grid
    gxpj.add_document(new_grid)
