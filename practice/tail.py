import os

filename = os.path.abspath(os.path.join('calc_letter_numbers.py'))

lines=[]
with open(filename) as f:
  for line in f.readlines():
    lines.append(line)

for line in lines[-2::]:
  print(line.strip())
