import mysql.connector

host = 'Localhost'
user = 'root'
password = 'Ultrasmars1379!'
database = 'LaPlateforme'

mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

print ('connection BDD')

query = 'SELECT nom, capacite FROM salle'
cursor = mydb.cursor()
cursor.execute(query)

for salle in cursor.fetchall():
    print(salle)

cursor.close()
mydb.close()




