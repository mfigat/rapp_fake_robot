#!/usr/bin/env python

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

def rapp_speech_detection(path, audio_source, user):
    try:

        rospack = rospkg.RosPack()
        aux = rospack.get_path('rapp_testing_tools') + '/test_data'

        req = SpeechRecognitionSphinx4TotalSrvRequest()
        req.language = 'el'
        req.words = ['ναι', 'όχι']
        req.grammar = []
        req.sentences = req.words
        req.path = aux + '/nao_wav_d05_a1.wav'
        req.audio_source = 'nao_wav_4_ch'
        req.user = 'rapp'
        record = rospy.ServiceProxy('/rapp/rapp_speech_detection_sphinx4/batch_speech_to_text', SpeechRecognitionSphinx4TotalSrv)
        resp1 = record(req)
        print "Error " + resp1.error
        if ( resp1.words != ['ναι', 'όχι', 'ναι'] ):
            print "Word miss-match"
        return resp1.words
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e