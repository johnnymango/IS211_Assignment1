#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 - Part 1"""

def listDivide(numbers=[], divide=2):
    """ The function returns the number of elements in the numbers list that
    are divisible by divide.

    Args:
        numbers(list): a list of numbers
        divide (int, default=2):  the number by which numbers in the list
        will be divided by.

    Returns:
        count(int): the count of numbers divisible by divide where remainder
        = 0.

    Example:
        >>> listDivide([2, 4, 6, 8, 10])
        5
    """
    count=0
    for i in numbers:
        remainder = i % divide
        if remainder == 0:
            count=count+1
    return count

class ListDivideException(Exception):
    """A custom Exception Class to be raised when errors are created."""
    pass

def testListDivide():
    """A function to test the listDivide function and raise an exception when
    the test fails.

    Args: None

    Returns:  An exception when the expected result from the test fails.

    Example:
    Traceback (most recent call last):
    File "C:/Users/Johnny/PyCharmProjects/IS211_Assignment1/assignment1_part1.py", line 62, in <module>
    testListDivide()
    File "C:/Users/Johnny/PyCharmProjects/IS211_Assignment1/assignment1_part1.py", line 51, in testListDivide
    raise ListDivideException("Test 2 Error")
    __main__.ListDivideException: Test 2 Error
    """
    test1 = listDivide([1, 2, 3, 4, 5])
    if test1 != 2:
        raise ListDivideException("Test 1 Error")
    test2 = listDivide([2,4,6,8,10])
    if test2 != 5:
        raise ListDivideException("Test 2 Error")
    test3 = listDivide([30, 54, 63, 98, 100], divide=10)
    if test3 !=2:
        raise ListDivideException("Test 3 Error")
    test4 = listDivide([])
    if test4 != 0:
        raise ListDivideException ("Test 4 Error")
    test5 = listDivide([1,2,3,4,5], 1)
    if test5 != 5:
        raise ListDivideException ("Test 5 Error")

testListDivide()