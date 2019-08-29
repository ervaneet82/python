square=lambda x: x**2

print(square(4))

f = lambda x, *args,y,**kwargs: (x,*args,y,kwargs)

print(f(1,'a','b',y=100,a=10,b=100))

def apply_func(x,fn):
  return fn(x)

print(apply_func(5,lambda x: x**2))

l=['c','B','D','a']

print("Without lambda : {}".format(sorted(l)))

print("With lambda expression : {}".format(sorted(l,key=lambda s: s.upper())))

### sorted dictionary based on value using lambda expression

d={'def': 300,'abc':200,'ghi':100}

dict=sorted(d, key=lambda e: d[e])

print(d)

### sorted last character

ch = ['Cleese','Idle','Palin','Chapman','Gilliam','Jones']

sorted_char=sorted(ch,key=lambda s: s[-1])
print(sorted_char)


import random

l= [1,2,3,4,5,6,7,8,9]
s = sorted(l, key=lambda x: random.random())

print(s)
