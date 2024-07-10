#!/usr/bin/env python3

import rospy
import actionlib
from my_package.msg import FibonacciAction, FibonacciFeedback, FibonacciResult

feedback = FibonacciFeedback()
result = FibonacciResult()

def execute_cb(goal):
  success = True
  feedback.sequence = []
  feedback.sequence.append(0)
  feedback.sequence.append(1)
  rospy.loginfo("%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i"%('fibonacci', goal.order, feedback.sequence[0], feedback.sequence[1]))
  for i in range(1, goal.order):
    if server.is_preempt_requested():
      rospy.loginfo("%s: Preempted"%'fibonacci')
      server.set_preempted()
      success = False
      break
    feedback.sequence.append(feedback.sequence[i] + feedback.sequence[i-1])
    server.publish_feedback(feedback)
    rospy.loginfo("feedback: %s"%feedback.sequence)
    rospy.Rate(1).sleep()
  if success:
    result.sequence = feedback.sequence
    rospy.loginfo("%s: Succeeded"%'fibonacci')
    server.set_succeeded(result)

def fibonacci_server():
  global server
  rospy.init_node('fibonacci_server')
  server = actionlib.SimpleActionServer('fibonacci', FibonacciAction, execute_cb=execute_cb, auto_start=False)
  server.start()
  rospy.spin()

if __name__ == '__main__':
  fibonacci_server()
