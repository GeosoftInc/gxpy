#!python3.3
'''
Apply a 3x3 (9-point) filter to a grid using any number of passes

This is a sample Python program that illustrates how to connect to 
the GX developer environment from a stand-alone program.  In this 
case, it demonstrates the following basic steps:

   1. Get (create) a GX Object handle.

   2. Create handles to input and output grid-images.

   3. Select filter if a predefined one was indicated

   4. Apply a filter using gx.GXIMU class
   
This example accepts command line parameters or will prompt for 
appropriate input if called without parameters. 

It demonstrates 
several types of user input, Dictionaries, Lists, file input 
and List comprehesions.
'''
import os
import sys
import geosoft.gx as gx
import numpy as np
import argparse as argp


# The predefined_filter_array Dictionary includes a List of 2 items for each key: 
# a filter array, and a constant indicating whether it is a horizontal derivative filter
predefined_filter_array = {
    'HANNING': (np.array([0.06, 0.10, 0.06, 0.10, 0.36, 0.10, 0.06, 0.10, 0.06]), gx.IMU_FILT_HZDRV_NO),
    'LAPLACE': (np.array([0.00, -0.25, 0.00, -0.25, 1.00, -0.25, 0.00, -0.25, 0.00]), gx.IMU_FILT_HZDRV_NO),
    'HDX': (np.array([0.00, 0.00, 0.00, -1.00, 0.00, 1.00, 0.00, 0.00, 0.00]), gx.IMU_FILT_HZDRV_X),
    'HDY': (np.array([0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00, -1.00, 0.00]), gx.IMU_FILT_HZDRV_Y),
    'H45': (np.array([0.00, -1.00, 0.00, 1.00, 0.00, -1.00, 0.00, 1.00, 0.00]), gx.IMU_FILT_HZDRV_NO)
}

def grid_filter(input_grid_name, output_grid_name, filter_name_or_file,
               number_of_passes, multiplier, write_dummies_or_interpolate):
    ''' One step filtering of a grid.
    
        USAGE:  input grid name
                output grid name
                filter name or file 
                    ie.  hanning, laplace, HDX, HDY, H45 or a filename
                number of passes
                multiplier to apply to grid values
                filter dummies or interpolate? 
                    ie. gx.IMU_FILT_DUMMY_NO or gx.IMU_FILT_DUMMY_YES    

         This function has 3 steps
            1. Initialize the grids & filter vv
            2. Determine if predefined filter or filter file is being used by 
               examining the filter_name_or_file parameter, and populate the
               filter control variables as appropriate. A try-except structure is
               used to handle the 2 cases.
            3. Apply the filter.
    '''
    # Get (create) a GX Object handle.
    ctx = gx.GXContext.create('Grid Filter', 'Geosoft Inc.')

    # Load an existing grid and create a new one.
    print('in:  ', input_grid_name)
    input_grid = gx.GXIMG.create_file(ctx, gx.GS_TYPE_DEFAULT, 
                                      input_grid_name, gx.IMG_FILE_READONLY)    
    print('out: ', output_grid_name, '\n')
    output_grid = gx.GXIMG.create_out_file(ctx, gx.GS_TYPE_DEFAULT, 
                                           output_grid_name, input_grid)

    # Create a VV to hold the filter values.
    filter_vv = gx.GXVV.create(ctx, gx.GS_REAL, 9)
   
    print('applying filter: ', end='')
    # Get a predefined filter if one exists and initialize VV with filter values.
    try:
        # The dict contains a list of 2 values, so we can 
        # retrieve 2 values on the lookup.
        filter_array, horizontal_derivative = predefined_filter_array[filter_name_or_file]
        filter_vv.set_data_np(0, filter_array)
        use_filter_file_or_not = gx.IMU_FILT_FILE_NO

        for i in range(filter_vv.length()):
            print(str(filter_vv.get_double(i)), end='  ')
        print()
    except KeyError:
        # The name provided didn't match a predefined filter, 
        # so we'll test if its a valid file and raise an exception
        # if it isn't.
        if not os.path.isfile(filter_name_or_file):
            raise OSError('Filter file ' + str.upper(filter_name_or_file) + ' not found') 
        use_filter_file_or_not = gx.IMU_FILT_FILE_YES
        horizontal_derivative = gx.IMU_FILT_HZDRV_NO
        
        # Print out filter elements on a single line
        with open(filter_name_or_file, 'r') as filterfile:
            for line in filterfile:
                # The strip() function will remove the linefeed from line 
                # and the "end=' '" statement is necessary not to prevent
                # print adding them back in
                print(line.strip(), end=' ')
        
    # Apply the filter.
    # NOTE: a licensed Geosoft environment is required to run this function.
    gx.GXIMU.grid_filt(ctx, input_grid, output_grid,
                       number_of_passes, multiplier,
                       write_dummies_or_interpolate, 
                       horizontal_derivative, use_filter_file_or_not, 
                       filter_name_or_file, filter_vv)

def select_file_by_extension(folder_path,ext):
    '''
    Prompt the user with a list of files filtered by file extension, 
    with option to enter name or index.
    
    USAGE:  folder_path - use '.' for current folder
            file extension - include the leading '.'
    
    This method  demonstrates several techniques:
        os.listdir() returns  LIST of files in the current directory
        SLICING - file[-4:] means return the last 4 elements in file
        FILTERED LIST COMPREHENSION creates a new list by iterating 
            over some items  and including those items that pass a test.
    
    So overall we are creating  a list of all files in the directory, testing
    each to see if it ends in the upper or lowercase version of the extension,
    and including those filenames in a new list. 
    
    Then we prompt the user to pick one.
    '''
    
    file_list = [file for file in os.listdir(folder_path) if str.lower(file[-4:])==ext]

    i = 0
    for file in file_list:
        print(i, file)
        i += 1
    value = input('Enter the index or filename .. ')
    try:
        # The user will almost certainly pick by index, so we'll try
        # that first.
        return file_list[int(value)] 
    except:
        return value
    
def get_input_grid():
    '''Prompt the user for an input grid, with option to show listing.'''
    input_grid_name = input(
                "Enter the input filename... (? for file listing) .. ")
    if input_grid_name =='?':
        input_grid_name = select_file_by_extension('.', '.grd')
    return input_grid_name
    
def get_filter():
    '''Prompt the user for a filter identifier or filename.'''
    print('Filtering options are to use one of the following predefined',
          'filters, or to enter a filename...' )
    for filt in predefined_filter_array.keys():
        print(filt, end='   ')
    return str.upper(input('\nEnter the filter name or a filter filename .. '))

def get_output_grid(input_grid_name, filter_name_or_file):
    '''
    Given an input filename and a filter, suggest an appropriate output 
    filename and accept user input.
    '''
    grid_name = os.path.splitext(input_grid_name)[0]
    try:
        predefined_filter_array[filter_name_or_file]
        decoration= filter_name_or_file
    except:
        decoration = os.path.splitext(filter_name_or_file)[0]

    suggestion = grid_name + '_' + decoration
    print('Suggested output filename - '+suggestion)  
    output_grid_name = input('Press Enter to accept, or enter a new name')
    if output_grid_name == '':
        output_grid_name = suggestion
    return output_grid_name
    
if __name__ == "__main__":

    # GEOSOFT Environment variable should contain a path with geodist.dll
    print("GX_GEOSOFT_BIN_PATH = {}".format(os.getenv("GX_GEOSOFT_BIN_PATH")))
    print('Working directory = ' + os.path.abspath(os.curdir))

    # get command line parameters
    parser = argp.ArgumentParser(description="Filter a grid.")
    parser.add_argument("-i","--input", type=str, default="", help="Name of grid to filter")
    parser.add_argument("-f","--filter", type=str, default="", help="Filter: file name or one of HANNING, LAPLACE, HDX, HDY or H45")
    parser.add_argument("-o","--output", type=str, default="", help="Output filtered grid")
    parser.add_argument("-p","--passes", type=int, default="1", help="Number of passes")
    args = parser.parse_args()
    print("gridfilter - no copyright\n")

    #interactive inputs
    if len(args.input) == 0:
        args.input = get_input_grid()
    if len(args.filter) == 0:
        args.filter = get_filter()
    if len(args.output) == 0:
        args.output = get_output_grid(args.input, args.filter)

    # echo parameters
    print("Input = " + args.input)
    print("Output = " + args.output)
    print("Filter = " + args.filter)
    print("Passes = {}".format(args.passes))


    multiplier = 1.0
    write_dummies_or_interpolate = gx.IMU_FILT_DUMMY_NO

    grid_filter(args.input,args.output,args.filter,args.passes,multiplier,write_dummies_or_interpolate)