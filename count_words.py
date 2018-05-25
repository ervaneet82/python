string=input("Enter the string : ")

count = 1

for str in string:
  if str == " ":
    count +=1

print("Number of words in string : {}".format(count))