def reverse(txt):
	a = txt.split()
	new_array = []
	for s in a:
		if len(s) >= 5:
			new_array.append(s[::-1])
		else:
			new_array.append(s)
	return " ".join(new_array)

print(reverse("Reverse the order of every word greater than or equal to five characters."))
