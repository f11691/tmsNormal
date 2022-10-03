""" devices voting"""
import random

import numpy as np


class Voter:  # nodes as voters

    def __init__(self, neighbours):
        self.vote_list = dict()
        self.neighbours = neighbours

    def voting(self, trustvalue_dict):
        print(trustvalue_dict)
        print(self.neighbours)

        vote = np.zeros((len(self.neighbours) + 1, len(self.neighbours) + 1))
        for i in range(len(self.neighbours) + 1):
            if i == 0:
                vote[0, i] = 0
            else:
                vote[0, i] = self.neighbours[i - 1]
                vote[i, 0] = self.neighbours[i - 1]

        for x in range(1, len(self.neighbours) + 1):
            for y in range(1, len(self.neighbours) + 1):
                if x == y:
                    pass
                else:
                    v = random.triangular(-1, 1, 0)
                    v = round(v, 1)
                    vote[x, y] = v

        return vote


"""
    def vote(self, vote_list):  # check if had not vote and request voting from full node, create vote list
        if self.called_voter is True and self.check_duplicate is True:
            keys = set(self.neighbours).intersection(
                set(syntheticdata.tvdict.keys()))  # Create a new dict with merging list of neighbors and new trust scores.
            return {k: syntheticdata.tvdict[k] for k in keys}
"""
