"""Trust Score for each subnetwork"""

import numpy as np
import voting


class score:  # calculate trust score of each subnet

    def __int__(self, matrix, neighbours):  # get the matrix vote for each subnet
        self.convert = []
        self.vote = matrix
        self.neighbours = neighbours
        self.trustscore = []


    """
    def score(self, convert):  # going throu the matrix and put each colum in a list
        convert = vote
        convert = np.array(convert)
        for (i > 2) in (range(len(convert)))  # we don't need first colum because it is full node
            xi = (convert[:, i])                 # create an array from each column
        """

    def scorearray(self, convert):      # function for get summation of each column from matrix
        convert = vote
        convert = np.array(convert)
        total_0_axis = np.sum(convert, axis=0)      # array of summation of columns
        columnumber = 5                             # number of column
        scorearray = [x / columnumber for x in total_0_axis]            # array of average amounts

        trustscore : [int: int] =[:]

        for (index, element) in neighbours.enumerated()             # crate a dictonary for trust score
            {
        trustscore[element] = self.scorearray[index]
        }

