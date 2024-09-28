def read_from_file(path: str):
    with open(path, encoding="utf-8") as file:
        return file.read()
factorial_text = read_from_file("factorial.joy")