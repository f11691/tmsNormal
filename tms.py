def trust_value(know_nodes, malicious_ids, tms_last_X_required_epochs, last_X_epochs,
                trustscore):  # remove the items from trust score lists that their key id are malicious

    trustvaluedict = dict()

    if tms_last_X_required_epochs != len(last_X_epochs):
        for node in know_nodes:
            if node == malicious_ids:
                # 10 thing
                trustvalue = (-3 + trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
                    "Trust_Value"].mean(axis=0) * 6) / 10
                trustvalue = round(trustvalue, 1)
                trustvaluedict[node] = trustvalue
            else:
                # 7 thing
                trustvalue = (trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
                    "Trust_Value"].mean(axis=0) * 6) / 7
                trustvalue = round(trustvalue, 1)
                trustvaluedict[node] = trustvalue

        return trustvaluedict
    else:
        # Potentially dead code
        # Known dublicate: maybe remove if logic is not different
        for node in know_nodes:
            if node == malicious_ids:
                # 10 thing
                trustvalue = (-3 + trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
                    "Trust_Value"].mean(axis=0) * 6) / 10
                trustvalue = round(trustvalue, 1)
                trustvaluedict[node] = trustvalue
            else:
                # 7 thing
                trustvalue = (trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
                    "Trust_Value"].mean(axis=0) * 6) / 7
                trustvalue = round(trustvalue, 1)
                trustvaluedict[node] = trustvalue
