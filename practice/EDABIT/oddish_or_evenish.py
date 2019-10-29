'''
Create a function that determines whether a number is Oddish or Evenish.
A number is Oddish if the sum of all of its digits is odd, and a number is Evenish
if the sum of all of its digits is even. If a function is Oddish, return "Oddish".
Otherwise, return "Evenish".
For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4.
oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.
'''

def oddish_or_evenish(num):
	return 'Oddish' if sum(map(int,str(num))) % 2 else 'Evenish'

print(oddish_or_evenish(43))