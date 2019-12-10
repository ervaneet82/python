def counter():
	count = 0
	def inc():
		nonlocal count
		count += 1
		return count
	return inc

fn = counter()
print(fn.__code__.co_freevars)
print(fn())