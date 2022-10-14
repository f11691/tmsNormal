import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import malicious
import score
import tms
import voting
import tmsanalyse


##########################
# Use with pandas < 1.5.0
##########################

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

    dict_of_nodes_subnets = dict()
    node_names = df_init["Node_ID"].tolist()
    for node in node_names:
        df_tmp = df_init.loc[df_init['Node_ID'] == node]
        df_tmp = df_tmp["Subnet_ID"].item()
        dict_of_nodes_subnets[node] = df_tmp

    # we need to change it to middle data frame (epochnumber,nodeID, subnetID, group list, trust level, malicious status)

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

    return df_init, df_output, subnets, dict_of_nodes_subnets, blacklist, graylist, whitelist, trustvalue_dict


if __name__ == "__main__":
    df_init, _, subnets, dict_of_nodes_subnets, blacklist, graylist, whitelist, trustvalue_dict = initialize()
    # Max X epochs (buffer)
    df_middle = pd.DataFrame(
        columns=["Epoch", "Node_ID", "Subnet_ID", "List_Type", "Trust_Value", "Malicious_Status"])

    current_epoch = 0
    tms_last_X_required_epochs = 5

    know_nodes = df_init["Node_ID"].unique()
    num_known_nodes = know_nodes.size

    for node in know_nodes:
        df_insert = pd.DataFrame(
            {"Epoch": current_epoch, "Node_ID": [node], "Subnet_ID": [dict_of_nodes_subnets[node]],
             "List_Type": "XXXX",
             "Trust_Value": [trustvalue_dict[node]], "Malicious_Status": [False]})
        df_middle = pd.concat([df_middle, df_insert])

    """
    print(df_output)
    print(subnets)
    print(blacklist)
    print(graylist)
    print(whitelist)
    print(trustvalue_dict)
    """

    for i in range(current_epoch, 11):
        current_epoch += 1
        print("#####################################")
        print("New epoch: %s" % current_epoch)
        m1 = malicious.Malicious(20, 2, len(whitelist), len(blacklist), len(graylist), whitelist, blacklist, graylist)
        malicious_nodes = m1.run_all()

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

        trustscore = s1score | s2score | s3score | s4score
        trustscore = dict(sorted(trustscore.items()))
        trustvalue = tms.trust_value(know_nodes, m1.m, tms_last_X_required_epochs, df_middle, trustscore)
        num_epochs_df_middle = df_middle["Epoch"].unique().tolist()
        # print("Num of epochs %s" % num_epochs_df_middle)
        if len(num_epochs_df_middle) == 5:
            # print("!!!!!!!! NOW WE NEED TO DELETE !!!!!!!!!")
            # print(num_epochs_df_middle[0])
            df_middle = df_middle.loc[df_middle["Epoch"].isin(num_epochs_df_middle[-4:]), :]

        node_trust_value_dict, list_type, top_percent_dict = tmsanalyse.analyse(df_middle)

        for node in know_nodes:
            if node in malicious_nodes:
                malicious_status = True
            else:
                malicious_status = False
            df_insert = pd.DataFrame(
                {"Epoch": current_epoch, "Node_ID": [node], "Subnet_ID": [dict_of_nodes_subnets[node]],
                 "List_Type": [list_type[node]],
                 "Trust_Value": [trustvalue[node]], "Malicious_Status": [malicious_status]})
            df_middle = pd.concat([df_middle, df_insert])
        print(df_middle)
