"""
Find longest word in string
"""

str = 'hello welcome to python language'

def count_word(str):
  counts = dict()
  words = str.split()

  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  print(counts)

def reverse_string(str):
  l=[]
  for s in str.split():
    l.append(''.join(reversed(s)))
  print(l)

def string_inversion(str):
  l=[]
  for s in str:
    if s.isupper():
      l.append(s.lower())
    elif s.islower():
      l.append(s.upper())
    elif s.isspace():
      l.append(s)

  print(''.join(l))

#string_inversion("vaNeet iS PytHon")

def count_word_in_file(filename):
  count = 0
  with open(filename) as f:
    for lines in f.read():
      if lines.isspace():
        count += 1
  print(count)

def count_vowel_in_file(filename):
  vowels = {'a':0,'i':0,'e':0,'u':0,'o':0}
  with open(filename) as f:
    for lines in f.read():
      for key,value in vowels.items():
        if key in lines:
          vowels[key] = value + 1
  print(vowels)


from functools import reduce
from operator import mul

fac  = reduce(mul,range(1,6))

