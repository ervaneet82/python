def sum_two_smallest_nums(lst):
	return sum(sorted([x for x in lst if x > 0])[:2])


print(sum_two_smallest_nums([19, 5, 42, 2, 77]))
print(sum_two_smallest_nums([2, 9, 6, -1]))