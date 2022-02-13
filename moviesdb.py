import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="daph11*sql",
  database="moviedb"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM favmov WHERE actor ='Andrew Garfield'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
