import random
import numpy as np


# function for set randomly how many request and transaction send by each node per epoch
def req(know_nodes):
     req_dict = dict()

     for node in know_nodes:
         request = np.random.uniform(0, 10)
         request = round(request, 1)
         req_dict[node]= request

     return req_dict


# function to calculate how many of request of each node must accept by network based on their trust level
def acp(req_dict, node_trust_value_dict, malicious_ids):
    accp_dict = dict()

    for node in node_trust_value_dict:
        if node_trust_value_dict[node] >= 0.5:
            accp_dict[node] = 100
        elif 0.5 > node_trust_value_dict[node] >= 0:
            accp_dict[node] = 80
        elif 0 > node_trust_value_dict[node] >= -0.1:
            accp_dict[node] = 50
        elif -0.1 > node_trust_value_dict[node] >= -0.5:
            accp_dict[node] = 30
        elif -0.5 > node_trust_value_dict[node] >= -1:
            accp_dict[node] = 0

    return accp_dict


# or calculate how many of them accepted from request numbers?!?!