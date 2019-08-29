class Balance:
  def __init__(self):
    self.balance = 0

  def deposit(self, money):
    self.balance += money

  def withdraw(self, money):
    self.balance -= money

  def total_balance(self):
    if self.balance < 0.0:
      print("Insufficient balance")
    else:
      print("Total balance : {}".format(self.balance))

BAL = Balance()
BAL.deposit(500)
BAL.withdraw(600)
BAL.total_balance()