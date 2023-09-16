from prettytable import PrettyTable
import pyperclip
from utils import writeJsonFile, loadJsonFile, interToFrench, frenchToInter

def choice():
    question = """
+------------------------------------------+
| Que voulez vous faire ?                  |
|    0 - Quitter                           |
|    1 - Ecrire dans le répertoire         |
|    2 - Chercher dans le répertoire       |
|    3 - Afficher le répertoire            |
|    4 - Copier le numéro de téléphone     |
+------------------------------------------+
>> """
    answer =  input(question)
    while answer not in ["0", "1", "2", "3", "4"]:
        print("/!\\ Vous ne pouvez que écrire 0, 1, 2, 3 ou 4.")
        answer = input(">> ")
    return int(answer)

def write():
    name = input("Entrez le nom (ex: John)\n>> ")
    num = input("Entrez le numéro (ex: +33612345678)\n>> ")

    database = loadJsonFile()

    # Get the key for the new item of the dictionnary
    i = -1
    if len(database.keys()) != 0:
        i = int(list(database.keys())[-1])

    database[str(i+1)] = [name, num] # adds the new element to the dictionnary
    writeJsonFile(database)

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

    # Checks if the phone number is associated with a name
    if answer == "1":
        query = input("Entrez un numéro de téléphone (Ex: +33612345678)\n>> ")
        identifier = 1
    elif answer == "2":
        query = input("Entrez un nom (Ex: Didier)\n>> ")
        identifier = 0
    else:
        return False
    
    database = loadJsonFile()

    if elements := [
            # Creates a list of tuples containing the name and phone number ONLY if the following condition is True
            (database[key][0], database[key][1]) for key in database.keys()
            # If `query` matches a name or a phone number (according to the identifier)
            if query.lower() in database[key][identifier].lower()
        ]:
        # Displays the table with the names and phone numbers
        table = PrettyTable(align="l")
        table.field_names = ["Nom", "Numéro de tél."]
        for element in elements:
            table.add_row([element[0], element[1]])
        print(table)
    else:
        print("Aucun résultat trouvé.")
    return True

def display():
    table = PrettyTable(align="l")
    table.field_names = ["ID", "Nom", "Numéro de tél."]
    database = loadJsonFile()
    for key in database.keys():
        table.add_row([key, database[key][0], interToFrench(database[key][1], True)])
    print(table)

def copy():
    name = input("De quelle personne voulez-vous copier le numéro de téléphone ?\n>> ")
    database = loadJsonFile()
    for key in database.keys():
        if name == database[key][0]:
            pyperclip.copy(frenchToInter(database[key][1]))
            print(f"Le numéro de téléphone de {name} ({database[key][1]}) a été copié !")
            return None
    print(f"Aucun numéro n'a été trouvé pour {name}")

if __name__ == "__main__":
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
        elif user_choice == 4:
            copy()
