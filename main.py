import pandas as pd


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
    df_output = df_output.drop(["Node_Type", "Subnet_ID", "List_Type"], axis=1)
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

    return df_init, df_output, subnets, blacklist, graylist, whitelist


if __name__ == "__main__":
    df_init, df_output, subnets, blacklist, graylist, whitelist = initialize()
    print(df_init)
    print(df_output)
    print(subnets)
    print(blacklist)
    print(graylist)
    print(whitelist)
