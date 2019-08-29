from collections import Counter

l=input().split()

list=sorted(l)
count=Counter(list)

print(count)