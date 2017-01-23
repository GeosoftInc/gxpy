import sys
import os
import shutil
import re

regex_for_class_definition = re.compile("\s*class\s+GX[a-zA-Z0-9]+\s*$")
regex_for_classorenum_definition_end = re.compile("\s*};\s*$")
regex_for_namespace_end_line = re.compile("^}\s*$")
regex_for_open_brace_line = re.compile("\s*{\s*$")
regex_for_close_brace_line = re.compile("\s*}\s*$")
regex_for_enum_definition = re.compile("\s*enum\s+[a-zA-Z0-9\_]+\s*$")
enum_dict = {}

def find_first_match(lines, starting_index, go_in_reverse, regex_to_find, regex_to_stop_at):
	i = 0
	if go_in_reverse:
		i = len(lines) - 1
	while True:
		if go_in_reverse:
			skip_line = i > starting_index
		else:
			skip_line = i < starting_index
		if not skip_line:
			if regex_to_find.match(lines[i]):
				return i;
			elif regex_to_stop_at.match(lines[i]):
				return -1
		if go_in_reverse:
			i = i - 1
			if -1 == i:
				break
		else:
			i = i + 1
			if len(lines) == i:
				break
	return -1;

def get_regex_for_class_definition_in_template_file(class_name):
	regex_string_part1 = "\s*public\s+ref\s+class\s+"
	regex_string_part2 = ""
	if not re.compile("^GD$").match(class_name):
		regex_string_part2 = "H?"
	regex_string_part3 = "\s+abstract\s+sealed\s*$"
	regex_string = regex_string_part1 + regex_string_part2 + class_name + regex_string_part3
	regex = re.compile(regex_string)
	return regex

def get_regex_for_function_definition_in_template_file(class_name, function_name):
	regex_string = "\s*static.+" + function_name + "\\_" + class_name + "\(.+"
	regex = re.compile(regex_string, re.IGNORECASE)
	return regex

def get_regex_for_enum_definition_in_template_file(enum_name):
	regex_string_part1 = "\s*public\s+ref\s+class\s+"
	regex_string_part2 = ""
	if not re.compile("^GD$").match(enum_name):
		regex_string_part2 = "H?"
	regex_string_part3 = "Constant\s+abstract\s+sealed\s*$"
	regex_string = regex_string_part1 + regex_string_part2 + enum_name + regex_string_part3
	regex = re.compile(regex_string)
	return regex

def get_summary_doc(input_template_lines, definition_index):
	summary_lines = []
	regex_for_summary_start = re.compile(".*///<summary>.*")
	summary_start_index = find_first_match(input_template_lines, definition_index, True, regex_for_summary_start, regex_for_classorenum_definition_end)
	if -1 != summary_start_index:
		regex_for_summary_end = re.compile(".*</summary>\s*$")
		summary_end_index = find_first_match(input_template_lines, definition_index, True, regex_for_summary_end, regex_for_classorenum_definition_end)
		if -1 != summary_end_index:
			summ_lines = []
			if summary_start_index == summary_end_index:
				summary_line = input_template_lines[summary_start_index].split("<summary>")[1].split("</summary>")[0]
				summ_lines.append(summary_line)
			else:
				for i in range(summary_start_index + 1, summary_end_index):
					summary_line = input_template_lines[i].split("///")[1]
					summ_lines.append(summary_line)
			for summary_line in summ_lines:
				if re.compile(".+<see cref=\".+$").match(summary_line):
					summary_line_with_link = summary_line.split("<see cref=\"")[0] + summary_line.split("<see cref=\"")[-1].split("Constant\"/>")[0]
					if len(summary_line.split("<see cref=\"")[-1].split("Constant\"/>")) > 0:
						summary_line_with_link = summary_line_with_link + summary_line.split("<see cref=\"")[-1].split("Constant\"/>")[1]
					summary_line = summary_line_with_link
				summary_lines.append(summary_line)
	return summary_lines

def get_param_doc(input_template_lines, definition_index):
	param_lines = []
	regex_for_param = re.compile(".*<param name=\".*")
	start_index = definition_index
	is_object_handle_first_param = not re.compile(".+\_(SYS|STR)\(.+").match(input_template_lines[definition_index])
	params = input_template_lines[definition_index].split("(")[1].split(")")[0].split(",")
	num_params = len(params)
	has_ref_str = False
	for i in range(0, len(params)):
		if re.compile("\s*string\^ \%.+").match(params[i]) and i < len(params) - 1 and re.compile("\s*int.+").match(params[i + 1]):
			num_params = num_params - 1
			has_ref_str = True
	param_count = num_params
	if is_object_handle_first_param:
		param_count = param_count - 1
	param_index = find_first_match(input_template_lines, start_index, True, regex_for_param, regex_for_close_brace_line)
	while -1 != param_index:
		is_param_buffer_size = has_ref_str and ((re.compile(".*<param name=\"str.+").match(input_template_lines[param_index - 1]) and (re.compile(".*<param name=\"i.+size.+", re.IGNORECASE).match(input_template_lines[param_index]) or re.compile(".*<param name=\"i.+length.+", re.IGNORECASE).match(input_template_lines[param_index]))) or re.compile(".*<param name=\"i.+of buffer.+", re.IGNORECASE).match(input_template_lines[param_index]) or re.compile(".*<param name=\"i.+size of result.+", re.IGNORECASE).match(input_template_lines[param_index]) or re.compile(".*<param name=\"i.+STR_TRIMConstant.+", re.IGNORECASE).match(input_template_lines[param_index]))
		if not is_param_buffer_size:
			if re.compile(".+</param>\s*$").match(input_template_lines[param_index]):
				param_line = "@param param" + str(param_count) + " " + input_template_lines[param_index].split("\">")[1].split("</param>")[0]
				if re.compile(".+<see cref=\".+$").match(param_line):
					param_line_with_link = param_line.split("<see cref=\"")[0] + param_line.split("<see cref=\"")[-1].split("Constant\"/>")[0]
					if len(param_line.split("<see cref=\"")[-1].split("Constant\"/>")) > 0:
						param_line_with_link = param_line_with_link + param_line.split("<see cref=\"")[-1].split("Constant\"/>")[1]
					param_line = ""
					for param_part in param_line_with_link.split():
						if param_part in enum_dict:
							enum_values = "["
							for enum_value in enum_dict[param_part]:
								enum_values = enum_values + enum_value + ", "
							enum_values = enum_values.strip()[:-1]
							enum_values = enum_values + "]"
							param_part = enum_values
						param_line = param_line + " " + param_part
						param_line = param_line.replace(" See ", " ").replace(" see ", " ").strip()
			else:
				param_line = "@param param" + str(param_count)
			param_count = param_count - 1
			param_lines.append(param_line)
		start_index = param_index - 1
		param_index = find_first_match(input_template_lines, start_index, True, regex_for_param, regex_for_close_brace_line)
	if len(param_lines) > 0:
		num_params_check = num_params
		if is_object_handle_first_param:
			param_lines.pop()
			num_params_check = num_params_check - 1
		param_lines.reverse()
		if len(param_lines) != num_params_check:
			param_lines = []
	return param_lines

def get_class_doc(input_template_lines, class_name):
	doc_lines = []
	regex_for_class_definition_in_template_file = get_regex_for_class_definition_in_template_file(class_name)
	class_definition_index = find_first_match(input_template_lines, 0, False, regex_for_class_definition_in_template_file, regex_for_namespace_end_line)
	if (-1 != class_definition_index):
		doc_lines = get_summary_doc(input_template_lines, class_definition_index)
	return doc_lines

def get_function_doc(input_template_lines, class_name, function_name):
	doc_lines = []
	regex_for_class_definition_in_template_file = get_regex_for_class_definition_in_template_file(class_name)
	regex_for_function_definition_in_template_file = get_regex_for_function_definition_in_template_file(class_name, function_name)
	class_definition_index = find_first_match(input_template_lines, 0, False, regex_for_class_definition_in_template_file, regex_for_namespace_end_line)
	if (-1 != class_definition_index):
		function_definition_index = find_first_match(input_template_lines, class_definition_index, False, regex_for_function_definition_in_template_file, regex_for_classorenum_definition_end)
		if (-1 != function_definition_index):
			summary_doc_lines = get_summary_doc(input_template_lines, function_definition_index)
			param_doc_lines = get_param_doc(input_template_lines, function_definition_index)
			for line in summary_doc_lines:
				doc_lines.append(line)
			for line in param_doc_lines:
				doc_lines.append(line)
	return doc_lines

def decorate_function_doc(function_doc_lines, function_definition):
	decorated_function_doc_lines = function_doc_lines
	definition_params = []
	if re.compile(".+\(.+\).*").match(function_definition):
		definition_params = function_definition.split("(")[1].split(")")[0].split(",")
	doc_params = []
	for doc_line in function_doc_lines:
		if re.compile("^\@param\s+.+").match(doc_line):
			doc_params.append(doc_line)
	if len(definition_params) > 0 or len(doc_params) > 0:
		if len(definition_params) == len(doc_params):
			decorated_function_doc_lines = []
			for doc_line in function_doc_lines:
				altered_doc_line = doc_line
				if re.compile("^\@param\s+.+").match(doc_line):
					rest = doc_line.split("@param")[1]
					param_name = rest.split()[0].strip()
					for definition_param in definition_params:
						regex_string_for_param_check = ".+\s+" + param_name + "\s*$"
						if re.compile(regex_string_for_param_check).match(definition_param):
							regex_string_for_param_ref_check = ".+\&\s+" + param_name + "\s*$"
							if re.compile(regex_string_for_param_ref_check).match(definition_param):
								altered_doc_line = "@param[out]" + rest
							else:
								altered_doc_line = "@param[in]" + rest
							break
				decorated_function_doc_lines.append(altered_doc_line)
	return decorated_function_doc_lines

def convert_input_functionname_format_to_template_functionname_format(input_function_name):
	converted_function_name = input_function_name
	if re.compile(".+\_$").match(converted_function_name):
		converted_function_name = converted_function_name[:-1]
	if not re.compile("^(get|set|read)\_(int|double)$").match(converted_function_name):
		if re.compile("^(get|set|read|write|query|exist|abs|mod|round)\_.*(int|double)\_?$").match(converted_function_name):
			if re.compile(".+\_int$").match(converted_function_name):
				converted_function_name = converted_function_name[:-4]
			elif re.compile(".+\_double$").match(converted_function_name):
				converted_function_name = converted_function_name[:-7]
	converted_function_name = converted_function_name.replace("double", "real")
	if re.compile("^bool\_mask$").match(converted_function_name):
		converted_function_name = converted_function_name[:-5]
	elif re.compile("^export\_file$").match(converted_function_name):
		converted_function_name = converted_function_name[:-5]
	elif re.compile("^export1$").match(converted_function_name):
		converted_function_name = converted_function_name[:-1]
	elif re.compile("^delete\_stk$").match(converted_function_name):
		converted_function_name = converted_function_name[:-4]
	converted_function_name = converted_function_name.replace("__", "++")
	converted_function_name = converted_function_name.replace("_", "")
	converted_function_name = converted_function_name.replace("++", "_")
	if re.compile(".+safe$").match(converted_function_name):
		converted_function_name = converted_function_name[:-4]
	return converted_function_name

def get_enum_doc(input_template_lines, enum_name):
	doc_lines = []
	regex_for_enum_definition_in_template_file = get_regex_for_enum_definition_in_template_file(enum_name)
	enum_definition_index = find_first_match(input_template_lines, 0, False, regex_for_enum_definition_in_template_file, regex_for_namespace_end_line)
	if (-1 != enum_definition_index):
		doc_lines = get_summary_doc(input_template_lines, enum_definition_index)
	return doc_lines

def generate(doxygen_exe, working_dir, input_file, input_template_file, root_output_dir):

	input_dir, input_filename = os.path.split(input_file)
	working_input_file = os.path.join(working_dir, input_filename)
	output_dir = os.path.join(root_output_dir, os.path.splitext(input_filename)[0])

	if os.path.exists(output_dir):
		shutil.rmtree(output_dir)
	os.makedirs(output_dir)

	input_lines = open(input_file, "r").read().splitlines()
	input_template_lines = open(input_template_file, "r").read().splitlines()

	sw = open(working_input_file, "w")
	inside_class = False
	inside_enum = False
	classes_count = 0
	for i in range(0, len(input_lines)):
		if regex_for_class_definition.match(input_lines[i]):
			inside_class = True
			class_name = input_lines[i].split("GX")[1]
			class_doc_lines = get_class_doc(input_template_lines, class_name)
			if len(class_doc_lines) > 0:
				print("Generating C++ GX API Documentation for class " + class_name)
				sw.write("            /**\n")
				for doc_line in class_doc_lines:
					sw.write("             * " + doc_line + "\n")
				sw.write("             */\n")
		elif inside_class and regex_for_open_brace_line.match(input_lines[i]):
			if not regex_for_class_definition.match(input_lines[i - 1]) and not re.compile("\s*~.+").match(input_lines[i - 1]) and not re.compile("\s*\:.+").match(input_lines[i - 1]):
				parts = input_lines[i - 1].split("(")[0].split(" ");
				function_name = parts[len(parts) - 1]
				if not re.compile("^is_null$").match(function_name) and not re.compile("^null$").match(function_name):
					converted_function_name = convert_input_functionname_format_to_template_functionname_format(function_name)
					function_doc_lines = get_function_doc(input_template_lines, class_name, converted_function_name)
					if 0 == len(function_doc_lines):
						if re.compile("^(get|set).+").match(converted_function_name):
							converted_function_name = converted_function_name[3:]
							function_doc_lines = get_function_doc(input_template_lines, class_name, converted_function_name)
						if 0 == len(function_doc_lines):
							converted_function_name = converted_function_name.replace("real", "double")
							function_doc_lines = get_function_doc(input_template_lines, class_name, converted_function_name)
					if len(function_doc_lines) > 0:
						#function_doc_lines = decorate_function_doc(function_doc_lines, input_lines[i - 1])
						sw.write("               /** \\brief\n")
						for doc_line in function_doc_lines:
							sw.write("                * " + doc_line + "\n")
						sw.write("                */\n")
			sw.write(input_lines[i - 1] + "\n")
		elif regex_for_classorenum_definition_end.match(input_lines[i]):
			if inside_class:
				inside_class = False
				classes_count = classes_count + 1
			elif inside_enum:
				inside_enum = False
		elif regex_for_enum_definition.match(input_lines[i]):
			inside_enum = True;
			enum_name = input_lines[i].split()[-1]
			enum_dict[enum_name] = []
			enum_doc_lines = get_enum_doc(input_template_lines, enum_name)
			sw.write("            /**\n")
			for doc_line in enum_doc_lines:
				sw.write("             * " + doc_line + "\n")
			sw.write("             */\n")
		elif inside_enum:
			if not re.compile(".*({|}).*").match(input_lines[i]):
				enum_value = input_lines[i].replace(",", "").strip()
				enum_dict[enum_name].append(enum_value)
		if i == len(input_lines) - 1 or not (inside_class and regex_for_open_brace_line.match(input_lines[i + 1])):
			sw.write(input_lines[i] + "\n")
	sw.close()

	doxygen_generated_dir = os.path.join(working_dir, "html")
	if os.path.exists(doxygen_generated_dir):
		shutil.rmtree(doxygen_generated_dir)
	old_current_dir = os.getcwd()
	os.chdir(working_dir)
	doxygen_config_file = os.path.join(working_dir, os.path.splitext(input_filename)[0] + ".conf")
	if os.path.exists(doxygen_config_file):
		os.system(doxygen_exe + " " + doxygen_config_file)
	os.chdir(old_current_dir)

	if os.path.exists(doxygen_generated_dir):
		shutil.move(doxygen_generated_dir, output_dir)

	print("\nCompleted generating C++ GX API documentation. It can be found at " + output_dir)

if __name__ == "__main__":

	if 6 == len(sys.argv) and os.path.exists(sys.argv[1]) and sys.argv[1].lower().endswith("doxygen.exe") and os.path.exists(sys.argv[2]) and os.path.isdir(sys.argv[2]) and os.path.exists(sys.argv[3]) and sys.argv[3].lower().endswith(".h") and os.path.exists(sys.argv[4]) and sys.argv[4].lower().endswith(".h") and os.path.isabs(sys.argv[5]):
		generate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	else:
		raise Exception("gxgencppodoc.py: Invalid arguments")