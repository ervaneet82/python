"""
Create a function that returns the indices of all
occurrences of an item in the list.
get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]
"""

def get_indices(lst, el):
	# new_lst = []
	# for ind, val in enumerate(lst):
	# 	if val == el:
	# 		new_lst.append(ind)
	# return new_lst
	return [idx for idx, i in enumerate(lst) if i == el]

print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))


