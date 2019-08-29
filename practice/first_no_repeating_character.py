'''
Find the First Non-Repeated Character
'''

def first_non_repeated_character(txt):
	output = []
	for char in txt:
		if txt.count(char) == 1:
			return char
	return False

# print(first_non_repeated_character("the quick brown fox jumps then quickly blows air"))
#
# print(first_non_repeated_character("hhheeelllooo"))

number = "123"
print(int(''.join((sorted(number)[::-1]))))