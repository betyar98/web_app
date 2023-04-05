FILEPATH = "feladatok.txt"


def get_todos(filepath=FILEPATH):
    """Beolvassa a dokumentumot és visszaad egy listát a feladatokról."""
    with open(filepath, "r") as file_local:
        feladatok_local = file_local.readlines()
    return feladatok_local


def write_todos(feladatok_arg, filepath=FILEPATH):
    """ Kiírja a feladatok listáját egy dokumentumba."""
    with open(filepath, "w") as file_local:
        file_local.writelines(feladatok_arg)


# ez csak akkor fut le ha az program neve main pl. ha importáljuk másik fájlba akkor már nem az a neve
if __name__ == "__main__":
    print("hello from functions!")
    print(get_todos())
