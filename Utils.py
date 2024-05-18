def string_to_int_validate(string):
	try:
		int(string)
		return True
	except ValueError:
		return False