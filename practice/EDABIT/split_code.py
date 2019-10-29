'''
You have a list of item codes with the following format: "[letters][digits]"
Create a function that splits these strings into their alphabetic and numeric parts.
split_code("TEWA8392") ➞ ["TEWA", 8392]
'''

import re

def split_code(item):
	digits = int(''.join(re.findall(r'\d', item)))
	letters = ''.join(re.findall(r'\D',item))
	return [letters, digits]
print(split_code("TEWA8392"))