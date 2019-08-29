def logged(fn):
  from functools import wraps
  from datetime import datetime,timezone

  @wraps(fn)
  def inner(*args,**kwargs):
    run_dt = datetime.now(timezone.utc)
    result= fn(*args,**kwargs)
    print('{0}: called {1}'.format(run_dt,fn.__name__))
    return result
  return inner

def timed(fn):
  from functools import wraps
  from time import perf_counter

  @wraps(fn)
  def inner(*args,**kwargs):
    start = perf_counter()
    result = fn(*args,**kwargs)
    end = perf_counter()
    print('{0} ran for {1:.6f}s'.format(fn.__name__,end-start))
    return result
  return inner

@logged
@timed

def fact(n):
  from operator import mul
  from functools import reduce

  return reduce(mul,range(1,n+1))

print(fact(6))

