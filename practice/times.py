import string
from random import *

min_char = 8
max_char = 10


allchar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","#", "*", "£", "$", "+", "-", "."]

generate = "".join(choice(allchar) for _ in range(randint(min_char, max_char)))

print(generate)