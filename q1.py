class Author:
    def __init__(self,name):
        self.name = name

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
author1=Author("wdfujm")
book = Book("Percy Jackson",author1)

print(f"{book.title}{book.author.name}")








        