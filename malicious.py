"""Malicious"""

import random  # for import Random choices() Methode
# from node import *


class Malicious:  # for calculate malicious nodes between 3 groups

    def __init__(self, n, x, xw, xb, xg, listw, listb, listg):
        self.mb = []
        self.mg = []
        self.mw = []
        self.m = []
        self.ca = []
        self.ra = []
        self.ad = []
        self.n = n  # get all nodes number from simblock
        self.x = x  # number of all malicious nodes
        self.xw = xw  # withe list nodes malicious number
        self.xb = xb  # black list nodes malicious number
        self.xg = xg  # gray list nodes malicious number
        self.lw = listw  # instantiation  of list white
        self.lb = listb  # instantiation  of list black
        self.lg = listg  # instantiation  of list gray

    def calculate_n(self):  # get number of all the nodes
        self.n = len(node.nodearray)

    def calculate_x(self):  # calculate number of all malicious nodes
        self.x = (self.n * (20 / 100))

    def calculate_xw(self):  # calculate number of malicious nodes in withe list
        self.xw = (self.x * (5 / 100))

    def calculated_xg(self):  # calculate number of malicious nodes in gray list
        self.xg = (self.x * (25 / 100))

    def calculated_xb(self):  # calculate number of malicious nodes in black list
        self.xb = (self.x * (70 / 100))

    def calculated_mw(self):  # calculate malicious nodes of withe list
        self.mw = random.choices(self.lw, weights=None, cum_weights=None, k=int(self.xw))

    def calculated_mb(self):  # calculate malicious nodes of black list
        self.mb = random.choices(self.lb, weights=None, cum_weights=None, k=self.xb)

    def calculated_mg(self):  # calculate malicious nodes of gray list
        self.mg = random.choices(self.lg, weights=None, cum_weights=None, k=self.xg)

    def merge_m(self):  # merge all malicious nodes id in one list
        self.m = self.mw + self.mb + self.mg
