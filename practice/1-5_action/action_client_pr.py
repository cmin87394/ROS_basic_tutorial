#! /usr/bin/env python3

import sys
import rospy
import actionlib
from my_package.msg import TurtleGoalAction, TurtleGoalGoal

def turtle_goal_client(x, y):
  rospy.init_node('turtle_goal_client')
  try:
    client = actionlib.SimpleActionClient('turtle_goal', TurtleGoalAction)
    client.wait_for_server()
    goal = TurtleGoalGoal(x=x,y=y)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()
  except rospy.ROSInterruptException:
    print("program interrupted before completion", file=sys.stderr)

if __name__ == '__main__':
  if len(sys.argv) == 3:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
  else:
    print("%s [x y]"%sys.argv[0])
    sys.exit(1)
  print("Result: %s"%str(turtle_goal_client(x, y).is_reached))
