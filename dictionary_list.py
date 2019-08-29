log_result={'start':[],'end':[]}


with open("logs.txt",'r') as myfile:
  for line in myfile:
    for key in log_result.keys():
      if key in line.rstrip():
        log_result[key].append(line.split(':')[1].rstrip())

print(log_result)
