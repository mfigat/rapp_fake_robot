#!/usr/bin/env python

import subprocess
import rospy
import urllib2
import os
import time
from rapp_fake_robot.srv import Say, Record, RecognizeWord

def rapp_say(text):
    rospy.wait_for_service('rapp_say')
    try:
        textToSpeech = rospy.ServiceProxy('rapp_say', Say)
        resp1 = textToSpeech(text, "english")
        return resp1.response
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def rapp_record(time_arg):
    rospy.wait_for_service('rapp_record')
    try:
        record = rospy.ServiceProxy('rapp_record', Record)
        resp1 = record(time_arg)
        return resp1.recordedFileDest
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
