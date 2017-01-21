import sys 

from gxgenutils import gxapi_api_collection_pickle

if __name__ == '__main__':
	if len(sys.argv)!=3:
		sys.stderr.write('incorrect params, usage:\n\n\pickle_gxapi_collection inputdirs outfile\n\n')
		sys.exit(1)

	gxapi_api_collection_pickle(sys.argv[1], sys.argv[2])