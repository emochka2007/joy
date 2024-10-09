import sys
def read_from_file():
    with open(sys.argv[1], encoding="utf-8") as file:
        return file.read()
    