#!/usr/bin/env python

import sys
import rospy
from fake_nao_wrapper import *

def usage():
    return "%s [text recording_time]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        text = sys.argv[1]
        time = (int)(sys.argv[2])
        print "Time= %s" % time
    else:
        print usage()
        sys.exit(1)
    print "Text to synthesize %s\nResponse: %s\n"%(text, rapp_say(text))
    print "Recording sound for %s seconds to %s file" % (time, rapp_record(time))