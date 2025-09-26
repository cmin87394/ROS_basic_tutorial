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

    #0.0 < P < 10.0, 0.0 < I < 3.0, 0.0 < D < 1.0
    if P_gain < 0.0:
      P_gain = 0.0
      rospy.set_param('P', P_gain)
      rospy.loginfo("Minimum P : 0")
    elif P_gain > 10.0:
      P_gain = 10.0
      rospy.set_param('P', P_gain)
      rospy.loginfo("Maximum P : 10")

    if I_gain < 0.0:
      I_gain = 0.0
      rospy.set_param('I', I_gain)
      rospy.loginfo("Minimum I : 0")
    elif I_gain > 3.0:
      I_gain = 3.0
      rospy.set_param('I', I_gain)
      rospy.loginfo("Maximum I : 3")

    if D_gain < 0.0:
      D_gain = 0.0
      rospy.set_param('D', D_gain)
      rospy.loginfo("Minimum D : 0")
    elif D_gain > 1.0:
      D_gain = 1.0
      rospy.set_param('D', D_gain)
      rospy.loginfo("Maximum D : 1")

    rospy.loginfo("P: %f, I: %f, D: %f"%(P_gain, I_gain, D_gain))
    rospy.Rate(1).sleep()

if __name__=="__main__":
   simple_param()
