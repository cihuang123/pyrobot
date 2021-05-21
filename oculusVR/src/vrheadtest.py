#!/usr/bin/env python
import rospy
import tf
from std_msgs.msg import Float64
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped


class subvrandpub(object):
    def __init__(self):
        self.sub = rospy.Subscriber("vr/head", PoseStamped, self.callback)
        self.test = false
        # self.pub_pan = rospy.Publisher('/pan/command', Float64, queue_size=10)
        # self.pub_tilt = rospy.Publisher('/tilt/command', Float64, queue_size=10)


    def callback(self, data):
        # explicit_quat = [data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w]
        # your_euler = tf.transformations.euler_from_quaternion(explicit_quat)
        # print(your_euler)
        
        # self.pub_pan.publish(your_euler[2])
        # self.pub_tilt.publish(your_euler[1])
        self.test = true
        assert self.test == true
    
if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    SUB = subvrandpub()
    rospy.spin() #run forever