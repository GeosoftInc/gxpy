import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid
import geosoft.gxpy.project as gxproj


# function to calculate grid statistics
def grid_stats(grid_file):

    # create a gxapi.GXST instance to accumulate statistics
    stats = gxapi.GXST.create()

    # open the grid and add each grid row to the stats instance
    with gxgrid.Grid.open(grid_file) as grid:
        for row in range(grid.ny):
            stats.data_vv(grid.read_row(row).gxvv)

    return stats


# entry point when run from a Geosoft Desktop application
def rungx():

    # get the name of a grid from the user
    grid_file = gxproj.get_user_input(title='Grid statistics',
                                      prompt='Grid file',
                                      kind='file',
                                      filemask='*.grd')

    stats = grid_stats(grid_file)

    gxproj.user_message(grid_file,
                        'min: {}\nmax: {}\nmean: {}\nstd_dev: {}'.format(stats.get_info(gxapi.ST_MIN),
                                                                         stats.get_info(gxapi.ST_MAX),
                                                                         stats.get_info(gxapi.ST_MEAN),
                                                                         stats.get_info(gxapi.ST_STDDEV)))


# running as stand-alone program
if __name__ == "__main__":

    # create context
    gxc = gx.GXpy()

    stats = grid_stats(input('grid file? '))

    # print statistical properties
    print('minimum: ', stats.get_info(gxapi.ST_MIN))
    print('maximum: ', stats.get_info(gxapi.ST_MAX))
    print('mean: ', stats.get_info(gxapi.ST_MEAN))
    print('standard deviation:', stats.get_info(gxapi.ST_STDDEV))



