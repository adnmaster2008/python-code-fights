import os
import multiprocessing
import time

# Get Game Properties____________________________________
system_game_properties_file = open("game.properties", "r")
exec(system_game_properties_file.read())
system_game_properties_file.close()
system_frame_limit = system_frame_limit
system_pythonfights_space_x = system_pythonfights_space_x
system_pythonfights_space_y = system_pythonfights_space_y
system_player1_position = system_player1_position
system_player2_position = system_player2_position
system_player_build_delay = system_player_build_delay
system_player_bullet_delay = system_player_bullet_delay
# Get Game Properties____________________________________


# Create GameSpace___________________________________
system_pythonfights_space = []
system_pythonfights_space_x_backup = system_pythonfights_space_x
system_pythonfights_space_y_backup = system_pythonfights_space_y
while True:
	if(system_pythonfights_space_y_backup == 0):
		break
	else:
		system_pythonfights_space.append([])
		system_pythonfights_space_y_backup -= 1
del system_pythonfights_space_y_backup
for x in range(0, len(system_pythonfights_space)):
	while True:
		if(system_pythonfights_space_x_backup == 0):
			break
		else:
			system_pythonfights_space[x].append(" ")
			system_pythonfights_space_x_backup -= 1
	system_pythonfights_space_x_backup = system_pythonfights_space_x
del system_pythonfights_space_x_backup
# Create GameSpace____________________________________

print("Creating game...")

system_frame = 0
# Create Game____________________________________________________________________
if(system_player1_is_alive):
	system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = "#"
if(system_player2_is_alive):
	system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = "#"
if(system_player3_is_alive):
	system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = "#"
if(system_player4_is_alive):
	system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = "#"
system_player1_bullet_delay = system_player_bullet_delay
system_player2_bullet_delay = system_player_bullet_delay
system_player3_bullet_delay = system_player_bullet_delay
system_player4_bullet_delay = system_player_bullet_delay
system_player1_build_delay = system_player_build_delay
system_player2_build_delay = system_player_build_delay
system_player3_build_delay = system_player_build_delay
system_player4_build_delay = system_player_build_delay
system_bullet_data = []
system_player1_data = []
system_player2_data = []
system_player3_data = []
system_player4_data = []
while True:
	system_player1_output = ""
	system_player2_output = ""
	system_player3_output = ""
	system_player4_output = ""
	system_player1_action = ""
	system_player2_action = ""
	system_player3_action = ""
	system_player4_action = ""

	# Player 1 Turn
	if(not system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] == "#"):
		system_player1_is_alive = False
	if(system_player1_is_alive):
		system_player1_turn_file = open("player1_code.py")
		exec(system_player1_turn_file.read())
		system_player1_turn_file.close()
		system_tmp_data_list = [system_pythonfights_space.copy(), system_player1_position[0], system_player1_position[1], system_player1_build_delay, system_player1_bullet_delay]
		system_tmp_data = player1_code(system_player1_data, system_tmp_data_list)
		system_player1_output = system_tmp_data[0]
		system_player1_data = system_tmp_data[1]
		del system_tmp_data_list
		del system_tmp_data
		del player1_code
	# Player 1 Turn

	# Player 2 Turn
	if(not system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] == "#"):
		system_player2_is_alive = False
	if(system_player2_is_alive):
		system_player2_turn_file = open("player2_code.py")
		exec(system_player2_turn_file.read())
		system_player2_turn_file.close()
		system_tmp_data_list = [system_pythonfights_space.copy(), system_player2_position[0], system_player2_position[1], system_player2_build_delay, system_player2_bullet_delay]
		system_tmp_data = player2_code(system_player2_data, system_tmp_data_list)
		system_player2_output = system_tmp_data[0]
		system_player2_data = system_tmp_data[1]
		del system_tmp_data_list
		del system_tmp_data
		del player2_code
	# Player 2 Turn

	# Player 3 Turn
	if(not system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] == "#"):
		system_player3_is_alive = False
	if(system_player3_is_alive):
		system_player3_turn_file = open("player3_code.py")
		exec(system_player3_turn_file.read())
		system_player3_turn_file.close()
		system_tmp_data_list = [system_pythonfights_space.copy(), system_player3_position[0], system_player3_position[1], system_player3_build_delay, system_player3_bullet_delay]
		system_tmp_data = player3_code(system_player3_data, system_tmp_data_list)
		system_player3_output = system_tmp_data[0]
		system_player3_data = system_tmp_data[1]
		del system_tmp_data_list
		del system_tmp_data
		del player3_code
	# Player 3 Turn

	# Player 4 Turn
	if(not system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] == "#"):
		system_player4_is_alive = False
	if(system_player4_is_alive):
		system_player4_turn_file = open("player4_code.py")
		exec(system_player4_turn_file.read())
		system_player4_turn_file.close()
		system_tmp_data_list = [system_pythonfights_space.copy(), system_player4_position[0], system_player4_position[1], system_player4_build_delay, system_player4_bullet_delay]
		system_tmp_data = player4_code(system_player4_data, system_tmp_data_list)
		system_player4_output = system_tmp_data[0]
		system_player4_data = system_tmp_data[1]
		del system_tmp_data_list
		del system_tmp_data
		del player4_code
	# Player 4 Turn

	# Process Current Frame
	if("m" in system_player1_output and system_player1_is_alive):
		system_player1_output = system_player1_output.replace("m", "")
		try:
			if(system_player1_output == ">"):
				if(system_pythonfights_space[system_player1_position[1]][system_player1_position[0]+1] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]+1] = "#"
					system_player1_position[0] += 1
			if(system_player1_output == "<"):
				if(system_pythonfights_space[system_player1_position[1]][system_player1_position[0]-1] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]-1] = "#"
					system_player1_position[0] -= 1
			if(system_player1_output == "+"):
				if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]] = "#"
					system_player1_position[1] -= 1
			if(system_player1_output == "-"):
				if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]] = "#"
					system_player1_position[1] += 1
			if(system_player1_output == ">+"):
				if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]+1] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]+1] = "#"
					system_player1_position[0] += 1
					system_player1_position[1] -= 1
			if(system_player1_output == ">-"):
				if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]+1] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]+1] = "#"
					system_player1_position[0] += 1
					system_player1_position[1] += 1
			if(system_player1_output == "<+"):
				if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]-1] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]-1] = "#"
					system_player1_position[0] -= 1
					system_player1_position[1] -= 1
			if(system_player1_output == "<-"):
				if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]-1] == " "):
					system_pythonfights_space[system_player1_position[1]][system_player1_position[0]] = " "
					system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]-1] = "#"
					system_player1_position[0] -= 1
					system_player1_position[1] += 1
		except:
			pass

	if("m" in system_player2_output and system_player2_is_alive):
		system_player2_output = system_player2_output.replace("m", "")
		try:
			if(system_player2_output == ">"):
				if(system_pythonfights_space[system_player2_position[1]][system_player2_position[0]+1] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]+1] = "#"
					system_player2_position[0] += 1
			if(system_player2_output == "<"):
				if(system_pythonfights_space[system_player2_position[1]][system_player2_position[0]-1] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]-1] = "#"
					system_player2_position[0] -= 1
			if(system_player2_output == "+"):
				if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]] = "#"
					system_player2_position[1] -= 1
			if(system_player2_output == "-"):
				if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]] = "#"
					system_player2_position[1] += 1
			if(system_player2_output == ">+"):
				if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]+1] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]+1] = "#"
					system_player2_position[0] += 1
					system_player2_position[1] -= 1
			if(system_player2_output == ">-"):
				if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]+1] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]+1] = "#"
					system_player2_position[0] += 1
					system_player2_position[1] += 1
			if(system_player2_output == "<+"):
				if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]-1] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]-1] = "#"
					system_player2_position[0] -= 1
					system_player2_position[1] -= 1
			if(system_player2_output == "<-"):
				if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]-1] == " "):
					system_pythonfights_space[system_player2_position[1]][system_player2_position[0]] = " "
					system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]-1] = "#"
					system_player2_position[0] -= 1
					system_player2_position[1] += 1
		except:
			pass

	if("m" in system_player3_output and system_player3_is_alive):
		system_player3_output = system_player3_output.replace("m", "")
		try:
			if(system_player3_output == ">"):
				if(system_pythonfights_space[system_player3_position[1]][system_player3_position[0]+1] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]+1] = "#"
					system_player3_position[0] += 1
			if(system_player3_output == "<"):
				if(system_pythonfights_space[system_player3_position[1]][system_player3_position[0]-1] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]-1] = "#"
					system_player3_position[0] -= 1
			if(system_player3_output == "+"):
				if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]] = "#"
					system_player3_position[1] -= 1
			if(system_player3_output == "-"):
				if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]] = "#"
					system_player3_position[1] += 1
			if(system_player3_output == ">+"):
				if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]+1] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]+1] = "#"
					system_player3_position[0] += 1
					system_player3_position[1] -= 1
			if(system_player3_output == ">-"):
				if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]+1] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]+1] = "#"
					system_player3_position[0] += 1
					system_player3_position[1] += 1
			if(system_player3_output == "<+"):
				if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]-1] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]-1] = "#"
					system_player3_position[0] -= 1
					system_player3_position[1] -= 1
			if(system_player3_output == "<-"):
				if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]-1] == " "):
					system_pythonfights_space[system_player3_position[1]][system_player3_position[0]] = " "
					system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]-1] = "#"
					system_player3_position[0] -= 1
					system_player3_position[1] += 1
		except:
			pass
	if("m" in system_player4_output and system_player4_is_alive):
		system_player4_output = system_player4_output.replace("m", "")
		try:
			if(system_player4_output == ">"):
				if(system_pythonfights_space[system_player4_position[1]][system_player4_position[0]+1] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]+1] = "#"
					system_player4_position[0] += 1
			if(system_player4_output == "<"):
				if(system_pythonfights_space[system_player4_position[1]][system_player4_position[0]-1] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]-1] = "#"
					system_player4_position[0] -= 1
			if(system_player4_output == "+"):
				if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]] = "#"
					system_player4_position[1] -= 1
			if(system_player4_output == "-"):
				if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]] = "#"
					system_player3_position[1] += 1
			if(system_player4_output == ">+"):
				if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]+1] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]+1] = "#"
					system_player4_position[0] += 1
					system_player4_position[1] -= 1
			if(system_player4_output == ">-"):
				if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]+1] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]+1] = "#"
					system_player4_position[0] += 1
					system_player4_position[1] += 1
			if(system_player4_output == "<+"):
				if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]-1] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]-1] = "#"
					system_player4_position[0] -= 1
					system_player4_position[1] -= 1
			if(system_player4_output == "<-"):
				if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]-1] == " "):
					system_pythonfights_space[system_player4_position[1]][system_player4_position[0]] = " "
					system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]-1] = "#"
					system_player4_position[0] -= 1
					system_player4_position[1] += 1
		except:
			pass
	if("b" in system_player1_output and system_player1_is_alive):
		system_player1_output = system_player1_output.replace("b", "")
		try:
			if(system_player1_build_delay == 0):
				system_player1_build_delay = system_player_build_delay
				if(system_player1_output == ">"):
					if(system_pythonfights_space[system_player1_position[1]][system_player1_position[0]+1] == " "):
						system_pythonfights_space[system_player1_position[1]][system_player1_position[0]+1] = "*"
				if(system_player1_output == "<"):
					if(system_pythonfights_space[system_player1_position[1]][system_player1_position[0]-1] == " "):
						system_pythonfights_space[system_player1_position[1]][system_player1_position[0]-1] = "*"
				if(system_player1_output == "+"):
					if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]] == " "):
						system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]] = "*"
				if(system_player1_output == "-"):
					if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]] == " "):
						system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]] = "*"
				if(system_player1_output == ">+"):
					if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]+1] == " "):
						system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]+1] = "*"
				if(system_player1_output == ">-"):
					if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]+1] == " "):
						system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]+1] = "*"
				if(system_player1_output == "<+"):
					if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]-1] == " "):
						system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]-1] = "*"
				if(system_player1_output == "<-"):
					if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]-1] == " "):
						system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]-1] = "*"
		except:
			pass
	if("b" in system_player2_output and system_player2_is_alive):
		system_player2_output = system_player2_output.replace("b", "")
		try:
			if(system_player2_build_delay == 0):
				system_player2_build_delay = system_player_build_delay
				if(system_player2_output == ">"):
					if(system_pythonfights_space[system_player2_position[1]][system_player2_position[0]+1] == " "):
						system_pythonfights_space[system_player2_position[1]][system_player2_position[0]+1] = "*"
				if(system_player2_output == "<"):
					if(system_pythonfights_space[system_player2_position[1]][system_player2_position[0]-1] == " "):
						system_pythonfights_space[system_player2_position[1]][system_player2_position[0]-1] = "*"
				if(system_player2_output == "+"):
					if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]] == " "):
						system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]] = "*"
				if(system_player2_output == "-"):
					if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]] == " "):
						system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]] = "*"
				if(system_player2_output == ">+"):
					if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]+1] == " "):
						system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]+1] = "*"
				if(system_player2_output == ">-"):
					if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]+1] == " "):
						system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]+1] = "*"
				if(system_player2_output == "<+"):
					if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]-1] == " "):
						system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]-1] = "*"
				if(system_player2_output == "<-"):
					if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]-1] == " "):
						system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]-1] = "*"
		except:
			pass
	if("b" in system_player3_output and system_player3_is_alive):
		system_player3_output = system_player3_output.replace("b", "")
		try:
			if(system_player3_build_delay == 0):
				system_player3_build_delay = system_player_build_delay
				if(system_player3_output == ">"):
					if(system_pythonfights_space[system_player3_position[1]][system_player3_position[0]+1] == " "):
						system_pythonfights_space[system_player3_position[1]][system_player3_position[0]+1] = "*"
				if(system_player3_output == "<"):
					if(system_pythonfights_space[system_player3_position[1]][system_player3_position[0]-1] == " "):
						system_pythonfights_space[system_player3_position[1]][system_player3_position[0]-1] = "*"
				if(system_player3_output == "+"):
					if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]] == " "):
						system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]] = "*"
				if(system_player3_output == "-"):
					if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]] == " "):
						system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]] = "*"
				if(system_player3_output == ">+"):
					if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]+1] == " "):
						system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]+1] = "*"
				if(system_player3_output == ">-"):
					if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]+1] == " "):
						system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]+1] = "*"
				if(system_player3_output == "<+"):
					if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]-1] == " "):
						system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]-1] = "*"
				if(system_player3_output == "<-"):
					if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]-1] == " "):
						system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]-1] = "*"
		except:
			pass
	if("b" in system_player4_output and system_player4_is_alive):
		system_player4_output = system_player4_output.replace("b", "")
		try:
			if(system_player4_build_delay == 0):
				system_player4_build_delay = system_player_build_delay
				if(system_player4_output == ">"):
					if(system_pythonfights_space[system_player4_position[1]][system_player4_position[0]+1] == " "):
						system_pythonfights_space[system_player4_position[1]][system_player4_position[0]+1] = "*"
				if(system_player4_output == "<"):
					if(system_pythonfights_space[system_player4_position[1]][system_player4_position[0]-1] == " "):
						system_pythonfights_space[system_player4_position[1]][system_player4_position[0]-1] = "*"
				if(system_player4_output == "+"):
					if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]] == " "):
						system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]] = "*"
				if(system_player4_output == "-"):
					if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]] == " "):
						system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]] = "*"
				if(system_player4_output == ">+"):
					if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]+1] == " "):
						system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]+1] = "*"
				if(system_player4_output == ">-"):
					if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]+1] == " "):
						system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]+1] = "*"
				if(system_player4_output == "<+"):
					if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]-1] == " "):
						system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]-1] = "*"
				if(system_player4_output == "<-"):
					if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]-1] == " "):
						system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]-1] = "*"
		except:
			pass
			
	system_gonna_be_popped = []
	if(len(system_bullet_data) > 0):
		for x in range(0, len(system_bullet_data)):
			if(not system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] == "*"):
				system_gonna_be_popped.append(x)
			else:
				if(system_bullet_data[x][2] == ">"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]+1] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]+1] = "*"
							system_bullet_data[x][0] += 1
						elif(system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]+1] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]+1] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]+1] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]+1] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
				if(system_bullet_data[x][2] == "<"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]-1] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]-1] = "*"
							system_bullet_data[x][0] -= 1
						elif(system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]-1] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]-1] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]-1] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]-1] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
				if(system_bullet_data[x][2] == "+"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]] = "*"
							system_bullet_data[x][1] -= 1
						elif(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
				if(system_bullet_data[x][2] == "-"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]] = "*"
							system_bullet_data[x][1] += 1
						elif(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
				if(system_bullet_data[x][2] == ">+"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]+1] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]+1] = "*"
							system_bullet_data[x][0] += 1
							system_bullet_data[x][1] -= 1
						elif(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]+1] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]+1] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]+1] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]+1] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
				if(system_bullet_data[x][2] == ">-"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]+1] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]+1] = "*"
							system_bullet_data[x][0] += 1
							system_bullet_data[x][1] += 1
						elif(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]+1] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]+1] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]+1] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]+1] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
				if(system_bullet_data[x][2] == "<+"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]-1] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]-1] = "*"
							system_bullet_data[x][0] -= 1
							system_bullet_data[x][1] -= 1
						elif(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]-1] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]-1] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]-1] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]-1][system_bullet_data[x][0]-1] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
				if(system_bullet_data[x][2] == "<-"):
					try:
						if(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]-1] == " "):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]-1] = "*"
							system_bullet_data[x][0] -= 1
							system_bullet_data[x][1] += 1
						elif(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]-1] == "*"):
							system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]-1] = " "
						elif(system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]-1] == "#"):
							system_pythonfights_space[system_bullet_data[x][1]+1][system_bullet_data[x][0]-1] = " "
					except:
						system_pythonfights_space[system_bullet_data[x][1]][system_bullet_data[x][0]] = " "
	for x in range(0, len(system_gonna_be_popped)):
		system_bullet_data.pop(system_gonna_be_popped[x])
	del system_gonna_be_popped
	
	if("s" in system_player1_output and system_player1_is_alive):
		system_player1_output = system_player1_output.replace("s", "")
		try:
			if(system_player1_bullet_delay == 0):
				system_player1_bullet_delay = system_player_bullet_delay
				if(system_player1_output == ">"):
					if(system_pythonfights_space[system_player1_position[1]][system_player1_position[0]+1] == " "):
						system_pythonfights_space[system_player1_position[1]][system_player1_position[0]+1] = "*"
						system_bullet_data.append([system_player1_position[0]+1, system_player1_position[1], system_player1_output])
				if(system_player1_output == "<"):
					if(system_pythonfights_space[system_player1_position[1]][system_player1_position[0]-1] == " "):
						system_pythonfights_space[system_player1_position[1]][system_player1_position[0]-1] = "*"
						system_bullet_data.append([system_player1_position[0]-1, system_player1_position[1], system_player1_output])
				if(system_player1_output == "+"):
					if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]] == " "):
						system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]] = "*"
						system_bullet_data.append([system_player1_position[0], system_player1_position[1]-1, system_player1_output])
				if(system_player1_output == "-"):
					if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]] == " "):
						system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]] = "*"
						system_bullet_data.append([system_player1_position[0], system_player1_position[1]+1, system_player1_output])
				if(system_player1_output == ">+"):
					if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]+1] == " "):
						system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]+1] = "*"
						system_bullet_data.append([system_player1_position[0]+1, system_player1_position[1]-1, system_player1_output])
				if(system_player1_output == ">-"):
					if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]+1] == " "):
						system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]+1] = "*"
						system_bullet_data.append([system_player1_position[0]+1, system_player1_position[1]+1, system_player1_output])
				if(system_player1_output == "<+"):
					if(system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]-1] == " "):
						system_pythonfights_space[system_player1_position[1]-1][system_player1_position[0]-1] = "*"
						system_bullet_data.append([system_player1_position[0]-1, system_player1_position[1]-1, system_player1_output])
				if(system_player1_output == "<-"):
					if(system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]-1] == " "):
						system_pythonfights_space[system_player1_position[1]+1][system_player1_position[0]-1] = "*"
						system_bullet_data.append([system_player1_position[0]-1, system_player1_position[1]+1, system_player1_output])
		except:
			pass

	if("s" in system_player2_output and system_player2_is_alive):
		system_player2_output = system_player2_output.replace("s", "")
		try:
			if(system_player2_bullet_delay == 0):
				system_player2_bullet_delay = system_player_bullet_delay
				if(system_player2_output == ">"):
					if(system_pythonfights_space[system_player2_position[1]][system_player2_position[0]+1] == " "):
						system_pythonfights_space[system_player2_position[1]][system_player2_position[0]+1] = "*"
						system_bullet_data.append([system_player2_position[0]+1, system_player2_position[1], system_player2_output])
				if(system_player2_output == "<"):
					if(system_pythonfights_space[system_player2_position[1]][system_player2_position[0]-1] == " "):
						system_pythonfights_space[system_player2_position[1]][system_player2_position[0]-1] = "*"
						system_bullet_data.append([system_player2_position[0]-1, system_player2_position[1], system_player2_output])
				if(system_player2_output == "+"):
					if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]] == " "):
						system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]] = "*"
						system_bullet_data.append([system_player2_position[0], system_player2_position[1]-1, system_player2_output])
				if(system_player2_output == "-"):
					if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]] == " "):
						system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]] = "*"
						system_bullet_data.append([system_player2_position[0], system_player2_position[1]+1, system_player2_output])
				if(system_player2_output == ">+"):
					if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]+1] == " "):
						system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]+1] = "*"
						system_bullet_data.append([system_player2_position[0]+1, system_player2_position[1]-1, system_player2_output])
				if(system_player2_output == ">-"):
					if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]+1] == " "):
						system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]+1] = "*"
						system_bullet_data.append([system_player2_position[0]+1, system_player2_position[1]+1, system_player2_output])
				if(system_player2_output == "<+"):
					if(system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]-1] == " "):
						system_pythonfights_space[system_player2_position[1]-1][system_player2_position[0]-1] = "*"
						system_bullet_data.append([system_player2_position[0]-1, system_player2_position[1]-1, system_player2_output])
				if(system_player2_output == "<-"):
					if(system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]-1] == " "):
						system_pythonfights_space[system_player2_position[1]+1][system_player2_position[0]-1] = "*"
						system_bullet_data.append([system_player2_position[0]-1, system_player2_position[1]+1, system_player2_output])
		except:
			pass

	if("s" in system_player3_output and system_player3_is_alive):
		system_player3_output = system_player3_output.replace("s", "")
		try:
			if(system_player3_bullet_delay == 0):
				system_player3_bullet_delay = system_player_bullet_delay
				if(system_player3_output == ">"):
					if(system_pythonfights_space[system_player3_position[1]][system_player3_position[0]+1] == " "):
						system_pythonfights_space[system_player3_position[1]][system_player3_position[0]+1] = "*"
						system_bullet_data.append([system_player3_position[0]+1, system_player3_position[1], system_player3_output])
				if(system_player3_output == "<"):
					if(system_pythonfights_space[system_player3_position[1]][system_player3_position[0]-1] == " "):
						system_pythonfights_space[system_player3_position[1]][system_player3_position[0]-1] = "*"
						system_bullet_data.append([system_player3_position[0]-1, system_player3_position[1], system_player3_output])
				if(system_player3_output == "+"):
					if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]] == " "):
						system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]] = "*"
						system_bullet_data.append([system_player3_position[0], system_player3_position[1]-1, system_player3_output])
				if(system_player3_output == "-"):
					if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]] == " "):
						system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]] = "*"
						system_bullet_data.append([system_player3_position[0], system_player3_position[1]+1, system_player3_output])
				if(system_player3_output == ">+"):
					if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]+1] == " "):
						system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]+1] = "*"
						system_bullet_data.append([system_player3_position[0]+1, system_player3_position[1]-1, system_player3_output])
				if(system_player3_output == ">-"):
					if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]+1] == " "):
						system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]+1] = "*"
						system_bullet_data.append([system_player3_position[0]+1, system_player3_position[1]+1, system_player3_output])
				if(system_player3_output == "<+"):
					if(system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]-1] == " "):
						system_pythonfights_space[system_player3_position[1]-1][system_player3_position[0]-1] = "*"
						system_bullet_data.append([system_player3_position[0]-1, system_player3_position[1]-1, system_player3_output])
				if(system_player3_output == "<-"):
					if(system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]-1] == " "):
						system_pythonfights_space[system_player3_position[1]+1][system_player3_position[0]-1] = "*"
						system_bullet_data.append([system_player3_position[0]-1, system_player3_position[1]+1, system_player3_output])
		except:
			pass

	if("s" in system_player4_output and system_player4_is_alive):
		system_player4_output = system_player4_output.replace("s", "")
		try:
			if(system_player4_bullet_delay == 0):
				system_player4_bullet_delay = system_player_bullet_delay
				if(system_player4_output == ">"):
					if(system_pythonfights_space[system_player4_position[1]][system_player4_position[0]+1] == " "):
						system_pythonfights_space[system_player4_position[1]][system_player4_position[0]+1] = "*"
						system_bullet_data.append([system_player4_position[0]+1, system_player4_position[1], system_player4_output])
				if(system_player4_output == "<"):
					if(system_pythonfights_space[system_player4_position[1]][system_player4_position[0]-1] == " "):
						system_pythonfights_space[system_player4_position[1]][system_player4_position[0]-1] = "*"
						system_bullet_data.append([system_player4_position[0]-1, system_player4_position[1], system_player4_output])
				if(system_player4_output == "+"):
					if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]] == " "):
						system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]] = "*"
						system_bullet_data.append([system_player4_position[0], system_player4_position[1]-1, system_player4_output])
				if(system_player4_output == "-"):
					if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]] == " "):
						system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]] = "*"
						system_bullet_data.append([system_player4_position[0], system_player4_position[1]+1, system_player4_output])
				if(system_player4_output == ">+"):
					if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]+1] == " "):
						system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]+1] = "*"
						system_bullet_data.append([system_player4_position[0]+1, system_player4_position[1]-1, system_player4_output])
				if(system_player4_output == ">-"):
					if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]+1] == " "):
						system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]+1] = "*"
						system_bullet_data.append([system_player4_position[0]+1, system_player4_position[1]+1, system_player4_output])
				if(system_player4_output == "<+"):
					if(system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]-1] == " "):
						system_pythonfights_space[system_player4_position[1]-1][system_player4_position[0]-1] = "*"
						system_bullet_data.append([system_player4_position[0]-1, system_player4_position[1]-1, system_player4_output])
				if(system_player4_output == "<-"):
					if(system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]-1] == " "):
						system_pythonfights_space[system_player4_position[1]+1][system_player4_position[0]-1] = "*"
						system_bullet_data.append([system_player4_position[0]-1, system_player4_position[1]+1, system_player4_output])
		except:
			pass

	# Process Current Frame

	# Reduce Delay
	if(system_player1_bullet_delay != 0):
		system_player1_bullet_delay -= 1
	if(system_player2_bullet_delay != 0):
		system_player2_bullet_delay -= 1
	if(system_player3_bullet_delay != 0):
		system_player3_bullet_delay -= 1
	if(system_player4_bullet_delay != 0):
		system_player4_bullet_delay -= 1
	if(system_player1_build_delay != 0):
		system_player1_build_delay -= 1
	if(system_player2_build_delay != 0):
		system_player2_build_delay -= 1
	if(system_player3_build_delay != 0):
		system_player3_build_delay -= 1
	if(system_player4_build_delay != 0):
		system_player4_build_delay -= 1
	# Reduce Delay

	# Output Current Frame
	system_tmp_str = ""
	for x in range(0, len(system_pythonfights_space)):
		for xx in range(0, len(system_pythonfights_space[x])):
			system_tmp_str += system_pythonfights_space[x][xx]
		system_tmp_str += "\n"
	system_tmp_str += "-"
	system_game_write_file = open("game.pyf", "a")
	system_game_write_file.write(system_tmp_str+"\n")
	system_game_write_file.close()
	del system_tmp_str
	# Output Current Frame

	if(system_frame == system_frame_limit):
		break
	system_frame += 1
# Create Game_____________________________________________________________________
print("Game created successfully")
while True:
	pass
