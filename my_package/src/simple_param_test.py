#!/usr/bin/env python3

import rospy

def simple_param():
  rospy.init_node('simple_param')
  rospy.set_param('P', 1.0)
  rospy.set_param('I', 1.0)
  rospy.set_param('D', 1.0)

  while not rospy.is_shutdown():
    P_gain = rospy.get_param('P')
    I_gain = rospy.get_param('I')
    D_gain = rospy.get_param('D')
    rospy.loginfo("P: %f, I: %f, D: %f"%(P_gain, I_gain, D_gain))
    rospy.Rate(1).sleep()

if __name__=="__main__":
   simple_param()
