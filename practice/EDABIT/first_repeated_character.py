def first_repeated_character(txt):
	for char in txt:
		if txt.count(char) > 1:
			return char
	return False

print(first_repeated_character("Vaneet"))
print(first_repeated_character("the quick brown fox jumps then quickly blows air"))