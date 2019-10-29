def remove_dups(lst):
	return sorted(set(lst), key=lst.index)


print(remove_dups(["John", "Taylor", "John"]))
print(remove_dups(['javascript', 'python', 'python', 'ruby', 'javascript', 'c', 'ruby']))