#! /usr/bin/python3
# -*- coding: utf-8 -*-

from polygon import Polygon
from node import Node
from sample import Sample
from transport import Transport
from poly_container import PolyContainer
from pydub.playback import play
from pydub import AudioSegment

transport = Transport(120)
pc = PolyContainer(transport)
transport.set_polycontainer(pc)

poly = pc.new("test", 5)
xylo = Sample("Samples/Xylophone.wav")
poly.set_node(0, xylo)
poly.set_node(1, xylo)
poly.set_node(2, xylo)
poly.set_node(4, xylo)

print("Length = ", transport.track_length())

transport.generate_sound()
transport.play_loop()

# track = AudioSegment.silent(duration = 2000)
# xylo = AudioSegment.from_wav("Samples/Xylophone.wav")
# track = track.overlay(xylo)
# play(track)

