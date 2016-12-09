#! /usr/bin/python3
# -*- coding: utf-8 -*-

from node import Node

class Polygon: 
    name = None
    dimension = None
    nodes = list()
    transport = None

    def __init__(self, name, dimension, transport):
        self.name = name 
        self.dimension = dimension
        self.transport = transport
        self.reset()

    def Show_Details(self):
        print("Name:",self.name,"\nDimension:",len(self.nodes))
        print("\nNodes:")
        for n in self.nodes:
            n.Show_Details()

    def append_node(self):
        self.nodes.append(Node(len(self.nodes)))

    def set_node(self, pos, sample) :
        self.nodes[pos].load_sample(sample)

    def get_node(self, pos) :
        return self.nodes[pos]

    def reset(self):
        self.nodes = [Node() for i in range(self.dimension)]

    def get_timeline(self) :
        rslt = list()
        length = self.transport.track_length()
        for i in range(0,self.dimension) :
            info = dict()
            info["time"] = int((i*length)/self.dimension)   #Time position
            info["node"] = self.nodes[i]     #Node
            rslt.append(info)
        return rslt