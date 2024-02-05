import mysql.connector

class Animal:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Animal ajouté avec succès!")
    
    def read_animal(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            for animal in result:
                print(animal)
        else:
            print("Aucun animal trouvé.")

    def update_animal(self, id_cage, nouveau_nom_animal, id):
        query = "UPDATE animal SET nom = %s, id_cage = %s WHERE id = %s"
        values = (nouveau_nom_animal, id_cage, id)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Animal mis à jour avec succès!")

    def delete_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s "
        values = (animal_id,)
        self.cursor.execute(query,values)
        self.mydb.commit()
        print("animal supprimé")
    
    def close_connection(self):
            self.cursor.close()
            self.mydb.close()


class Cage:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()
    

    def ajouter_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Cage ajouté avec succès!")

    def read_cage(self):
        query = "SELECT * FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            for cage in result:
                print(cage)
        else:
            print("Aucune cage trouvé.")

    def update_cage(self, id, nouvelle_superficie, nouvelle_capacite_max):
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
        values = (nouvelle_superficie, nouvelle_capacite_max, id)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Cage mise à jour avec succès!")
    
    def delete_cage(self, id):
        query = "DELETE FROM cage WHERE id = %s "
        values = (id,)
        self.cursor.execute(query,values)
        self.mydb.commit()
        print("cage supprimé")
    
    def close_connection(self):
            self.cursor.close()
            self.mydb.close()

class Directeur:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def animaux_dans_cage(self):
        query = "SELECT animal.nom, animal.race, cage.id AS cage FROM animal JOIN cage ON cage.id = animal.id_cage"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            for animaux in result:
                print(animaux)
        else:
            print("Aucune cage trouvé.")

    def superficie_total_cages(self):
        query = "SELECT SUM(superficie) AS TotalSuperficie FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            for superficie in result:
                print(superficie)
        else:
            print('Rien trouvé')

    def close_connection(self):
            self.cursor.close()
            self.mydb.close()

host = "localhost"
user = "root"
password = "Ultrasmars1379!"
database = "zoo"

mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

print("Les cages du zoo :")
gerer_cage = Cage(host, user, password, database)
gerer_cage.read_cage()

print('Les animaux du zoo sont : ')
gerer_animaux = Animal(host, user, password, database)
gerer_animaux.read_animal()

print('Les animaux des cages :')
gerer_zoo = Directeur(host, user, password, database)
gerer_zoo.animaux_dans_cage()

print('La superficie total des cages est : ')
gerer_zoo.superficie_total_cages()

gerer_animaux.close_connection()
gerer_cage.close_connection()
gerer_zoo.close_connection()




