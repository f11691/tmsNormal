"""Trust Score for each subnetwork"""

import numpy as np


class Score:  # calculate trust score of each subnet

    def __init__(self, matrix, neighbours):  # get the matrix vote for each subnet
        self.convert = []
        self.vote = matrix
        self.neighbours = neighbours

    def scorearray(self):  # function for get summation of each column from matrix
        convert = self.vote
        # Delete the first column of the matrix, not needed more
        convert = np.delete(convert, 0, 1)
        # Store the neighbours for later use
        neighbours = convert[0]
        # Delete first row
        convert = np.delete(convert, 0, 0)
        total_0_axis = np.average(convert, axis=0)  # array of summation of columns
        trustscore = dict()
        for index, neighbour in enumerate(neighbours):
            trustscore[int(neighbour)] = round(total_0_axis[index], 4)

        return trustscore
