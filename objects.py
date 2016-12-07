#!/usr/bin/env python3

''' 
Definition of polygons and nodes. Objects and methods. 
''' 

class Node: 
    sample = "No sample" 
    def __init__(self, number):
        self.number = number
    def Load_Sample(self, path):
        self.sample = path 
    def Remove_Sample(self):
        self.sample = "No sample"
    def Show_Details(self):
        print "Number:",self.number,"\nSample:",self.sample


class Polygon: 

    def __init__(self, name, dimension):
        self.name = name 
        self.dimension = dimension
        self.node = [Node(i) for i in range(dimension)]
    def Show_Details(self):
        print "Name:",self.name,"\nDimension:",len(self.node)
        print "\nNodes:"
        for nodes in self.node:
            nodes.Show_Details()
    def Add_Node(self):
        self.node.append(Node(len(self.node)))
    def Reset(self):
        self.node = [Node(i) for i in range(self.dimension)]

polya = Polygon('polya', 2)
polya.node[1].Load_Sample("sample/test.wav")
polya.Add_Node()
polya.Add_Node()
polya.Show_Details()
polya.Reset()
polya.Show_Details()
'''
nodia = Node(0)
nodia.Show_Details()
nodia.Load_Sample("samples/test.wav")
nodia.Show_Details()
'''
