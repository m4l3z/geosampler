#! /usr/bin/python3
# -*- coding: utf-8 -*-

from audio.polygon import Polygon
from audio.node import Node
from audio.sample import Sample
from audio.transport import Transport
from audio.poly_container import PolyContainer
from pydub.playback import play
from pydub import AudioSegment

transport = Transport(100)
pc = PolyContainer(transport)
transport.set_polycontainer(pc)

xylo = Sample("Samples/Xylophone.wav")

poly = pc.new("test", 5)
poly.set_node(0, xylo)
poly.set_node(1, xylo)
poly.set_node(2, xylo)
poly.set_node(4, xylo)

poly2 = pc.new("test", 7)
poly2.set_node(0, xylo)
poly2.set_node(1, xylo)
poly2.set_node(5, xylo)
poly2.set_node(6, xylo)

print("Length = ", transport.track_length())

transport.generate_sound()
transport.play_loop()

