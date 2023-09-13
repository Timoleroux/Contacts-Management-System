from prettytable import PrettyTable

database = {1:["Bernard", "+33612345678"], 2:["François", "+33687654321"], 3:["Elise", "+33669696969"]}

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
    try:
        answer = int(answer) # Convertir 'answer' au bon type
        if not(0 <= answer <=4): # Vérifie que 'answer' est compris entre 0 et 4
            raise TypeError
    except Exception:
        exit("/!\\ Vous ne pouvez que écrire 0, 1, 2, 3 ou 4")
    return answer

def write():
    """
    Aide pour Adrien : n'hésite pas à recréer un fichier 'test' avec 
    uniquement la fonction write et 'database' pour te simplifier la tache
    
    Etapes de la fonction :
        -> Demander à l'utilisateur un nom et un numéro de téléphone
        -> Chercher le dernier indice de 'database' (3)
        -> Ajouter le nom et le numéro à l'indice correspondant (4)
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
    try:
        answer = int(answer)
        if answer not in [0, 1, 2]:
            raise TypeError
    except Exception:
        exit("/!\\ Vous ne pouvez que écrire 0, 1 ou 2")
    
    if answer == 1:
        # Vérifie si le numéro recherché est associé à un nom
        num = input("Entrez le numéro de téléphone (Ex: +33612345678)\n    >> ")
        for key in database.keys():
            if database[key][1] == num:
                print(f"Le numéro de téléphone {num} appartient à {database[key][0]}.")
                return database[key][0]
        print(f"Le numéro {num} n'est pas attribué.")
    elif answer == 2:
        # Vérifie si le nom recherché est associé à un numéro
        name = input("Entrez le prénom (Ex: Didier)\n    >> ")
        for key in database.keys():
            if database[key][0].lower() == name.lower():
                print(f"Le numéro de téléphone de {name} est {database[key][1]}.")
                return database[key][1]
        print(f"Aucun numéro trouvé pour {name}.")

def display():
    table = PrettyTable(align="l")
    table.field_names = ["Nom", "Numéro de tél."]
    for key in database.keys():
        table.add_row([database[key][0], database[key][1]])
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
            find()
        elif user_choice == 3:
            display()

    print("Programme arrêté.")

if __name__ == "__main__":
    main()
