fin = open("Day01.txt")
codes = fin.read().split("\n")


def get_hidden_number(code):
	"""Gets the first numeric digit from the code.
	If is_from_beginning == True, the search starts from the code[0]
	if False it starts from code[len(code) - 1]."""
	if code.strip() == "":
		return 0
	code_aux = code.strip().lower()
	numbers_dict = {
		"0": 0,
		"1": 1,
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
		"zero": 0,
		"one": 1,
		"two": 2,
		"three": 3,
		"four": 4,
		"five": 5,
		"six": 6,
		"seven": 7,
		"eight": 8,
		"nine": 9
	}
	lower_index = -1
	first_number = ''
	upper_index = -1
	second_number = ''
	for i in numbers_dict:
		current_lower_index = code_aux.find(i)
		if current_lower_index != -1:
			if current_lower_index < lower_index or lower_index == -1:
				# if we found a lower index or is the first iteration.
				lower_index = current_lower_index
				first_number = str(numbers_dict[i])
		current_upper_index = code_aux.rfind(i)
		if current_upper_index != -1:
			if current_upper_index > upper_index:
				# if we found a higher index or is the first iteration.
				upper_index = current_upper_index
				second_number = str(numbers_dict[i])
	return int(first_number + second_number)


total = 0
for n in codes:
	number = get_hidden_number(n)
	print(str(n) + " " + str(number))
	total = total + int(number)

print("The total is " + str(total))
