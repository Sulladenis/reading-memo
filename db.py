import json


def insert(data: dict) -> None:
    with open('book.json', 'w') as file:
        json.dump(data, file)

def get_db():
    with open('book.json') as file:
        data = json.load(file)
    return data

def list_book():
    data = get_db()
    return [x[1] for x in data]
