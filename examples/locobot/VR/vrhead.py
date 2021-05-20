#!/usr/bin/env python
import rospy
import tf
from std_msgs.msg import Float64
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped


def callback(data):
    explicit_quat = [data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w]
    your_euler = tf.transformations.euler_from_quaternion(explicit_quat)
    # print(your_euler)
    
    pub_pan = rospy.Publisher('/pan/command', Float64, queue_size=10)
    pub_tilt = rospy.Publisher('/tilt/command', Float64, queue_size=10)

    pub_pan.publish(your_euler[2])
    pub_tilt.publish(your_euler[1])






def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("vr/head", PoseStamped, callback)

    rospy.spin() #run forever

if __name__ == '__main__':
     listener()
