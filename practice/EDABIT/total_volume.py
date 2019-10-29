from functools import reduce
from operator import mul

def total_volume(*boxes):
	new_arr = []
	for l in boxes:
		new_arr.append(reduce(mul,l))
	print(sum(new_arr))

total_volume([4,2,4],[3,3,3],[1,1,2],[2,1,1])
total_volume([1,1,1])