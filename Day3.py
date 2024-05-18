fin = open("Day03_sample.txt")
raw_engine_parts = fin.read().split("\n")


def get_symbol_positions(code):
	"""Returns a zero based position array of all symbols found
	on the string code '.' and integers are not considered symbols"""
	symbol_positions = []
	index = 0
	for char in code:
		if not (char.isdigit()) and char != ".":
			symbol_positions.append(index)
		index += 1
	return symbol_positions


def get_hidden_numbers(code):
	"""Returns an array with the hidden numbers contained in code"""

	if code.strip() == "":
		return []
	code_aux = code.strip().lower()

	number_string = ""
	hidden_numbers = []
	for i in code_aux:
		if i.isdigit():
			number_string += str(i)
		else:
			if number_string.isdigit():
				hidden_numbers.append(int(number_string))
				number_string = ""

	return hidden_numbers


def get_hidden_numbers_position(code):
	"""Gets the hidden number position in code"""

	if code.strip() == "":
		return []

	number_positions = []
	index_start = -1
	index_end = -1
	current_index = 0
	number_position_item = []
	is_last_number_passed = False

	for char in code:
		# set the index start
		if char.isdigit():
			if index_start == -1:
				index_start = current_index
				number_position_item.append(index_start)
			index_end = current_index

			# The whole line is composed by numbers
			if current_index == (len(code) - 1):
				if index_start != index_end:
					number_position_item.append(index_end)
				is_last_number_passed = True

		else:
			is_last_number_passed = index_start != -1

			# set the index end
			if is_last_number_passed and index_end != index_start:
				number_position_item.append(index_end)
			index_end = -1
			index_start = -1

		# append the number position to number positions
		if len(number_position_item) != 0 and is_last_number_passed:
			number_positions.append(number_position_item)

		# clear number_position_item and is_last_number_passed
		if is_last_number_passed:
			number_position_item = []
			is_last_number_passed = False

		current_index += 1

	return number_positions


# Test cases
# Symbol position
print("Symbol position")
print("...*...... " + str(get_symbol_positions("...*......")))
print("..35..633. " + str(get_symbol_positions("..35..633.")))
print("......#... " + str(get_symbol_positions("......#...")))
print(".....+.58. " + str(get_symbol_positions(".....+.58.")))

# Hidden Numbers
print("Hidden Numbers")
print("...*...... " + str(get_hidden_numbers("...*......")))
print("..35..633. " + str(get_hidden_numbers("..35..633.")))
print("......#... " + str(get_hidden_numbers("......#...")))
print(".....+.58. " + str(get_hidden_numbers(".....+.58.")))

# Number Position
print("Number Position")
print("...*...... " + str(get_hidden_numbers_position("...*......")))
print("..35.5633. " + str(get_hidden_numbers_position("..35.5633.")))
print("5232156547 " + str(get_hidden_numbers_position("5232156547")))
print("1.2.3.4.58 " + str(get_hidden_numbers_position("1.2.3.4.58")))
print(".........8 " + str(get_hidden_numbers_position(".........8")))
print("8......... " + str(get_hidden_numbers_position("8.........")))
