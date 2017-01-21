import sys 

from gxgenutils import generate_code

if __name__ == '__main__':
	if len(sys.argv)!=5:
		sys.stderr.write('incorrect params, usage:\n\n\tgxgen pickled_collection_file namespace build_version output_dir\n\n')
		sys.exit(1)

	generate_code(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])