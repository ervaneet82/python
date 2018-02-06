import re

email = "ervaneet82@gmail.co.in"
match = re.match('^[_a-z0-9]+(\.[_[a-z0-9])*\@[a-z0-9]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

if match == None:
  print('Bad Syntax')
  raise ValueError('Bad Syntax')
else:
  print("Validate Email")

