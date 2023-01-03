#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("hehe")
    rospy.logwarn("haha")
    rospy.logerr("cuong")

    rospy.sleep(1.0)
    rospy.logerr("End")