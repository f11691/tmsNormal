import pandas as pd

import malicious
import score
import voting


def initialize():
    """
    Load the initial list of nodes from csv
    Create the dict of subnets (contains list of nodes per subnet)
    :return: initial dataframe, dataframe for logging, subnet dict
    """
    df_init = pd.read_csv("init.csv")

    subnets = dict()
    subnet_names = df_init["Subnet_ID"].unique().tolist()

    for names in subnet_names:
        df_tmp = df_init.loc[df_init['Subnet_ID'] == names]
        df_tmp = df_tmp["Node_ID"]
        subnet_nodes = df_tmp.tolist()
        subnets[names] = subnet_nodes

    df_output = df_init
    # df_output = df_output.drop(["Node_Type", "Subnet_ID", "List_Type"], axis=1)
    df_output = df_output.drop(["Node_Type", "Subnet_ID"], axis=1)
    df_output.insert(0, "Epoch", 0)

    list_types = ["B", "G", "W"]
    blacklist = list()
    graylist = list()
    whitelist = list()

    for element in list_types:
        df_tmp = df_init.loc[df_init["List_Type"] == element]
        df_tmp = df_tmp["Node_ID"]
        nodes = df_tmp.tolist()
        if element == "B":
            blacklist.extend(nodes)
        elif element == "G":
            graylist.extend(nodes)
        elif element == "W":
            whitelist.extend(nodes)
        else:
            raise ValueError

    trustvalue_dict = dict()

    for index, row in df_output.iterrows():
        trustvalue_dict[row["Node_ID"]] = row["Trust_Value"]

    return df_init, df_output, subnets, blacklist, graylist, whitelist, trustvalue_dict


if __name__ == "__main__":
    df_init, df_output, subnets, blacklist, graylist, whitelist, trustvalue_dict = initialize()
    print(df_output)
    tms_last_X_required_epochs = 5

    current_epoch = 0
    """
    print(df_init)
    print(df_output)
    print(subnets)
    print(blacklist)
    print(graylist)
    print(whitelist)
    print(trustvalue_dict)
    """
    print(20 * "#")

    m1 = malicious.Malicious(20, 2, len(whitelist), len(blacklist), len(graylist), whitelist, blacklist, graylist)
    m1.run_all()

    # Subnet 1
    v1 = voting.Voter(subnets[1])
    v1vote = v1.voting(trustvalue_dict)
    s1 = score.Score(v1vote, subnets[1])
    s1score = s1.scorearray()

    # Subnet 2
    v2 = voting.Voter(subnets[2])
    v2vote = v2.voting(trustvalue_dict)
    s2 = score.Score(v2vote, subnets[2])
    s2score = s2.scorearray()

    # Subnet 3
    v3 = voting.Voter(subnets[3])
    v3vote = v3.voting(trustvalue_dict)
    s3 = score.Score(v3vote, subnets[3])
    s3score = s3.scorearray()

    # Subnet 4
    v4 = voting.Voter(subnets[4])
    v4vote = v4.voting(trustvalue_dict)
    s4 = score.Score(v4vote, subnets[4])
    s4score = s4.scorearray()

    # extract last 5 epochs from df_output
    num_epochs = df_output["Epoch"].unique().tolist()
    num_epochs = pd.Series(num_epochs)
    last_X_epochsindexes = num_epochs.nlargest(tms_last_X_required_epochs)
    last_X_epochs_numbers = last_X_epochsindexes.index.values.tolist()
    print(last_X_epochs_numbers)
    print(tms_last_X_required_epochs)

    df_last_X_epochs = df_output.loc[df_output["Epoch"].isin(last_X_epochs_numbers)]
    print(df_last_X_epochs)

    # call tms with: malicious_ids, tms_last_X_required_epochs, last_X_epochs, s1score, s2score, s3score, s4score

