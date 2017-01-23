import sys 

from gxgenutils import gxapi_pickle

if __name__ == '__main__':
	if len(sys.argv)!=3:
		sys.stderr.write('incorrect params, usage:\n\n\tpickle_gxapi infile outfile\n\n')
		sys.exit(1)

	gxapi_pickle(sys.argv[1], sys.argv[2])