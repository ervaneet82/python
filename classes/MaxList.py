class Maxlist(object):
  def __init__(self,size):
    self.size = size
    self.mylist = []
  def append_list(self,value):
    self.mylist.append(value)
    if len(self.mylist) > self.size:
      self.mylist.pop(0)
  def get_list(self):
    return self.mylist

a = Maxlist(3)
a.append_list(4)
a.append_list(5)
a.append_list(6)
a.append_list(9)

print(a.get_list())