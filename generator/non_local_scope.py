def outer_func():
  x = "hello"
  def inner_func():
    nonlocal x
    x = "python"
  inner_func()
  print(x)

outer_func()