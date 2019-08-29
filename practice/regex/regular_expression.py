import re

email = 'username@hackerrank.com'

# m = re.match(r'(\w+)@(\w+).(\w+)',email)
#
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
#
# print(m.groups())


m = re.match(r'(?P<user>\w+)@(?P<website>\w+).(?P<extension>\w+)',email)

#print(m.groupdict())

### print first repeating char in string
import re

# m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
# print(m.group(1) if m else -1)

## print vowels in string

s = "matchasinglecharacternotpresent"

s=input()
t=re.findall(r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])',s,re.I)
if len(t)!=0:
    for i in t:
        print(i)
else:
    print("-1")


