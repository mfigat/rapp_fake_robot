#!/usr/bin/env python
# -*- coding: latin-1 -*-

import subprocess
import rospy
import roslib
import rospkg
import urllib2
import os
import time
import unittest
import sys
from rapp_fake_robot.srv import Say, Record, RecognizeWord, SpeechRecognitionSphinx4Srv, SpeechRecognitionSphinx4ConfigureSrv, SpeechRecognitionSphinx4TotalSrv, SpeechRecognitionSphinx4TotalSrvResponse, SpeechRecognitionSphinx4TotalSrvRequest

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
