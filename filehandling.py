with open('logs.txt') as f:
  dict = {k: v for k, v in (x.split(':') for x in f)}

