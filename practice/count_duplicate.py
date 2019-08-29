from collections import Counter
str = "Indivisibilities"

d = Counter(str)
count = 0
# for value in d.values():
# 	if value > 1:
# 		count += 1

count = len([value for value in d.values() if value > 1])

#print(count)

lst = []

if len(lst) == 0:
	print(lst)
else:
	lst.remove(min(lst))

print(lst)


