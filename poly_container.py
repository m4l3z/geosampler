#! /usr/bin/python3
# -*- coding: utf-8 -*-

from polygon import Polygon

class PolyContainer :
	polys = list()
	transport = None
	i = 0

	def __init__(self, transport) :
		self.transport = transport

	def new(self, name, dimension) :
		poly = Polygon(name, dimension, self.transport)
		self.polys.append(poly)
		return poly

	def __iter__(self) :
		return self.polys.__iter__()

	def __next__(self) :
		return self.polys.__next__()


