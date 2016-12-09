#! /usr/bin/python3
# -*- coding: utf-8 -*-

from polygon import Polygon
from node import Node
from sample import Sample

# polya = Polygon('polya', 2)
# polya.node[1].Load_Sample("sample/test.wav")
# polya.Add_Node()
# polya.Add_Node()
# polya.Show_Details()
# polya.Reset()
# polya.Show_Details()


sample = Sample("Samples/Xylophone.wav")
sample.play()

'''
nodia = Node(0)
nodia.Show_Details()
nodia.Load_Sample("samples/test.wav")
nodia.Show_Details()
'''