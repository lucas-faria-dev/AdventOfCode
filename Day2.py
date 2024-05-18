import Utils
fin = open("Day02.txt")
raw_games = fin.read().split("\n")


def evaluate_game(game, game_number):
	"""
	Red, Green or Blue cubes
	Each turn is separated by a semicolon
	maximum amount of cubes:
	red = 12
	green = 13
	blue = 14
	One game have one or more turns.
	A turn have one or more cubes
	"""
	game_aux = game.replace("Game " + str(game_number) + ":", "")
	# separates all turns
	turns = game_aux.split(";")
	# Rules
	max_red_cubes = 12
	max_green_cubes = 13
	max_blue_cubes = 14

	for turn in turns:
		parsed_turn = parse_turn(turn)
		if parsed_turn[0] > max_red_cubes or parsed_turn[1] > max_green_cubes or parsed_turn[2] > max_blue_cubes:
			return False
	return True


def get_minimal_cubes(game, game_number):
	"""
	Red, Green or Blue cubes
	Each turn is separated by a semicolon
	One game have one or more turns.
	A turn have one or more cubes
	"""
	game_aux = game.replace("Game " + str(game_number) + ":", "")
	# separates all turns
	turns = game_aux.split(";")
	cubes = [0, 0, 0]

	for turn in turns:
		parsed_turn = parse_turn(turn)
		if parsed_turn[0] > cubes[0]:
			cubes[0] = parsed_turn[0]
		if parsed_turn[1] > cubes[1]:
			cubes[1] = parsed_turn[1]
		if parsed_turn[2] > cubes[2]:
			cubes[2] = parsed_turn[2]
	return cubes


def parse_turn(turn):
	# separate all cubes
	raw_cubes = turn.split(",")
	# 0 = red; 1 = green; 2 = blue
	parsed_cubes = [0, 0, 0]
	for cube in raw_cubes:
		cube = cube.strip()
		number_as_string = ""
		for char in cube:
			if Utils.string_to_int_validate(char):
				number_as_string = number_as_string + str(char)
		if cube.find("red") != -1:
			parsed_cubes[0] = int(number_as_string)
		if cube.find("green") != -1:
			parsed_cubes[1] = int(number_as_string)
		if cube.find("blue") != -1:
			parsed_cubes[2] = int(number_as_string)
	return parsed_cubes


def get_game_number(game):
	return int(game[0:game.find(":")].replace("Game ", ""))


# Test cases
# print(evaluate_game(game="Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", game_number=1))
# print(get_game_number(game="Game 151: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))

# Snow Island Day 2 part 1
total = 0
for g in raw_games:
	current_game_number = get_game_number(game=g)
	if evaluate_game(game=g, game_number=current_game_number):
		total += current_game_number
print("The total is " + str(total))

# Snow Island Day 2 part 2
total = 0
for g in raw_games:
	current_game_number = get_game_number(game=g)
	minimal_cubes_by_game = get_minimal_cubes(game=g, game_number=current_game_number)
	product = minimal_cubes_by_game[0] * minimal_cubes_by_game[1] * minimal_cubes_by_game[2]
	total += product
print("The total is " + str(total))
