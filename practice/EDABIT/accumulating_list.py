"""
Create a function that takes in a list and returns a list of the accumulating sum.
accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]

Explaination [1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
"""

def accumulating_list(lst):
	return [sum(lst[:i + 1]) for i in range(len(lst))]

print(accumulating_list([1, 2, 3, 4]))