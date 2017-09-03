#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print "{}, written by {}.".format(self.title, self.author)


book1 = Book("John Steinbeck", "Of Mice and Men")
book2 = Book("Harper Lee", "To Kill a Mockingbird")

book1.display()
book2.display()


