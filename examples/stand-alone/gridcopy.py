#!python3.3
'''
Copy the contents of one grid to another.

This is a sample Python program that illustrates how to connect to the GX
developer environment from a stand-alone program.  In this case, there 
the following basic steps:

   1. Get (create) a GX Object handle.

   2. Create handles to an input and output grid-images.

   3. Copy a grid

Note that Geosoft grid file decorations are supported.  Grid decorations allow one to change the
characteristics and format of the output grid.
'''

import os
import sys
import geosoft.gx as gx
import argparse as argp

def copy_grid(input,output):
    '''
    Creates an exact copy of an input grid. The output copy has
    (exact copy) added to the filename.
    '''

    # get (create) a GX Object handle
    ctx = gx.GXContext.create('Grid Copy', 'Geosoft Inc.')

    # load an existing grid and create new ones
    input_grid = gx.GXIMG.create_file(ctx, gx.GS_TYPE_DEFAULT, input, gx.IMG_FILE_READONLY)
    output_grid = gx.GXIMG.create_out_file(ctx, gx.GS_TYPE_DEFAULT, output, input_grid)

    # copy grid using another function
    input_grid.copy(output_grid)


if __name__ == "__main__":

    # GEOSOFT Environment variable should contain a path with geodist.dll
    print("GX_GEOSOFT_BIN_PATH = {}".format(os.getenv("GX_GEOSOFT_BIN_PATH")))
    print('Working directory = ' + os.path.abspath(os.curdir))

    # get command line parameters
    parser = argp.ArgumentParser(description="Make a copy of a grid.  Decorations in the grid names can be used to reformat grids (see https://www.scribd.com/doc/241419409/dat-xgd)")
    parser.add_argument("sInGrid", help="Input grid file name")
    parser.add_argument("sOutGrid", help="Output grid file name, decorations supported")
    args = parser.parse_args()
    print("gridcopy - no copyright\n")

    # echo parameters
    print("Input grid = "+args.sInGrid)
    print("Output grid = "+args.sOutGrid)

    # script requires input parameters
    if len(sys.argv) < 2:
        raise Exception("script parameters ERROR - an input grid name is required")

    # run an example
    parameter_input_grid_name = sys.argv[1]
    copy_grid(args.sInGrid,args.sOutGrid)

    print("Grid was copied successfully")