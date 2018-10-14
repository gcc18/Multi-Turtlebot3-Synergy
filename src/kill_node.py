#!/usr/bin/env python

import rospy
import commands

if __name__=="__main__":
	commands.getoutput("rosnode kill gazebo_gui")
