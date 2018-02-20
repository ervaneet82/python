string="Hello"

#my_iterator=iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator)) ## It will terminate the program by calling StopIteration error.
#


my_list=["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]

my_iterator = iter(my_list)

for i in range(0,len(my_list)):
  next_item = next(my_iterator)
  print(next_item)