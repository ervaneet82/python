def is_smooth(txt):
	lst = txt.lower().split(" ")
	for index in range(0,len(lst) - 1):
		if lst[index][-1] != lst[index + 1][0]:
			return False
	return True

print(is_smooth("Rita asks Sam mean numbered dilemmas"))