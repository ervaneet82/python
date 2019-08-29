import re
N=int(input())
output=[]
for i in range(N):
	if re.match(r'^[798]\d{9}$',input()):
		output.append("Yes")
	else:
		output.append("No")

for display in output:
	print(display)