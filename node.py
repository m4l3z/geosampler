#! /usr/bin/python3
# -*- coding: utf-8 -*-

class Node: 
    sample = None

    def __init__(self):
    	pass

    def load_sample(self, sample):
        self.sample = sample

    def remove_sample(self):
        self.sample = None

    def has_sample(self) :
    	if self.sample == None :
    		return False
    	else :
    		return True

    def to_audiosegment(self) :
    	return self.sample.sound