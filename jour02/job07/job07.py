import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()
        
    def creation_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Employé ajouté avec succès!")

    def lire_employe(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            for employe in result:
                print(employe)
        else:
            print("Aucun employé trouvé.")
    
    def maj_employe_salaire(self, employe_id, nouveau_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (nouveau_salaire, employe_id)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Salaire de l'employé mis à jour avec succès!")

    def supprimer_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Employé supprimé avec succès!")

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

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

gerer_employe = Employe(host, user, password, database)
gerer_employe.supprimer_employe(5)
gerer_employe.maj_employe_salaire(3, 5000)
gerer_employe.lire_employe()



query = "SELECT nom, prenom FROM employe WHERE salaire > 3000"
cursor = mydb.cursor()
cursor.execute(query)
resultat = cursor.fetchall()

if resultat:
    print("Les employés gagnant plus de 3000€ sont :")
    for employe in resultat:
        print(f'{employe}')
else:
    print("Aucun employé gagne plus de 3000€")

query = "SELECT employe.nom, employe.prenom, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id"
cursor = mydb.cursor()
cursor.execute(query)
resultat = cursor.fetchall()

if resultat:
    print('le role des personnes est :')
    for personne in resultat:
        print(f'{personne}')

cursor.close()
mydb.close()