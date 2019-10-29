'''
In each input list, every number repeats at least once, except for two.
Write a function that returns the two unique numbers.
returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]
'''

def return_unique(lst):
	return [x for x in lst if lst.count(x) == 1]

print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))