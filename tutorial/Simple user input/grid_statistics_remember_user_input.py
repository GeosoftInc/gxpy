import os
import geosoft.gxapi as gxapi
import geosoft.gxpy.grid as gxgrid
import geosoft.gxpy.project as gxproj
import geosoft.gxpy.utility as gxu


# function to calculate grid statistics
def grid_stats(grid_file):

    # create a gxapi.GXST instance to accumulate statistics
    stats = gxapi.GXST.create()

    # open the grid
    grid = gxgrid.Grid.open(grid_file)

    # add data from each row to the stats instance
    for row in range(grid.ny):
        stats.data_vv(grid.read_row(row).gxvv)

    return stats


# entry point when run from a Geosoft Desktop application
def rungx():

    # parameter 'GRID_FILE' is the last-specified grid file name for this script.
    grid_parameter = 'GRID_FILE'
    group = os.path.basename(__file__).split('.')[0]
    parms = gxu.get_parameters(group, {grid_parameter: ''})

    # get the name of a grid from the user
    grid_file = gxproj.get_user_input(title='Grid statistics',
                                      prompt='Grid file',
                                      default=parms.get(grid_parameter),
                                      kind='file',
                                      filemask='*.grd')

    # save the grid file name as the default the next time this script is run
    parms[grid_parameter] = grid_file
    gxu.save_parameters(group, parms)

    stats = grid_stats(grid_file)

    gxproj.user_message(grid_file,
                        'min: {}\nmax: {}\nmean: {}\nstd_dev: {}'.format(stats.get_info(gxapi.ST_MIN),
                                                                         stats.get_info(gxapi.ST_MAX),
                                                                         stats.get_info(gxapi.ST_MEAN),
                                                                         stats.get_info(gxapi.ST_STDDEV)))


