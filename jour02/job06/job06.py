import mysql.connector

host = 'Localhost'
user = 'root'
password = 'Ultrasmars1379!'
database = 'LaPlateforme'

mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

print ("Connection BDD")

query = "SELECT SUM(capacite) AS total_capacite FROM salle"
cursor = mydb.cursor()
cursor.execute(query)

total_capacite = cursor.fetchone()[0]
print(f"La capacité de toute les salles est de : {total_capacite}")

cursor.close()
mydb.close()