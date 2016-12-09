#! /usr/bin/python3
# -*- coding: utf-8 -*-

from node import Node

class Polygon: 

    def __init__(self, name, dimension):
        self.name = name 
        self.dimension = dimension
        self.node = [Node(i) for i in range(dimension)]
    def Show_Details(self):
        print("Name:",self.name,"\nDimension:",len(self.node))
        print("\nNodes:")
        for nodes in self.node:
            nodes.Show_Details()
    def Add_Node(self):
        self.node.append(Node(len(self.node)))
    def Reset(self):
        self.node = [Node(i) for i in range(self.dimension)]