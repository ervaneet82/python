'''
Write a function that returns the first n vowels of a string.
first_n_vowels("sharpening skills", 3) ➞ "aei"
'''

import re
def first_n_vowels(txt, n):
	vowels = re.findall(r'[aeiou]', txt)
	return ''.join(vowels)[:n] if len(vowels) >= n else 'invalid'

print(first_n_vowels("sharpening skills", 3))
print(first_n_vowels("major league", 5))
print(first_n_vowels("shrimpy", 2))