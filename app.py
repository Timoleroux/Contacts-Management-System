database = {"001":["Bernard", "0612345678"], "002":["François", "0687654321"], "003":["Elise", "0669696969"]}

def choice():
    question = """
    --------------------------------------
    | Que voulez vous faire ?            |
    |    0 - Quitter                     |
    |    1 - Ecrire dans le répertoire   |
    |    2 - Chercher dans le répertoire |
    --------------------------------------
    >> """
    return int(input(question))

def write():
    cles = list(database.keys())
    cles[-1]
    cles_1=cles[-1]+1
    print(cles_1)
    question= input("ajouter le prenom")
    question2=input("ajouter le numero")

def find():
    pass

def main():
    print(choice())

if __name__ == "__main__":
    main()
