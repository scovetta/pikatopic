#!/usr/bin/env python

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))


from pikatopic import PikaTopic

import pikatopic

pikatopic.DEFAULT_HOST = '172.17.0.2'

with PikaTopic(verbose=True) as pt:
    pt.sendText("X", "high")
    pt.sendData("X", ['in between'])
    pt.sendData("X", {'a':123})
    # pt.sendText("X", "exit")

