def outer():
  x = "hello"
  def inner1():
    nonlocal x
    x = "python"
    def inner2():
      nonlocal x
      x = "monty"
    print("inner(before)",x)
    inner2()
    print("inner(after)",x)
  inner1()
  print("outer",x)

outer()