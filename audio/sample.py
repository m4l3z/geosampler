#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pydub import AudioSegment
from pydub.playback import play

class Sample :
	path = ""
	sound = None

	def __init__(self, p) :
		self.path = p
		self.sound = AudioSegment.from_wav("Samples/Xylophone.wav")
	
	def play(self) :
		play(self.sound)
