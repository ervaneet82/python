def primes_below_num(n):
	l = []
	for n in range(n + 1):
		if n > 1:
			for i in range(2, n):
				if (n % i) == 0:
					break
			else:
				l.append(n)
	return l

print(primes_below_num(5))