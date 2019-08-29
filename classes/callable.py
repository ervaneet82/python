from time import perf_counter

class Timer:
  def __init__(self):
    self.start = perf_counter()

  def __call__(self):
    return perf_counter() - self.start

t1=Timer()
print(t1())