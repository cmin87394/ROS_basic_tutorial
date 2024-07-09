#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose

def callback(data):
  x = data.x
  y = data.y
  
  pose_string = "x: %s, y: %s"%(x, y)

  # print
  rospy.loginfo(pose_string)

  # publish
  pub.publish(pose_string)
    
def listener():
  global pub
  rospy.init_node('pose_listener')
  pub = rospy.Publisher('turtle_pose', String, queue_size=1)
  rospy.Subscriber('/turtle1/pose', Pose, callback)
  rospy.spin()

if __name__ == '__main__':
  listener()
    