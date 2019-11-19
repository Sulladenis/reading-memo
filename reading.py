import csv


class Book:

    def __init__(self, name = None, pages = None, start_date=None):
        self.name = name
        self.pages = pages
        self.start_date = start_date
        self.end_date = None
        self.progress = 0

    def record(self):
        with open('book.txt', 'a') as note:
            note.write(
                f'{self.name},{self.pages},{self.start_date, },'
                f'{self.end_date},{self.progress}')


    def set(self, name, pages, start_date):
        self.name = name
        self.pages = pages
        self.start_date = start_date
        self.end_date = None
        self.progress = 0

        with open('books.csv', 'a', newline='') as csvfile:
            fieldnames = ['name', 'pages', 'start_date', 'end_date', 'progress']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(
                {'name': self.name, 'pages': self.pages,'progress': self.progress,
                 'start_date': self.start_date, 'end_date': self.end_date}
            )


    def __str__(self):
        return self.name


class Note:

    def __init__(self, data, book, number_page):
        self.data = data
        self.book = book
        self.number_page = number_page

    def set_note(self):
        if self.number_page < self.book.pages:
            with open('note.txt', 'a') as note:
                note.write(f'{self.data},{self.book},{self.number_page}')
                self.book.progress = self.number_page
        else:
            print('the book does not have so many pages!')




