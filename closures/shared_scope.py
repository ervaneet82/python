def outer():
	count = 0
	def inc1():
		nonlocal count
		count += 1
		return count
	def inc2():
		nonlocal count
		count +=1
		return count
	return inc1, inc2

f1, f2 = outer()

print(f1())
print(f2())
