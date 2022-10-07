def trust_value(know_nodes, malicious_ids, tms_last_X_required_epochs, last_X_epochs,
                trustscore):  # remove the items from trust score lists that their key id are malicious

    trustvaluedict = dict()

    if tms_last_X_required_epochs != len(last_X_epochs):
        for node in know_nodes:
            if node == malicious_ids:
                # 10 thing
                trustvalue = (-3 + trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
                    "Trust_Value"].item() * 6) / 10
                trustvaluedict[node] = trustvalue
            else:
                # 7 thing
                trustvalue = (trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
                    "Trust_Value"].item() * 6) / 7
                trustvalue = round(trustvalue, 1)
                trustvaluedict[node] = trustvalue

        return trustvaluedict

    """
    for i in nodenumber:
        keys = set(self.nodenumber)
        self.trustvalue = {k: ((malicious.m[k] * 3 + score.trustscore[k] + blockchain.lastepoch[k] * 6) / 10) for k
                           in keys}
    """
