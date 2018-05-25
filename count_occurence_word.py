string ="hello vaneet hello hello vaneet welcome hello".split()


count = dict()


for word in string:
  if word in count:
    count[word] +=1
  else:
    count[word] = 1

print(count)
