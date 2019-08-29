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

@logged
def func1():
  pass

func1()

#Decorator without @
# func1 = logged(func1)
# func1()

