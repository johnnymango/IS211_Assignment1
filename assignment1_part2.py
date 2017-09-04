#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 - Part 2"""

class Book:
    """A Book Class"""
    def __init__(self, author, title):
        """A constructor function for the book class to set attributes.

        Args:
            author (str): the author of the book
            title (str): the title of the book

        Attributes:
            author (str): the author of the book
            title (str): the title of the book
        """
        self.author = author
        self.title = title

    def display(self):
        """ Function displays the formatted string containing author and title of book.

        Args:
            author (str):  the author of the book.
            title (str): the title of the book.

        Returns:
            A formatted string containing the author and book.

        Examples:
            >>>book1.display()
            Of Mice and Men, written by John Steinbeck.
        """
        print "{}, written by {}.".format(self.title, self.author)


book1 = Book("John Steinbeck", "Of Mice and Men")
book2 = Book("Harper Lee", "To Kill a Mockingbird")

book1.display()
book2.display()


