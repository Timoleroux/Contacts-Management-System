import os, json

DIR_PATH = os.path.abspath(os.getcwd()) # path of the main directory
DB_PATH = DIR_PATH + "\\data\\repertoire.json"

def loadJsonFile():
    """Loads the json file and returns it's content

    Returns:
        dict: content of the json file
    """
    if os.stat(DB_PATH).st_size == 0:
        raise(FileExistsError(f"The file '{DB_PATH}' can't be empty."))
    with open(DB_PATH, "r") as f:
        db = json.load(f)
    return db

def writeJsonFile(new_content):
    """Overrides the json file with `new_content`.

    Args:
        new_content (dict): new content of the json file
    """
    with open(DB_PATH, "w") as f:
        json.dump(new_content, f, indent=4)

def formatDict(dictionary):
    """Resctructures the database so that the list of keys always starts with 0 and increments by 1 with each key.

    Args:
        dictionary (dict): Input dictionary (ex: `{"2"="value0", "6"="value1"}`)

    Returns:
        dict: Ouput dictionnary (ex: `{"0"="value0", "1"="value1"}`)
    """
    sorted_keys = sorted(map(int, dictionary.keys()))
    return {
        str(counter): dictionary[str(key)] for counter, key in enumerate(sorted_keys)
    }

def interToFrench(num, spaces=False):
    """Converts a French phone number to international format.

    Args:
        num (str): phone number to be converted
        spaces (bool, optional): indicates whether the converted phone number is separated by spaces. Defaults to False.

    Returns:
        str: converted phone number or `num` if it couldn't be converted
    """
    if num[:3] != "+33" or len(num) != 12 or not num[2:].isdigit():
        return num
    if spaces:
        return f"0{num[3]} {num[4:6]} {num[6:8]} {num[8:10]} {num[10:12]}"
    else:
        return f"0{num[3:]}"

def frenchToInter(num: str):
    """Converts a international phone number to French format.

    Args:
        phone_number (str): phone number to be converted

    Returns:
        str: converted phone number or `num` if it couldn't be converted
    """
    num = num.replace(" ", "")
    if num[0] == "0" and len(num) == 10 and num[1:].isdigit():
        return f"+33{num[1:]}"
    return num