import malicious
import score


class Tms:  # class for calculate trust value running end of every epoch

    def get_maliciouslist(self):  # get list of malicious nodes ID
        return malicious.m

    def trust_value(self, nodenumber):  # remove the items from trust score lists that their key id are malicious
        for i in nodenumber:
            keys = set(self.nodenumber)
            self.trustvalue = {k: ((malicious.m[k] * 3 + score.trustscore[k] + blockchain.lastepoch[k] * 6) / 10) for k
                               in keys}
