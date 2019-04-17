"""
Primary algorithm for k-Means clustering

This file contains the Algorithm class for performing k-means clustering.  While it is
the last part of the assignment, it is the heart of the clustering algorithm.  You
need this class to view the complete visualizer.

Anthony Nguyen an523 and John O'Donnel jro79
DATE COMPLETED HERE
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6checks
import a6dataset
import a6cluster


class Algorithm(object):
    """
    A class to manage and run the k-means algorithm.

    INSTANCE ATTRIBUTES:
        _dataset [Dataset]: the dataset which this is a clustering of
        _clusters [list of Cluster]: the clusters in this clustering (not empty)
    """


    # Part A
    def __init__(self, dset, k, seeds=None):
        """
        Initializes the algorithm for the dataset ds, using k clusters.

        If the optional argument seeds is supplied, it will be a list of indices into the
        dataset that specifies which points should be the initial cluster centroids.
        Otherwise, the clusters are initialized by randomly selecting k different points
        from the database to be the cluster centroids.

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter k: the number of clusters
        Precondition: k is an int, 0 < k <= dset.getSize()

        Paramter seeds: the initial cluster indices (OPTIONAL)
        Precondition seeds is None, or a list of k valid indices into dset.
        """
        assert isinstance(dset, a6dataset.Dataset)
        assert isinstance(k, int) and k > 0 and k <= dset.getSize()
        assert seeds == None or a6checks.is_seed_list(seeds,k,dset.getSize())

        self._dataset = dset
        self._clusters = []
        self.seeds = seeds
        population = a6dataset.Dataset.getContents(self._dataset)
        length_list = a6dataset.Dataset.getDimension(self._dataset)
        random_point_list = random.sample(population, k)

        if self.seeds == None: #choose random centroids
            for x in range(k):
                new_cluster = a6cluster.Cluster(self._dataset, random_point_list[x])
                self._clusters.append(new_cluster)
        else:
            for x in self.seeds:
                new_cluster = a6cluster.Cluster(self._dataset, population[x])
                self._clusters.append(new_cluster)


    def getClusters(self):
        """
        Returns the list of clusters in this object.

        This method returns the attribute _clusters directly.  Any changes made to this
        list will modify the set of clusters.
        """
        return self._clusters


    # Part B
    def _nearest(self, point):
        """
        Returns the cluster nearest to point

        This method uses the distance method of each Cluster to compute the distance
        between point and the cluster centroid. It returns the Cluster that is closest.

        Ties are broken in favor of clusters occurring earlier self._clusters.

        Parameter point: The point to compare.
        Precondition: point is a list of numbers (int or float), with the same dimension
        as the dataset.
        """

        assert a6checks.is_point(point)
        assert len(point) == self._dataset.getDimension()

        list_of_clusters = self.getClusters()
        nearest_cluster = None
        nearest_distance = None

        for i in range(len(list_of_clusters)):
            if(i==0):
                nearest_cluster = list_of_clusters[i]
                nearest_distance = list_of_clusters[i].distance(point)
    
            if(list_of_clusters[i].distance(point) < nearest_distance):
                nearest_cluster = list_of_clusters[i]
                nearest_distance = list_of_clusters[i].distance(point)
        return nearest_cluster



    def _partition(self):
        """
        Repartitions the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.

        for i in range(len(self.getClusters())):
            self._clusters[i].clear()

        for operating_cluster in self.:
            for i in range(len(self._dataset.getContents())):
                point_to_add = self._dataset.getPoint(i)
                cluster_added_to = self._nearest(point_to_add)
                if(cluster_added_to == operating_cluster):
                    print("index being added is " + str(i))
                    operating_cluster.addIndex(i)






    # Part C
    def _update(self):
        """
        Returns True if all centroids are unchanged after an update; False otherwise.

        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """

        cluster_list = self.getClusters()

        for i in range(len(cluster_list)):
            if(cluster_list[i].update() == False):
                return False
        return True


    def step(self):
        """
        Returns True if the algorithm converges after one step; False otherwise.

        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns the appropriate value.
        """
        # In a cycle, we partition the points and then update the means.
        # BEGIN REMOVE
        pass
        # END REMOVE
        # IMPLEMENT ME


    # Part D
    def run(self, maxstep):
        """
        Continues clustering until either it converges or maxstep steps (which ever comes first).

        Parameter maxstep: an int >= 0.
        """
        # Call step repeatedly, up to maxstep times, until the algorithm
        # converges. Stop after maxstep iterations even if the algorithm has not
        # converged.
        # You do not need a while loop for this.  Just write a for-loop, and exit
        # the for-loop (with a return) if you finish early.

        # BEGIN REMOVE
        pass
        # END REMOVE
        # IMPLEMENT ME


    def findTotalError(self):
        """
        Returns: a float representing the sum of the errors of all the centroids.

        For example, if we have two centroids and they have errors of 2.0 and 3.0 respectively,
        then the total error would be 5.0 and we would return 5.0.

        Hint: the method and findError() would be helpful in the function.
        """
        pass
