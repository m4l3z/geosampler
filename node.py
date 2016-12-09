#! /usr/bin/python3
# -*- coding: utf-8 -*-

class Node: 
    sample = None

    def __init__(self):
    	pass

    def Load_Sample(self, sample):
        self.sample = sample

    def Remove_Sample(self):
        self.sample = None