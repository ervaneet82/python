import operator

my_list = [1, 2, 3, 4]

operator.setitem(my_list,1,100)

print(my_list)

operator.delitem(my_list,3)

print(my_list)

f = operator.itemgetter(2)
print(f(my_list))

## itemgetter return in tuple

s = "python"
print("String : ",s)
print(f(s))


### attribute getter

d = {"name":"vaneet","lastname":"gupta"}

sort = sorted(d.items(), key=operator.itemgetter(1))

print(sort)