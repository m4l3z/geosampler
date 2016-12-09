#! /usr/bin/python3
# -*- coding: utf-8 -*-

from node import Node
from lxml import etree

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

    def show_details(self):
        print("<Polygon dim =",'"', str(self.dimension),'"', " name =" ,self.name,">\n")
        for node in self.nodes:
            if(node.sample == None):
                print("<node></node>\n")
            else:
                print("<node> path ="+node.sample+"</node>\n")
        print("</Polygon>")

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
    
    def save(self): 
        f = open(self.name+".save","w+")
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write("<Polygon dim ="+ '"'+str(self.dimension)+'"'+ " name =" +self.name+">\n")
        for node in self.nodes:
            if(node.sample == None):
                f.write("<node></node>\n")
            else:
                f.write("<node> path ="+node.sample+"</node>\n")
        f.write("</Polygon>")
        f.close()

    def load(self,filename):
        tree = etree.parse(filename)
        for Polygon in tree.xpath("/Polygon"):
            print(Polygon.name)
        


# polya = Polygon("polya",5)
# polya.nodes[1].sample="Samples/Xylophone.wav"
# polya.show_details()
# polya.save()
# polya.load("polya.save")
