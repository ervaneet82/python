def letter_check(lst):
	s1, s2 = lst
	for char in s2:
		if char.lower()in s1.lower():
			pass
		else:
			return False
	return True


print(letter_check(["compadres", "DRAPES"]))