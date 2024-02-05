import mysql.connector

host = "localhost"
user = "root"
password = "Ultrasmars1379!"
database = "LaPlateforme"

# Connexion à la base de données

mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

print("Connecté à la base de données")

        # Récupérer l'ensemble des étudiants
query = "SELECT * FROM etudiant"
cursor = mydb.cursor()
cursor.execute(query)

for etudiant in cursor.fetchall():
        print(etudiant)

cursor.close()
mydb.close()


