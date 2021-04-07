import rospy
from sensor_msgs.msg import LaserScan


def callback(msg):
	print(msg.ranges[0])

rospy.init_node('read_lidar')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
