import db


class Book:

    def __init__(self, name=None, pages=None, start_date=None):
        self.name = name
        self.start_date = start_date
        self.pages = pages
        self.progress = 0
        self.end_date = None

    def get(self, name):
        data = db.get_db()
        self.name = name = name.capitalize()
        self.start_date = data[name][0]
        self.pages = data[name][1]
        self.progress = data[name][2]
        self.end_date = data[name][3]

    def save(self):
        data = db.get_db()
        data.update({
            self.name.capitalize():
                [self.start_date, self.pages, self.progress, self.end_date]
        })
        db.insert(data)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
