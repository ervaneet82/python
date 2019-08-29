class Celcius:
  def __init__(self,temperature=0):
    """Initialize the tempature"""
    self._temperature = temperature

  def to_fahrenheit(self):
    return (self.temperature * 1.8) + 32

  @property
  def temperature(self):
    print("Getting Temperature : ",end='')
    return self._temperature

  @temperature.setter
  def temperature(self,value):
    if value < -273:
      raise ValueError("Temperature below -273 is not possible")
    print("Setting Value : " , value)
    self._temperature= value

c = Celcius()
c.temperature=30
print(c.to_fahrenheit())