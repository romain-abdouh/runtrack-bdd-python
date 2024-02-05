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

query = "SELECT SUM(superficie) AS total_superficie FROM etage"
cursor = mydb.cursor()
cursor.execute(query)

total_superficie = cursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {total_superficie} m2")

cursor.close()
mydb.close()