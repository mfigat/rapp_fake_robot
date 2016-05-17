#!/usr/bin/env python

import sys
import rospy
from rapp_fake_robot.srv import Say, Record, RecognizeWord

def say_client(text):
    rospy.wait_for_service('rapp_say')
    try:
        textToSpeech = rospy.ServiceProxy('rapp_say', Say)
        resp1 = textToSpeech(text, "english")
        return resp1.response
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def record_client(time_arg):
    rospy.wait_for_service('rapp_record')
    try:
        record = rospy.ServiceProxy('rapp_record', Record)
        resp1 = record(time_arg)
        return resp1.recordedFileDest
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

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
    print "Text to synthesize %s Response %s"%(text, say_client(text))
    #print "Recording sound for %s seconds in %s file" % (time, record_client(time))
    sys.exit(1)
