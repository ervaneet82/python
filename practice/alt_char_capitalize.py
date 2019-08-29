def alternating_caps(txt):
	array = []
	for num in range(0, len(txt)):
		if num % 2 ==0:
			array.append(txt[num].upper())
		else:
			array.append(txt[num].lower())
	return ''.join(array)

print(alternating_caps("OMG!!! This website is awesome!!"))