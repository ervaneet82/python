import textwrap
def wrap(string, max_width):
	wrapper = textwrap.TextWrapper(width=max_width)
	word_list = wrapper.wrap(text=string)
	return word_list


word_list = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)

for element in word_list:
	print(element)
