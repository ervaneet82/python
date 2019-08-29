#!/usr/bin/python
import csv
import difflib
import MySQLdb


db1 = MySQLdb.connect(host="localhost",  # your host
                      user="root",       # username
                      passwd="",     # password
                      db="upen")   # name of the database

# Create a Cursor object to execute queries.
cur1 = db1.cursor()

# Select data from table using SQL query.
cur1.execute("SELECT column_name FROM information_schema.columns WHERE  table_name = 'person4' AND table_schema ='upen'")
result1=cur1.fetchall()
cur1.close()
with open("table1.csv",  "w") as f:
  writer = csv.writer(f)
  for row in result1:
    writer.writerow(row)


db2 = MySQLdb.connect(host="localhost",  # your host
                      user="root",       # username
                      passwd="",     # password
                      db="vaneet")   # name of the database

# Create a Cursor object to execute queries.
cur2 = db2.cursor()

# Select data from table using SQL query.
cur2.execute("SELECT column_name FROM information_schema.columns WHERE  table_name = 'person4' AND table_schema ='vaneet'")
result2 = cur2.fetchall()
cur2.close()
with open("table2.csv", "w") as f1:
  writer = csv.writer(f1)
  for row in result2:
    writer.writerow(row)


with open('table1.csv') as text1, open('table2.csv') as text2:
    diff = difflib.ndiff(text1.readlines(), text2.readlines())
with open('diff.txt', 'w') as result:
    for line in diff:
        result.write(line)