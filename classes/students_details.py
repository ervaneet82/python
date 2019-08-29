class Students(object):
  def __init__(self,roll_number,name):
    self.roll_number = roll_number
    self.name = name

  @property
  def student_age(self):
    return self.age

  @property
  def student_marks(self):
    return self.marks

  @student_age.setter
  def student_age(self,age):
    self.age = age

  @student_marks.setter
  def student_marks(self,marks):
    self.marks = marks

  def display(self):
    print("Student Name : {}".format(self.name))
    print("Student Roll Number : {}".format(self.roll_number))
    print("Student Age : {}".format(self.age))
    print("Student marks : {}".format(self.marks))

st = Students("Vaneet",11)
st.age = 36
st.marks = 97

st.display()