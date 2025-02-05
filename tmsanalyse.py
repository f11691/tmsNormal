def analyse(df_middle, full_node_ids):
    """
    0. extract last epoch of df_middle !
    1. extract trust value and node id as dict !
    2. sort dict by value !
    3. get top 10% of value and node id -> new list !
    4. sort dict (from 2.) -> if > 0.5: white, 0.5 - -0.1: grey, -0.2 - -1: black
    return sort dict, list_type, new list for log
    """

    df_last_epoch = df_middle[df_middle["Epoch"].max() == df_middle["Epoch"]]

    node_trust_value_dict = dict()
    full_node_dict = dict()

    for _, row in df_last_epoch.iterrows():
        node_trust_value_dict[row["Node_ID"]] = row["Trust_Value"]

    for _, row in df_last_epoch.iterrows():
        full_node_dict[row["Node_ID"]] = row["Node_Type"]

    for k, _ in node_trust_value_dict.items():
        if node_trust_value_dict[k] == 0.0 or node_trust_value_dict[k] == -0.0:
            node_trust_value_dict[k] = abs(0)

    node_trust_value_dict = dict(sorted(node_trust_value_dict.items(), key=lambda item: item[1], reverse=True))

    top_percent = 10

    number_elements = int(top_percent * len(node_trust_value_dict) / 100)

    top_percent_dict = {}

    copy_node_trust_value_dict = dict(node_trust_value_dict)

    for element in full_node_ids:
        copy_node_trust_value_dict.pop(element)

    for i, key in enumerate(copy_node_trust_value_dict.keys(), 1):
        if i > number_elements:
            break
        top_percent_dict[key] = copy_node_trust_value_dict[key]

    list_type = dict()
    for node in node_trust_value_dict:
        if node_trust_value_dict[node] >= 0.8:
            list_type[node] = "W"
        elif 0.8 > node_trust_value_dict[node] >= 0.3:
            list_type[node] = "G"
        elif 0.3 > node_trust_value_dict[node] >= 0:
            list_type[node] = "B"
        else:
            print("Node ID %s has undefined List type for value %s" % (node, node_trust_value_dict[node]))
            raise ValueError

    return node_trust_value_dict, list_type, top_percent_dict
