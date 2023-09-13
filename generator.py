import names, string, json, os
from random import randint, choice

CUR_PATH = f"{os.path.abspath(os.getcwd())}\\"

def databaseGenerator(db_name, nbr):
    print(f"WARNING: This function will erase all the content of the file '{db_name}' !")
    if input("Do you want to continue ? (Y/N) ") not in ["y", "Y"]:
        exit("Function abvorted")
    data = {}
    for i in range(nbr):
        name = f"{names.get_first_name()} {choice(string.ascii_uppercase)}."
        num = "+336"
        for _ in range(8):
            num += str(randint(0, 9))
        data[str(i)] = [name, num]
    
    with open(CUR_PATH + db_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print("The database was successfully generated.")

databaseGenerator("repertoire.json", 1000)
