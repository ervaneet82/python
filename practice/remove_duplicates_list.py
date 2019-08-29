def is_symmetrical(num):
	new_num = int(''.join(list(reversed(str(num)))))

	if num == new_num:
		return True
	else:
		return False




print(is_symmetrical(12567))