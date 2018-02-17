employee={
  "01" : {'name':'Vaneet','telephone':'9650230061'},
  "02" : {'name' : 'Suman','telephone':'9650230049'}
}


for id in employee:
  for details in employee[id]:
    if details == 'telephone':
      print(id ,":", employee[id][details])