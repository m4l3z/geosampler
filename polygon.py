#! /usr/bin/python3
# -*- coding: utf-8 -*-

from node import Node

class Polygon: 
    name = None
    dimension = None
    nodes = list()

    def __init__(self, name, dimension):
        self.name = name 
        self.dimension = dimension
        reset()

    def show_details(self):
        print("Name:",self.name,"\nDimension:",len(self.nodes))
        print("\nNodes:")
        for n in self.nodes:
            n.show_details()

    def append_node(self):
        self.nodes.append(Node(len(self.nodes)))

    def set_node(self, pos, node) :
        self.nodes[pos] = node

    def get_node(self, pos) :
        return self.nodes[pos]

    def reset(self):
        self.nodes = [None for i in range(self.dimension)]
