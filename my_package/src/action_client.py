#! /usr/bin/env python3

import sys
import rospy
import actionlib
from my_package.msg import FibonacciAction, FibonacciGoal

def fibonacci_client(x):
  rospy.init_node('fibonacci_client')
  try:
    client = actionlib.SimpleActionClient('fibonacci', FibonacciAction)
    client.wait_for_server()
    goal = FibonacciGoal(order=x)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()
  except rospy.ROSInterruptException:
    print("program interrupted before completion", file=sys.stderr)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    x = int(sys.argv[1])
  else:
    print("%s [x]"%sys.argv[0])
    sys.exit(1)
  print("Result:", ', '.join([str(n) for n in fibonacci_client(x).sequence]))
