""" devices voting"""
import random
import sigma
import numpy as np


class Voter:  # nodes as voters

    def __init__(self, neighbours):
        self.vote_list = dict()
        self.neighbours = neighbours

    def voting(self, trustvalue_dict, df_middle, avg_dict, sig_dict):
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

        # this is vorting for all, we need voting for the neighbours
        # SO we need to only look at the node_trust.... keys that are our neighbours
        # for x in ...
        # node_trust...[y]
        for x in range(1, len(self.neighbours) + 1):
            for y in range(1, len(self.neighbours) + 1):
                if x == y:
                    pass
                else:
                    # dont loop
                    # look at avg_dict[y]
                    # for node_avg, node_sig in zip(avg_dict, sig_dict):
                    if node_trust_value_dict[y] > (avg_dict[y] + sig_dict[y]):
                        v = node_trust_value_dict[y] + random.uniform(0.1, 0.2)
                        if v > 1:
                            v = 1
                    elif (avg_dict[y] - sig_dict[y]) <= node_trust_value_dict[y] <= (avg_dict[y] + sig_dict[y]):
                        v = node_trust_value_dict[y] + random.uniform(0, 0.1)

                    elif (avg_dict[y] - sig_dict[y]) < node_trust_value_dict[y]:
                        v = node_trust_value_dict[y] - random.uniform(0.05, 0.1)
                        if v < 0:
                            v = 0
                    else:
                        v = 9999999
                    vote[x, y] = v

        return vote
