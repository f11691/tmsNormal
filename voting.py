""" devices voting"""
import random

import numpy as np


class Voter:  # nodes as voters

    def __init__(self, neighbours):
        self.vote_list = dict()
        self.neighbours = neighbours

    def voting(self, trustvalue_dict, df_middle):
        # print(trustvalue_dict)
        # print(self.neighbours)

        df_last_epoch = df_middle[df_middle["Epoch"].max() == df_middle["Epoch"]]

        node_trust_value_dict = dict()

        for _, row in df_last_epoch.iterrows():
            node_trust_value_dict[row["Node_ID"]] = row["Trust_Value"]

        for k, _ in node_trust_value_dict.items():
            if node_trust_value_dict[k] == 0.0 or node_trust_value_dict[k] == -0.0:
                node_trust_value_dict[k] = abs(0)

        node_trust_value_dict = dict(sorted(node_trust_value_dict.items(), key=lambda item: item[1], reverse=True))

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

                    for node in node_trust_value_dict:





























                       """ if node_trust_value_dict[node] == 1:
                            v = node_trust_value_dict[node] + 0.1
                            if v > 1:
                                v = 1
                        elif 0.9 < node_trust_value_dict[node] < 1:
                            v = node_trust_value_dict[node] + 0.1
                        elif 0.8 < node_trust_value_dict[node] <= 0.9:
                            v = node_trust_value_dict[node] + 0.09
                        elif 0.7 < node_trust_value_dict[node] <= 0.8:
                            v = node_trust_value_dict[node] + 0.08
                        elif 0.6 < node_trust_value_dict[node] <= 0.7:
                            v = node_trust_value_dict[node] + 0.08
                        elif 0.5 < node_trust_value_dict[node] <= 0.6:
                            v = node_trust_value_dict[node] + 0.07
                        elif 0.4 < node_trust_value_dict[node] <= 0.5:
                            v = node_trust_value_dict[node] + 0.06
                        elif 0.3 < node_trust_value_dict[node] <= 0.4:
                            v = node_trust_value_dict[node] + 0.05
                        elif 0.2 < node_trust_value_dict[node] <= 0.3:
                            v = node_trust_value_dict[node] - 0.03
                        elif 0.1 < node_trust_value_dict[node] <= 0.2:
                            v = node_trust_value_dict[node] - 0.04
                        elif 0 < node_trust_value_dict[node] <= 0.1:
                            v = node_trust_value_dict[node] - 0.05
                        elif node_trust_value_dict[node] == 0:
                            v = node_trust_value_dict[node] - 0.1
                            if v < 0:
                                v = 0
                        else:
                            print("Node ID %s has undefined List type for value %s" % (node, node_trust_value_dict[node]))
                            raise ValueError

        return vote"""

    """def __init__(self, neighbours):
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
                    # v = random.triangular(0, 1, 0.5)
                    # v = random.random()
                    #v = round(v, 1)
                    #vote[x, y] = v
                    if 0.75 < tv_y <= 1:
                        v = tv_y + 0.05
                        if v > 1:
                            v = 1
                    elif 0.5 < tv_y <= 0.75:
                        v = tv_y + 0.025
                    elif 0.025 < tv_y <= 0.05:
                        v = tv_y - 0.025
                    else 0 < tv_y <= 0.025:
                        v = tv_y - 0.05
                        if v < 0
                            v = 0

        return vote"""
