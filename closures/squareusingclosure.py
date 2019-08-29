def pow(n):
  def inner(x):
    return x ** n
  return inner

square=pow(2)
print(square.__closure__)  # Gives memory address of python cell id and reference to variable
print(hex(id(2))) # memory address of the int 2

print(square(5))
