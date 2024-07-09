#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty
from turtlesim.msg import Pose

def clear_client():
  rospy.init_node('clear_client')
  rospy.wait_for_service('clear')
  rospy.Subscriber('/turtle1/pose', Pose, callback)
  rospy.spin()

def callback(msg):
  global initial, total_distance, last_x, last_y
  x = msg.x
  y = msg.y

  if initial == True:
    initial = False
  else:
    total_distance += ((last_x-x)**2 + (last_y-y)**2)**0.5
  rospy.loginfo(total_distance)

  try:
    if total_distance >= 5.0:
      clear = rospy.ServiceProxy('clear', Empty)
      clear()
      total_distance = 0.0
    else:
      pass
  except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

  last_x = x
  last_y = y

if __name__ == "__main__":
  rospy.loginfo("Requesting /clear service")
  initial = True
  total_distance = 0.0
  clear_client()