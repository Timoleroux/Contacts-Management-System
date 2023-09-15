from names import get_first_name
from string import ascii_uppercase
from random import randint, choice
from ressources import DB_PATH, writeJsonFile


def databaseGenerator(database_path: str, iteration: int):
    """Generates a json file with random names and phone numbers. Example: `{"3": ["Richard V.", "+33664699560"]})`.

    Args:
        db_name (str): name of the database (ex: `database.json`)
        iteration (int): number of items generated
    """
    # Displays a confimation message
    print(f"WARNING: This function will erase all the content of '{database_path}' !")
    if input("Do you want to continue ? (Y/N) ") not in ["y", "Y"]:
        exit("Operation cancelled")
    data = {}
    for i in range(iteration):
        # Generates a random name
        name = f"{get_first_name()} {choice(ascii_uppercase)}."
        phone_number = "+336"
        # Generates a random phone number
        for _ in range(8):
            phone_number += str(randint(0, 9))
        # Adds a new element in 'data'
        data[str(i)] = [name, phone_number]

    # Uptades the json file
    writeJsonFile(data)
    print("The database was successfully generated.")

if __name__ == '__main__':
    databaseGenerator(DB_PATH, 50)