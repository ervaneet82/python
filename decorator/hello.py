def fac(fn):
  def inner(*args,**kwargs):
    result=fn(*args,**kwargs)
    return 'Result of factorial {} is :'.format(*args,**kwargs),result
  return inner

@fac
def factorial(n):
  from operator import mul
  from functools import reduce
  return reduce(mul,range(1,n+1))

print(factorial(6))
