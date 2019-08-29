# def unique(lst):
# 	return min(set(lst), key=lst.count)

from collections import Counter

def unique(lst):
    return Counter(lst).most_common()[-1][0]

print(unique([3, 3, 3, 7, 3, 3]))

