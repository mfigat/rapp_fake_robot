#!/usr/bin/env python

import subprocess
import rospy
import urllib2
import os
import time
import rospkg
from os.path import expanduser
from rapp_fake_robot.srv import Say, Record, RecognizeWord


file_name="/path_to_sound_recorded/sound.ogg"
script_path=""

def handle_say(req):
	print "NAO says in %s: %s" % (req.language, req.request)
	subprocess.check_call([script_path+"say.sh", req.request])
	return 1

def handle_record(req):
	print "NAO records for %s seconds" % req.recordingTime
	home_path = expanduser("~")
	path= home_path + file_name
	subprocess.check_call([script_path+"record.sh", str(req.recordingTime), path])
	return path

def fake_nao_comm():
	rospack = rospkg.RosPack()
	global script_path
	script_path = rospack.get_path('rapp_fake_robot') + "/scripts/"
	rospy.init_node('fake_nao_comm')
	s = rospy.Service('rapp_say', Say, handle_say)
	s = rospy.Service('rapp_record', Record, handle_record)
	#s = rospy.Service('rapp_get_recognized_word', RecognizeWord, handle_recognize_word)
	print "Ready to synthesize words and record sound"
	rospy.spin()

if __name__ == "__main__":
	fake_nao_comm()
