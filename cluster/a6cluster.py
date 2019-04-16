"""
Cluster class for k-Means clustering

This file contains the class cluster, which is the second part of the assignment.  With
this class done, the visualization can display the centroid of a single cluster.

Anthony Nguyen (an523) and John O'Donnel (jro79)
4/11/19
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6checks
import a6dataset


class Cluster(object):
    """
    A class representing a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices in the dataset
    of the points contained in the cluster.  For instance, a cluster consisting of the
    points with indices 0, 4, and 5 in the dataset's data array would be represented by
    the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of the k-means
    algorithm.  This centroid is an n-D point (where n is the dimension of the dataset),
    represented as a list of n numbers, not as an index into the dataset. (This is because
    the centroid is generally not a point in the dataset, but rather is usually in between
    the data points.)

    INSTANCE ATTRIBUTES:
        _dataset [Dataset]: the dataset this cluster is a subset of
        _indices [list of int]: the indices of this cluster's points in the dataset
        _centroid [list of numbers]: the centroid of this cluster
        _name [str]: an optional label for the centroid. Can be the empty string
    EXTRA INVARIANTS:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """

    # Part A
    def __init__(self, dset, centroid,name=""):
        """
        Initializes a new empty cluster whose centroid is a copy of <centroid>

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter centroid: the cluster centroid
        Precondition: centroid is a list of dset.getDimension() numbers

        Parameter name: the name of the cluster centroid
        Precondition: a string, possibly empty
        """
        # Asserting Preconditions
        assert isinstance(dset, a6dataset.Dataset), "dset must be of type Dataset"
        assert isinstance(centroid, list)
        assert len(centroid) == dset.getDimension()
        assert isinstance(name, str)

        self._dataset = dset
        self._centroid = centroid[:]
        self._name = name
        self._indices = []


    def getCentroid(self):
        """
        Returns the centroid of this cluster. Does not return a copy.

        This getter method is to protect access to the centroid.
        """

        return self._centroid


    def getName(self):
        """
        Returns the name of this centroid.

        This getter method is to protect access to the centroid.
        """

        return self._name


    def setName(self,name):
        """
        Sets the name of this centroid.

        Precondition: name is a string
        """

        assert type(name) == str
        self._name = name


    def getIndices(self):
        """
        Returns the indices of points in this cluster

        This method returns the attribute _indices directly.  Any changes made to this
        list will modify the cluster.
        """
        return self._indices


    def addIndex(self, index):
        """
        Adds the given dataset index to this cluster.

        If the index is already in this cluster, this method leaves the
        cluster unchanged.

        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize()-1.
        """
        assert index in range(self._dataset.getSize())
        if index not in self._indices:
            self._indices.append(index)



    def clear(self):
        """
        Removes all points from this cluster, but leave the centroid unchanged.
        """
        self._indices = []


    def getContents(self):
        """
        Returns a new list containing copies of the points in this cluster.

        The result is a list of list of numbers.  It has to be computed from the indices.
        """
        new_list=[]
        for x in self._indices:
            copy = a6dataset.Dataset.getPoint(self._dataset, x)
            new_list.append(copy)
        return new_list


    # Part B
    def distance(self, point):
        """
        Returns the euclidean distance from point to this cluster's centroid.

        Parameter point: The point to be measured
        Precondition: point is a list of numbers (int or float), with the same dimension
        as the centroid.
        """
        assert len(point) == a6dataset.Dataset.getDimension(self._dataset)
        sum = 0
        for x in range(a6dataset.Dataset.getDimension(self._dataset)):
            diff = point[x] - self._centroid[x]
            diff_squared = math.pow(diff,2)
            sum += diff_squared
        euclidean = math.sqrt(sum)
        return euclidean

    def getRadius(self):
        """
        Returns the maximum distance from any point in this cluster, to the centroid.

        This method loops over the contents to find the maximum distance from the centroid.
        """
        list_distance = []
        



    def update(self):
        """
        Returns True if the centroid remains the same after recomputation; False otherwise.

        This method recomputes the _centroid attribute of this cluster. The new _centroid
        attribute is the average of the points of _contents (To average a point, average
        each coordinate separately).

        Whether the centroid "remained the same" after recomputation is determined by
        numpy.allclose.  The return value should be interpreted as an indication of whether
        the starting centroid was a "stable" position or not.

        If there are no points in the cluster, the centroid. does not change.
        """
        # BEGIN REMOVE
        pass
        # END REMOVE
        # IMPLEMENT ME


    def findError(self):
        """
        Returns: a float representing the total error of the centroid.

        The total error is calculated as the total squared distance from every point
        belonging to that centroid to the center of the centroid.

        For example, if their is 2 points, one 1 unit from the center and another point
        2 units from the center the error for this centroid would be 5 as we have
        1 * 1 + 2 * 2 = 5.

        Thus we would return 5.0

        Hint: The method distance() will he helpful.
        """

        datalist = self.getContents()
        indiciesist = self.getIndices()
        total_error = 0

        for i in range(0,len(self.getIndices())):
            total_error += distance(datalist[indiciesist[i]]) ** 2


    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """
        Returns a String representation of the centroid of this cluster.
        """
        return str(self._centroid)


    def __repr__(self):
        """
        Returns an unambiguous representation of this cluster.

        You do NOT have to use this function in your implementation if you do not want
        to. This provides more infomation for assert statements and can be used
        in place of the str method however, this method is deemed out of scope for
        A6 ,so do not stress if you do not understand __repr__.
        """
        return str(self.__class__) + str(self)
