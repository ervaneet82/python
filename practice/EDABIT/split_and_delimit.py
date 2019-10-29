'''
Write a function that splits a string into substrings of size n,
adding a specified delimiter between each of the pieces.
split_and_delimit("bellow", 2, "&") ➞ "be&ll&ow"
'''

def split_and_delimit(txt, num, delimiter):
	return delimiter.join(txt[i:i+num] for i in range(0, len(txt), num))

print(split_and_delimit("bellow", 2, "&"))