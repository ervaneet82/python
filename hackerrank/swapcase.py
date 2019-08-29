string="pYtHon"
new_string=[]
for s in string:
  if s.isupper():
    new_string.append(s.lower())
  elif s.islower():
    new_string.append(s.upper())
  else:
    print("No new char")

print(''.join(new_string))