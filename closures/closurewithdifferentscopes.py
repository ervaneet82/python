def create_adders():
  adders=[]
  for n in range(1,4):
    adders.append(lambda x,y=n: x + y)
  return adders

adders = create_adders()
print(adders)
print(adders[0](10))