#! /usr/bin/env python3

import numpy as np
import rospy
import actionlib
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from my_package.msg import TurtleGoalAction, TurtleGoalFeedback, TurtleGoalResult

feedback = TurtleGoalFeedback()
result = TurtleGoalResult()

def execute_cb(goal):
  success = True
  rospy.loginfo("Executing, creating path planner of order (%f,%f)"%(goal.x,goal.y))
  data = Twist()
  
  while not rospy.is_shutdown():
    if server.is_preempt_requested():
      rospy.loginfo("turtle_goal: Preempted")
      server.set_preempted()
      success = False
      break

    goal_dis = ((goal.x-x)**2 + (goal.y-y)**2)**0.5
    feedback.distance = goal_dis
    server.publish_feedback(feedback)
    rospy.loginfo("goal distance: %f"%feedback.distance)
    if goal_dis <= 0.05:
      break

    reference_theta = np.arctan2((goal.y-y),(goal.x-x))
    theta_error = reference_theta - theta
    if abs(theta_error) > 0.17 and abs(theta_error) < (6.28-0.17): # 0.17 rad (10 deg)
      if (abs(theta_error) <= 3.14 and theta_error >= 0) or (abs(theta_error) > 3.14 and theta_error < 0):
        data.linear.x = 0.0
        data.angular.z = 0.5
        print('Turn left')
      else:
        data.linear.x = 0.0
        data.angular.z = -0.5
        print('Turn right')
    else:
      data.linear.x = 0.5
      data.angular.z = 0.0
      print('Go straight')
    pub.publish(data)
    rospy.Rate(10).sleep()
  
  if success:
    result.is_reached = True
    rospy.loginfo("Goal: Reached")
    rospy.loginfo("Current: (%f,%f)"%(x,y))
    server.set_succeeded(result)

def callback(msg):
  global x, y, theta
  x = msg.x
  y = msg.y
  theta = msg.theta

def turtle_goal_server():
  global pub, server
  rospy.init_node('turtle_goal_server')
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
  rospy.Subscriber('/turtle1/pose', Pose, callback)
  server = actionlib.SimpleActionServer('turtle_goal', TurtleGoalAction, execute_cb=execute_cb, auto_start=False)
  server.start()
  rospy.spin()

if __name__ == '__main__':
  turtle_goal_server()
