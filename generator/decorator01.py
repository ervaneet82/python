def smart_divide(func):
  def inner(a,b):
    print("I am going to divide {} and {}".format(a,b))
    if b == 0:
      print("Whoops can't divide by zero")
      return
    return func(a,b)
  return inner

@smart_divide
def divide(a,b):
  return a/b

print(divide(4,2))
divide(4,0)