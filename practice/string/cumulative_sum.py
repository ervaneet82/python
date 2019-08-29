lst = [3, 3, -2, 408, 3, 3]

# sum = []
# for index,value in enumerate(lst):
# 	if index == 0:
# 		sum.append(0 + value)
# 	else:
# 		sum.append(sum[index - 1] + value)



print([sum(lst[:i+1]) for i in range(len(lst))])


from itertools import accumulate
def cumulative_sum(lst):
  return list(accumulate(lst))

print(cumulative_sum([3, 3, -2, 408, 3, 3]))

