#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalStatusArray

def callback(msg):
  global goal_status
  if msg.status_list == []:
    goal_status = -1
  else:
    goal_status = msg.status_list[-1].status

def GoalPublisher(current_goal):
  while not rospy.is_shutdown():
    pub.publish(GoalMessage(current_goal))
    rospy.Rate(10).sleep()
    if goal_status == 1:
      break

def GoalMessage(current_goal):
  msg = PoseStamped()
  msg.header.stamp       = rospy.Time.now()
  msg.header.frame_id    = 'map'
  msg.pose.position.x    = current_goal[0]
  msg.pose.position.y    = current_goal[1]
  msg.pose.orientation.z = current_goal[2]
  msg.pose.orientation.w = current_goal[3]
  return msg

def turtlebot_goal_pub():
  global goal_flag
  # [position x, position y, orientation z, orientation w]
  goal_list = [[1.76, 0.99, 0.0, 1.0], [0.1, 1.9, 0.0, 1.0], [-0.7, -1.77, 0.0, 1.0]]
  goal_flag = True
  i = 0

  while not rospy.is_shutdown():
    if goal_flag:
      goal_flag = False
      current_goal = goal_list[i]
      GoalPublisher(current_goal) 
      goal_x = current_goal[0]
      goal_y = current_goal[1]
      rospy.loginfo("Starting path planing to (%.1f,%.1f) !!"%(goal_x,goal_y))

    if goal_status == 3:
      rospy.loginfo("Goal reached !!")
      goal_flag = True
      i += 1

    if i == len(goal_list):
      rospy.loginfo("All path planning complete.")
      break
    
    rospy.Rate(10).sleep()


if __name__ == '__main__':
  rospy.init_node('turtlebot_goal_pub')
  pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
  rospy.Subscriber('/move_base/status', GoalStatusArray, callback)
  try:
    turtlebot_goal_pub()
  except rospy.ROSInterruptException:
    pass
