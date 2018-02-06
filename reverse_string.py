str=input("Enter the string : ")

new_string = ""

count = len(str)

while count > 0:
  new_string += str[count -1]
  count -= 1

print(new_string)

### there is another method to do string[-1::-1]