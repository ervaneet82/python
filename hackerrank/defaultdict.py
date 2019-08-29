n, r = input().split()

n1 = int(n)
n2 = int(r)

result = []
for i in range(n1 + n2):
	result.append(input())

result = result[:len(result) - n2]

store = (result[-n2::])

for index, item in enumerate(result):
	if store in result:
		print(index)