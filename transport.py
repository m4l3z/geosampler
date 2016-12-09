#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pydub import AudioSegment
from pydub.playback import play
from sample import Sample

class Transport :
	bpm = 120
	track = None
	polys = None

	def __init__(self, bpm) :
		self.bpm = bpm

	def set_polycontainer(self, polys) :
		self.polys = polys

	def track_length(self) :
		return 240000/self.bpm

	def generate_sound(self) :
		self.track = AudioSegment.silent(duration = self.track_length())
		timeline = list()
		for p in self.polys :
			timeline += p.get_timeline()
		for n in timeline :
			print(n)
			if n["node"].has_sample() :
				self.track = self.track.overlay(n["node"].to_audiosegment(), position = n["time"])


	def play(self) :
		play(self.track)

	def play_loop(self) :
		while True :
			self.play()


