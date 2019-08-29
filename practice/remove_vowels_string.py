import re
def silence_Trump(txt):
	return re.sub('[AaIiOoeEuU]','',txt)
#
# print(silence_Trump("I have never seen a thin person drinking Diet Coke."))

def sum_two_smallest_nums(lst):
	lst = [item for item in lst if item >= 0]
	n1 = min(lst)
	lst.remove(n1)
	n2 = min(lst)
	return n1 + n2

#print(sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))

def letter_check(lst):
	if len(set(lst[1].lower()).difference(set(lst[0].lower()))) > 0:
		return False
	else:
		return True



