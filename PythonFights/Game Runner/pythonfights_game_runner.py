import os
import time
run_properties_file = open("run.properties", "r")
exec(run_properties_file.read())
run_properties_file.close()
time_delay_each_frame = time_delay_each_frame
shell_keyword_to_clear = shell_keyword_to_clear
while True:
	input_data = input("Enter filename: ")
	if(os.path.exists(input_data)):
		break
	else:
		print("Invalid Path")
gonna_be_run_file = open(input_data, "r")
run_data = gonna_be_run_file.read()
gonna_be_run_file.close()
run_data_list = run_data.splitlines()
current_line = 0
while True:
	current_frame_list = []
	while True:
		if(run_data_list[current_line] == "-"):
			break
		else:
			current_frame_list.append(run_data_list[current_line])
			current_line += 1
	if(outline):
		print(" ", end="")
		for x in range(0, len(current_frame_list[0])):
			print("~", end="")
		print("")
		for x in range(0, len(current_frame_list)):
			print("|", end="")
			print(current_frame_list[x], end="")
			print("|")
		print(" ", end="")
		for x in range(0, len(current_frame_list[0])):
			print("~", end="")
		print("")
	else:
		for x in range(0, len(current_frame_list)):
			print(current_frame_list[x])
	time.sleep(time_delay_each_frame)
	os.system(shell_keyword_to_clear)
	current_line += 1
	del current_frame_list