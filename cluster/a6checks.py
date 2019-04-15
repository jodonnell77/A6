"""
Helper functions for k-Means clustering

This file contains the functions for enforcing preconditions for k-means clustering.
We have written the first for you.  You will probably want to write others.

John O'Donnell (jro79) and Anthony Nguyen (an523)
4/11/19
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
    if(type(value) != list or len(value) == 0):
        return False
    for i in range(0,len(value)):
        if(type(value[i]) != int and type(value[i]) != float):
            return False
    return True


# ADD MORE HELPER FUNCTIONS FOR ASSERTS HERE
def is_point_list(value):
    """
    Returns True if value is a 2d list of int or float

    This function also checks that all points in value have same dimension.

    Parameter value: a value to check
    Precondition: value can be anything
    """
    if(type(value) != list or len(value) == 0):
        return False
    for i in range(0,len(value)):
        if(type(value[i]) != list):
            return False
        if( not is_point(value[i]) ):
            return False

    for i in range(0,len(value)):
        if(i == 0):
            pass
        else:
            for ii in range(0,len(value)-1):
                if(len(value[i]) != len(value[ii])):
                    return False
    return True

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
    assert size > 0, "Size must be greater than 0"
    assert k > 0, "k must be greater than 0"

    pass
