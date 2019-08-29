import re
def verify_substrs(main_txt, head, body, tail):
	return "My head, body, and tail." if main_txt.startswith(head) \
	                                     and body in main_txt \
	                                     and main_txt.endswith(
		tail) else "Incomplete."
print(verify_substrs("Centipede", "Cent", "tip", "pede"))