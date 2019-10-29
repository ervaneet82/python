def is_valid_pin(pin):
	return len(pin) in [4, 6] and pin.isdigit()

print(is_valid_pin("45"))
print(is_valid_pin("12345"))