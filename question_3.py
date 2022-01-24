from __future__ import print_function
from cubes import Workspace, Cell, PointCut
from mysql import connector
import matplotlib.pyplot as plt
import numpy as np

mydb = connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="olapdb"
)

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="mysql://root@localhost/olapdb")
workspace.import_model("model.json")

# 2. Get a browser
browser = workspace.browser("london12")

mycursor = mydb.cursor()

# 4_a
country1 = [];
count = [];

sql = "SELECT country,COUNT(DISTINCT id) FROM london12 group by country order by COUNT(DISTINCT id) desc LIMIT 10 "
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
   country1.append(row[0])
   count.append(row[1])

y_positions = range(len(country1))

plt.bar(y_positions,count)
plt.xticks(y_positions,country1,fontsize=5,rotation = 30)
plt.ylabel("Number of participants")
plt.xlabel("country")
plt.title("Column chart of the top 10 countries in terms of number of participants:(4_a)")
plt.show()

# 4_b
continent = [];
medals = [];

sql = "SELECT continent,SUM(gold),SUM(silver),SUM(bronze) FROM london12 group by continent  "
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
   continent.append(row[0])
   medals.append(row[1]+row[2]+row[3])

plt.pie(medals, labels=continent , autopct="%.2f")
plt.show()

# 4_c
gold_ratio = [];
silver_ratio = [];
bronze_ratio = [];
country = [];


sql = "SELECT country,(SUM(gold)+SUM(silver)+SUM(bronze))/COUNT(DISTINCT id) as ratio,COUNT(DISTINCT id),SUM(gold)/COUNT(DISTINCT id),SUM(silver)/COUNT(DISTINCT id),SUM(bronze)/COUNT(DISTINCT id)  FROM london12  group by country  having COUNT(DISTINCT id) >=30 order by ratio desc LIMIT 10 "
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    country.append(row[0])
    gold_ratio.append(row[3])
    silver_ratio.append(row[4])
    bronze_ratio.append(row[5])

n_group = len(country)
fig, ax = plt.subplots()
index = np.arange(n_group)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index,gold_ratio,bar_width,alpha=opacity , color='b',label='gold')
rects2 = plt.bar(index + bar_width, silver_ratio, bar_width, alpha=opacity , color='g',label='silver')
rects3 = plt.bar(index + bar_width+bar_width, bronze_ratio, bar_width, alpha=opacity , color='r',label='bronze')
plt.xlabel("country")
plt.ylabel("ratio")
plt.title("third chart")
plt.xticks(index + bar_width , country,fontsize=5,rotation = 30)
plt.legend()
plt.show()