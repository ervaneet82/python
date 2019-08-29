import re
def maskify(txt):
	return '{}{}'.format('#' * (len(txt) - 4), txt[-4:])

print(maskify("4556364607935616"))