def trust_value(know_nodes, malicious_ids, tms_last_X_required_epochs, last_X_epochs,
                trustscore):  # remove the items from trust score lists that their key id are malicious

    trustvalue = dict()

    if len(tms_last_X_required_epochs) != last_X_epochs:
        for node in know_nodes:
            if node == malicious_ids:
                # 7 thing
                print("ahahahah")
            else:
                # 10 thing
                print("heheheh")

    """
    for i in nodenumber:
        keys = set(self.nodenumber)
        self.trustvalue = {k: ((malicious.m[k] * 3 + score.trustscore[k] + blockchain.lastepoch[k] * 6) / 10) for k
                           in keys}
    """
