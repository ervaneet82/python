# a,b=0,1
# n = 10
# while b < 10:
#   a,b=b,a+b
#   print(b,end=' ')

str = "welcome125554"


def count_digit_letter(str):
  d = {"digits":0,"letters":0}
  for char in str:
    if char.isdigit():
      d['digits'] += 1
    else:
      d['letters'] +=1

def print_mini_list_tuple(l):
  from itertools import starmap
  """
  Print mini value from given tuple in list
  :return:
  """
  return list(starmap(min,l))

li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ]
mini_number = print_mini_list_tuple(li1)

import re

result = re.split(r'[.,]+',input().strip(' ,.'))
for out in result:
  print(out)

