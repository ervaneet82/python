def counter(fn):
  count = 0
  def inner(*args,**kwargs):
    nonlocal count
    count +=1
    print('{0} was called {1} times'.format(fn.__name__,count))
    return fn(*args,**kwargs)
  return inner

@counter
def mult(a,b,c=1):
  return a * b *c

print(mult.__name__)