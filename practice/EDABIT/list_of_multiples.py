'''
Create a function that takes two numbers as arguments (num, length)
and returns a list of multiples of num up to length.
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
'''

def list_of_multiples (num, length):
	return [i * num for i in range(1, length+1)]

print(list_of_multiples(7, 5))