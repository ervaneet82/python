import os
from itertools import islice

filename = os.path.abspath(os.path.join('practice.py'))

with open(filename) as f:
  for line in islice(f,2):
    print(line.strip())


