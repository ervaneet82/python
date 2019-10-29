'''
# The last digit of 25 is 5, the last digit of 21 is 1, and the last
# digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
# to the last digit of 125(5).
'''
def last_dig(a, b, c):
	# s1, s2, s3 = int(str(a)[-1]), int(str(b)[-1]), int(str(c)[-1])
	# if int(str(s1 * s2)[-1]) == s3:
	# 	return True
	# return False
	return str(a * b)[-1] == str(c)[-1]
print(last_dig(25, 21, 125))
print(last_dig(12, 15, 10))