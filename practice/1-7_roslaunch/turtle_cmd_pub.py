#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def turtle_cmd_pub():
  rospy.init_node('turtle_cmd_pub')
  pub1 = rospy.Publisher('/turtlesim1/turtle1/cmd_vel', Twist, queue_size=1)
  pub2 = rospy.Publisher('/turtlesim2/turtle1/cmd_vel', Twist, queue_size=1)
  pub3 = rospy.Publisher('/turtlesim3/turtle1/cmd_vel', Twist, queue_size=1)
  data = Twist()
  while not rospy.is_shutdown():
    # Turtle1
    data.linear.x = 1.0
    data.angular.z = 0.5
    pub1.publish(data)
    
    # Turtle2
    data.linear.x = 1.0
    data.angular.z = 0.3
    pub2.publish(data)

    # Turtle3
    data.linear.x = 1.0
    data.angular.z = -0.5
    pub3.publish(data)

    rospy.Rate(1).sleep()

if __name__ == '__main__':
  try:
    turtle_cmd_pub()
  except rospy.ROSInterruptException:
    pass
