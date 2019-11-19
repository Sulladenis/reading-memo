import db

data = {'python book': ['10.09.2019', 200, 50, False]}

def test_insert_and_get_db(data):
    db.insert(data)
    result = db.get_db()
    return result == data


if __name__ == '__main__':
    print(f' Test insert dict in to db, and get dict from db is {test_insert_and_get_db(data)}')
    print(f'List books = {db.list_book()}')
