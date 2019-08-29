def high_low(txt):
	a = list(map(int, txt.split()))
	return "{} {}".format(max(a), min(a))

print(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"),)
print(high_low("1 2 3 4 5"))
print(high_low("13"))
print(high_low("1 2 -3 4 5"))
print(high_low("1 9 3 4 -5"))