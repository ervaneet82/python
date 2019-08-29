def format_phone_number(lst):
	# s = "".join(map(str, lst))
	# return "({}) {}-{}".format(s[0:3], s[3:6], s[6:])
	return '({}{}{}) {}{}{}-{}{}{}{}'.format(*lst)

print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))



