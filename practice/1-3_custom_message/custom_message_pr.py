#!/usr/bin/env python3

import rospy
from my_package.msg import MsgTurtle
from turtlesim.msg import Pose

def simple_msg():
  global pub
  rospy.init_node('simple_msg_turtle')
  pub = rospy.Publisher('my_topic', MsgTurtle, queue_size=1)
  rospy.Subscriber('/turtle1/pose', Pose, callback)
  rospy.loginfo("Publish start")
  rospy.spin()

def callback(msg):
  x = msg.x
  y = msg.y
  
  data = MsgTurtle()
  data.stamp = rospy.Time.now()
  data.distance = min(x, 11.0-x, y, 11.0-y)
  # 1: hit the wall(0 or 11), 2: warning(<2 or >9), 3: good(>2 or <9)
  if (x<=0.0) or (x>=11.0) or (y<=0.0) or (y>=11.0):
    data.status = 'hit the wall'

  elif (x>0.0 and x<=2.0) or (x>=9.0 and x<11.0) or (y>0.0 and y<=2.0) or (y>=9.0 and y<11.0):
    data.status = 'warning'

  else:
    data.status = 'good'

  pub.publish(data)
  
if __name__=="__main__":
   simple_msg()
