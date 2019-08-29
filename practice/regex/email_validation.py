import re
N=int(input())
mail = []
for i in range(N):
    email = input()
    output = email.split()[1].replace('<', '').replace('>', '')
    if re.match(r'[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$', output):
        mail.append(email)


for m in mail:
    print(m)

