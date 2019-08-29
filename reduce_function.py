from functools import reduce

l = [5,8,6,10,9]


### Get max value of any iterables
_max = reduce(lambda a,b: a if a > b else b , l)
print(_max)


### adding of elements in the list
_add = reduce(lambda a,b: a + b , l)
print(_add)

### factorial using reduce function

fac = reduce(lambda a,b: a * b , range(1,5+1))
print(fac)

_min = lambda a,b: a if a < b else b

print("Print minimum number from the lamba func : ", _min(10,2))

def min_sequence(sequence):
  result = sequence[0]
  for x in sequence[1:]:
    result = _min(result,x)
  return result

print("Minimum from min_sequence func : " ,min_sequence(l))


from functools import reduce

l=[1,2,3,4]

mulitply=reduce(lambda a,b: a * b, l)
print(mulitply)