import random
import numpy as np


# function for set randomly how many request and transaction send by each node per epoch
def req(know_nodes):
     reqn = dict()

     for node in know_nodes:
         request = np.random.uniform(0, 10)
         request = round(request, 1)
         reqn[node]= request

     return reqn


# function to calculate how many of request of each node must accept by network based on their trust level
def acp(reqn, tvalue, malicious_ids):
    acpn = dict()
