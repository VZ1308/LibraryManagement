class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}"
