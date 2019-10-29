def first_non_repeated_character(txt):
	for c in txt:
		if txt.count(c) == 1:
			return c
	return False

print(first_non_repeated_character("the quick brown fox jumps then quickly blows air"))
print(first_non_repeated_character("the misty examination pleases into the drab county"))
print(first_non_repeated_character(""))