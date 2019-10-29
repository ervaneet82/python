def duplicate_count(txt):
	lst = []
	for char in txt:
		if txt.count(char) > 1:
			lst.append(char)
	print(len(list(set(lst))))

duplicate_count("abcddee")