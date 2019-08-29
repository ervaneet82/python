s="vaneet gupta"


for x in s[:].split():
  s = s.replace(x,x.capitalize())

print(s)