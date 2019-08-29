def reverse(arg):
	return "boolean expected" if not isinstance(arg,bool) else not arg

print(reverse(True))