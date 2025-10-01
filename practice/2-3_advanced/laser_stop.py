#!/usr/bin/env python3

import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

def Callback(data):
  filtered_data = np.where(np.array(data.ranges)<0.5)
  if np.array(filtered_data).size!=0:
    print("Warning")
    pub.publish("Warning")
  else:
    print("Good")
        
def laser_stop():
  global pub
  rospy.init_node("Laser_stop")
  pub = rospy.Publisher("warning", String, queue_size=1)
  rospy.Subscriber("scan_filtered", LaserScan, Callback)
  rospy.spin()

if __name__=="__main__":
  laser_stop()
