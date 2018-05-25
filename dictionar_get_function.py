import sys
fruit= {
  "orange" : "a sweet sour",
  "apple" : "good for health",
  "lemon" : "sour, green citrus",
  "green" : "a green , sweet"
}


while True:
  dict_key = input("Enter the fruit : ")
  if dict_key == "quit":
    sys.exit(0)
  print(fruit.get(dict_key,"We don't have " + dict_key))

