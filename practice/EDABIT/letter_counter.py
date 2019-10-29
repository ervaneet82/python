def letter_counter(lst,letter):
	arr = []
	for li in lst:
		if letter in li:
			arr.append(li.count(letter))
	print(sum(arr))

letter_counter([
	['D', 'E', 'Y', 'H', 'A', 'D'],
	['C', 'B', 'Z', 'Y', 'J', 'K'],
	['D', 'B', 'C', 'A', 'M', 'N'],
	['F', 'G', 'G', 'R', 'S', 'R'],
	['V', 'X', 'H', 'A', 'S', 'S']
], 'D')