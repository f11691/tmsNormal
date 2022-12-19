import numpy as np


def sigma(know_nodes, tms_last_X_required_epochs, last_X_epochs):
    avgdict = dict()
    sigdict = dict()

    if tms_last_X_required_epochs != len(last_X_epochs):
        for node in know_nodes:
            avg = (last_X_epochs.loc[last_X_epochs["Node_ID"] == node]["Trust_Value"].mean(axis=0))
            avg = round(avg, 5)
            avgdict[node] = avg
            sig = np.std(last_X_epochs.loc[last_X_epochs["Node_ID"] == node]["Trust_Value"])
            sig = round(sig, 5)
            sigdict[node] = sig

    return avgdict, sigdict
