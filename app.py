from prettytable import PrettyTable
import json, os

CUR_PATH = os.path.abspath(os.getcwd()) # Path of the current directory
DB_PATH = CUR_PATH + "\\repertoire.json" # Path of the database
# Load 'repertoire.json' in the variable 'database'
with open(DB_PATH, "r") as f: 
    database = json.load(f)

# Base de donnée pour les tests :
database = {"1":["Bernard", "+33612345678"], "2":["François", "+33687654321"], "3":["Elise", "+33669696969"]}

def choice():
    question = """
+------------------------------------------+
| Que voulez vous faire ?                  |
|    0 - Quitter                           |
|    1 - Ecrire dans le répertoire         |
|    2 - Chercher dans le répertoire       |
|    3 - Afficher le répertoire            |
|    4 - Convertir au format international |
+------------------------------------------+
>> """
    answer =  input(question)
    while answer not in ["0", "1", "2", "3", "4"]:
        print("/!\\ Vous ne pouvez que écrire 0, 1, 2, 3 ou 4.")
        answer = input(">> ")
    return int(answer)

def write():
    """
    Aide pour Adrien : n'hésite pas à recréer un fichier 'test' avec 
    uniquement la fonction write et 'database' pour te simplifier la tache
    
    Etapes de la fonction :
        -> Demander à l'utilisateur un nom et un numéro de téléphone (stocké dans des variables)
        -> Chercher le dernier indice de 'database' (attention aux types (int VS str))
        -> Ajouter le nom et le numéro dans le dictionnaire à l'indice correspondant (exemple : "4":["Jonny", "+3321436587"]) )
    """
    cles = list(database.keys())
    cles[-1]
    cles_1=cles[-1]+1
    print(cles_1)
    question= input("ajouter le prenom")
    question2=input("ajouter le numero")

def find():
    question = """
+------------------------------------+
| Comment voulez-vous chercher ?     |
|    1 - Avec un numéro de téléphone |
|    2 - Avec un prénom              |
|                                    |
| Retour au menu : 0                 |
+------------------------------------+
>> """
    answer =  input(question)
    while answer not in ["0", "1", "2"]:
        print("/!\\ Vous ne pouvez que écrire 0, 1 ou 2.")
        answer = input(">> ")
        if answer == "0":
            return False

    # Vérifie si le numéro recherché est associé à un nom
    if answer == "1":
        look_for = input("Entrez un numéro de téléphone (Ex: +33612345678)\n>> ")
        identifier = 1
    elif answer == "2":
        look_for = input("Entrez un nom (Ex: Didier)\n>> ")
        identifier = 0
    else:
        return False

    if elements := [ # Crée une liste contenant noms & numéros si 'look_for' est contenu dans un numéro ou un nom
            (database[key][0], database[key][1])
            for key in database.keys()
            if look_for.lower() in database[key][identifier].lower()
        ]:
        # Affiche le tableau avec le(s) numéro(s)
        table = PrettyTable(align="l")
        table.field_names = ["Nom", "Numéro de tél."]
        for element in elements:
            table.add_row([element[0], element[1]])
        print(table)
    else:
        # Si la liste est vide :
        print("Aucun résultat trouvé.")
    return True

def display():
    table = PrettyTable(align="l")
    table.field_names = ["ID", "Nom", "Numéro de tél."]
    for key in database.keys():
        table.add_row([key, database[key][0], database[key][1]])
    print(table)

def international():
    pass

def main():
    user_choice = -1
    while user_choice != 0:
        user_choice = choice()
        if user_choice == 1:
            write()
        elif user_choice == 2:
            loop = True
            while loop:
                loop = find()
        elif user_choice == 3:
            display()

if __name__ == "__main__":
    main()
