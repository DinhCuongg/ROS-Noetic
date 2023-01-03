#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg : Pose):
    rospy.loginfo("x = " + str(msg.x) + "y = "+ str(msg.y))

if __name__ == '__main__':
    rospy.init_node("my_first_sub")
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback)
    rospy.spin()
