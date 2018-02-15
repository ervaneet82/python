vowels = {'a' : 0 , 'e' : 0 , 'i' : 0 , 'o' : 0 , 'u' : 0 }

string=input("Enter the string : ")

count = 0

for word in string:
  for key,value in vowels.items():
    if key in word:
      vowels[key] = value + 1
print(vowels)
