#! /usr/bin/python3
# -*- coding: utf-8 -*-

class Node: 
    sample = "No sample" 
    def __init__(self, number):
        self.number = number
    def Load_Sample(self, path):
        self.sample = path 
    def Remove_Sample(self):
        self.sample = "No sample"
    def Show_Details(self):
        print ("Number:",self.number,"\nSample:",self.sample)