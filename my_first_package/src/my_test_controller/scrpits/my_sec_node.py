#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("second_node")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.logerr("hehe")
        rate.sleep()