import math
from math import pow

class Circle:
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return math.pi * pow(self.radius,2)
  def circumference(self):
    return 2 * math.pi * self.radius

circle = Circle(3)
print("Area of Circle : ",circle.area())
print("Circumference of Circle : ",circle.circumference())