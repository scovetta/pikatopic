#!/usr/bin/env python

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))


from pikatopic import PikaTopic
import pikatopic

#
# this demonstrates setting the default host, which would be kind of an odd case
#
# pikatopic.DEFAULT_HOST = '172.17.0.2'

def handler(routing_key, message, message_data):
    if message_data:
        print("%r data=%r" % (routing_key, message_data))
    else:
        print("%r text=%r" % (routing_key, message))
    return "exit" != message


with PikaTopic(verbose=True) as pt:
    pt.listen(handler, ['#'])


