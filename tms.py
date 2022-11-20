def trust_value(node, last_X_epochs, trustscore, df_calculation):  # remove the items from trust score lists that their key id are malicious
    # print("this is our last_X_epochs")
    print("OUR NODE IS: %s" % node)
    print("THIS IS INSIDE THE CALC...")
    print(df_calculation)
    m_rate = df_calculation["M_Rate"].item()
    last_epoch_tv = last_X_epochs.loc[last_X_epochs["Node_ID"] == node]["Trust_Value"].item()

    trustvalue = (trustscore[node] + last_epoch_tv * 2 + m_rate) / 4

    """"
    if node in malicious_ids:
        # 10 thing
        trustvalue = (0 + trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
            "Trust_Value"].mean(axis=0) * 6) / 10
        trustvalue = round(trustvalue, 1)
        trustvaluedict[node] = trustvalue
    else:
        # 7 thing
        trustvalue = (trustscore[node] + last_X_epochs.loc[last_X_epochs["Node_ID"] == node][
            "Trust_Value"].mean(axis=0) * 6) / 7
        trustvalue = round(trustvalue, 1)
        trustvaluedict[node] = trustvalue
    """

    return abs(trustvalue)
"""
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
"""
