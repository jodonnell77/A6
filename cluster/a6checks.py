"""
Helper functions for k-Means clustering

This file contains the functions for enforcing preconditions for k-means clustering.
We have written the first for you.  You will probably want to write others.

John O'Donnell (jro79) and Anthony Nguyen (an523)
4/11/19 asdapsdkaspodkasdkapsdkaop
"""
import math
import random
import numpy


def is_point(value):
    """
    Returns True if value is a list of int or float

    Parameter value: a value to check
    Precondition: value can be anything
    """
    pass


# ADD MORE HELPER FUNCTIONS FOR ASSERTS HERE
def is_point_list(value):
    """
    Returns True if value is a 2d list of int or float

    This function also checks that all points in value have same dimension.

    Parameter value: a value to check
    Precondition: value can be anything
    """
    pass


def is_seed_list(value, k, size):
    """
    Returns True if value is k-element list of indices between 0 and (len - 1).

    Parameter value: a value to check
    Precondition: value can be anything

    Parameter k: The required list size
    Precondition: k is an int > 0

    Paramater size: The database size
    Precondition: size is an int > 0
    """
    pass
