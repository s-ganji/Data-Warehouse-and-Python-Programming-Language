from __future__ import print_function
from mysql import connector
import pandas as pd

print("preparing data...")

mydb = connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="olapdb"
)

df = pd.read_csv('london12.csv')
df2 = pd.read_csv('countries_by_continent.csv')


# data cleaning and integration
df["Country"] = df["Country"].replace("People's Republic of China","China")
df["Country"] = df["Country"].replace("Islamic Republic of Iran","Iran")
df["Country"] = df["Country"].replace("Syrian Arab Republic","Syria")
df["Country"] = df["Country"].replace("Republic of Moldova","Moldova")
df["Country"] = df["Country"].replace("Myanmar","Burma (Myanmar)")
df["Country"] = df["Country"].replace("Former Yugoslav Republic of Macedonia","Macedonia")
df["Country"] = df["Country"].replace("American Samoa","Samoa")
df["Country"] = df["Country"].replace("Federated States of Micronesia","Micronesia")
df["Country"] = df["Country"].replace("United Republic of Tanzania","Tanzania")
df["Country"] = df["Country"].replace("Brunei Darussalam","Brunei")
df["Country"] = df["Country"].replace("Burkina Faso","Burkina")

data_file = pd.merge(df , df2 , left_on='Country', right_on='Country' , how = 'left').fillna("unknown")


mycursor = mydb.cursor()

# checking if there was any record in the table, if it was we should delete them first and then add new records
mycursor.execute("SELECT count(*) FROM london12")
myresult = mycursor.fetchall()
if(myresult !=0):
    mycursor.execute("DELETE FROM london12 ")
    mycursor.execute("ALTER TABLE london12 AUTO_INCREMENT = 1")


for index, row in data_file.iterrows():

    if( row["Age"] <20 ):
        ageGroup = "A"
    elif( row["Age"] >=20 and row["Age"] <25):
        ageGroup = "B"
    elif(row["Age"] >=25 and row["Age"] <30 ):
        ageGroup = "C"
    else:
        ageGroup = "D"

    sql1 = "INSERT INTO london12(continent, country, gender, agegroup, sport, gold, silver, bronze) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (row["Continent"], row["Country"], row["Gender"], ageGroup,
           row["Sport"], row["Gold Medals"], row["Silver Medals"], row["Bronze Medals"])
    mycursor.execute(sql1, val)


mydb.commit()
print("done. file data.sqlite created")



