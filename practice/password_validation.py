class Email:
	def __init__(self, password):
		self.password = password

	@property
	def password_length(self):
		return self._length

	@password_length.setter
	def password_length(self,length):
		if len(self.password) < int(length):
			raise ValueError("Password is not allowed less than 8 characters")

email = Email("vaneet")
email.password_length = 8