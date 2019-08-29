lines = []

count = 0
with open('logs.txt') as f:
  for line in f.read():
    for char in line.strip():
      count +=1


print(count)