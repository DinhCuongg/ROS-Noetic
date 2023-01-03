#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

def call_set_pen(r,g,b,width,off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen",SetPen)
        reponse = set_pen(r,g,b,width,off)
    except rospy.ServiceException as e:
        rospy.logerr(e)
def callback_controll(msg: Pose):
    cmd = Twist()
    if msg.x <= 2.0 or msg.x >= 9.0 or msg.y <= 2.0 or msg.y >= 9.0:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
        call_set_pen(0,200,0,3,0)
    else :
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
        call_set_pen(0,0,200,3,0)
    pub.publish(cmd)

if __name__ == '__main__':
    rospy.init_node("test_controll")
    ser  = rospy.wait_for_service("/turtle1/set_pen")
    call_set_pen(200,0,0,3,0)
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=callback_controll)
    rospy.spin()