#### Input the number in interger and calculate factorial of the number
### Python version 3.6.2

n=int(input("Enter the number : "))

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(n))
