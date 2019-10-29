from functools import reduce
from operator import mul
def mystery_func(num):
	#return reduce(mul,(map(int,str(num))))
	return eval("*".join(str(num)))

print(mystery_func(152))
