from __future__ import print_function
from mysql import connector
import pandas as pd


print("creating indices...")

mydb = connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="olapdb"
)

mycursor = mydb.cursor()

# ALTER TABLE  `table` DROP INDEX  `NameIndex`
columns = ["continent" , "country" , "gender" , "agegroup" , "sport"]

indices_num = 0

i=0
while(i != len(columns)):
    sql1 = "CREATE INDEX %s ON london12(%s) USING BTREE" % (columns[i] + "_index", columns[i])
    mycursor.execute(sql1)
    indices_num = indices_num+1
    i = i+1

i=0
while(i != len(columns)-1):
    j = i+1
    while(j != len(columns)):
        sql1 = "CREATE INDEX %s ON london12(%s) USING BTREE" % (columns[i]+"_"+columns[j] + "_index", columns[i]+","+columns[j])
        mycursor.execute(sql1)
        indices_num = indices_num+1
        j = j + 1
    i = i+1

i=0
while(i !=len(columns)-2):
    j=i+1
    while(j != len(columns)-1):
        z=j+1
        while(z != len(columns)):
            sql1 = "CREATE INDEX %s ON london12(%s) USING BTREE" % (columns[i] + "_" + columns[j]+"_"+columns[z] + "_index", columns[i] + "," + columns[j]+","+columns[z])
            mycursor.execute(sql1)
            indices_num = indices_num+1
            z=z+1
        j=j+1
    i=i+1

i=0
while(i !=len(columns)-3):
    j=i+1
    while(j != len(columns)-2):
        z=j+1
        while(z != len(columns)-1):
            k = z+1
            while(k != len(columns)):
                sql1 = "CREATE INDEX %s ON london12(%s) USING BTREE" % (columns[i] + "_" + columns[j]+"_"+columns[z]+"_"+columns[k] + "_index", columns[i] + "," + columns[j]+","+columns[z]+","+columns[k])
                mycursor.execute(sql1)
                indices_num = indices_num + 1
                k = k+1
            z=z+1
        j=j+1
    i=i+1

i=0
while(i !=len(columns)-4):
    j=i+1
    while(j != len(columns)-3):
        z=j+1
        while(z != len(columns)-2):
            k = z+1
            while(k != len(columns)-1):
                e = k+1
                while(e!=len(columns)):
                    sql1 = "CREATE INDEX %s ON london12(%s) USING BTREE" % (columns[i] + "_" + columns[j]+"_"+columns[z]+"_"+columns[k]+"_"+columns[e] + "_index", columns[i] + "," + columns[j]+","+columns[z]+","+columns[k]+","+columns[e])
                    mycursor.execute(sql1)
                    indices_num = indices_num + 1
                    e=e+1
                k=k+1
            z=z+1
        j=j+1
    i=i+1

sql1 = "CREATE INDEX %s ON london12(%s) USING BTREE" % ("sport" + "_" + "agegroup"+"_"+"gender"+"_"+"country"+"_"+"continent" + "_index", "sport" + "," + "agegroup"+","+"gender"+","+"country"+","+"continent")
mycursor.execute(sql1)
indices_num = indices_num + 1


print("number of indices: %d"%(indices_num))
mydb.commit()
print("done. file data.sqlite created")
