d = {"DIGITS":0,"LETTERS":0}
st = input("Enter the string : ")
def calc(st):
  """Calculate the number of letters and digits in the string"""
  for s in st:
    if s.isdigit():
      d['DIGITS'] +=1
    elif s.isalpha():
      d['LETTERS'] +=1
    else:
      pass

calc(st)
print(d)
