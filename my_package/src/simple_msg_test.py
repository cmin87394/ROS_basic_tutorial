#!/usr/bin/env python3

import rospy
from my_package.msg import MsgTutorial

def simple_msg():
  rospy.init_node('simple_msg')
  pub = rospy.Publisher('my_topic', MsgTutorial, queue_size=1)
  data = MsgTutorial()
  rospy.loginfo("Publish start")
  while not rospy.is_shutdown():
    data.stamp = rospy.Time.now()
    data.name = 'Steve'
    data.age = 25
    data.height = 175.5
    pub.publish(data)
    rospy.Rate(1).sleep()

if __name__=="__main__":
   simple_msg()
