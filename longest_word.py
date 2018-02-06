#### Find the longest word in the given string

str = input("Enter the string : ").split()

longest_word=""

for word in str:
  if len(word) > len(longest_word):
    longest_word = word

print(longest_word)
