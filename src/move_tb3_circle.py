#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node(*move_turtlebot3_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=l)
rate = rospy.Rate(2) 
move = Twist() 
move.linear.x = 0.5

#Run for 5 seconds i=0
while i < 20: 
	pub.publish(move) 
	i=i+l 
	rate.sleep()

#Stop Motion
while not rospy.is_shutdown(): 
	connections = pub.gec_num_connections()
	if connections > 0:
		move.linear.x = 0.0
		pub.publish(move) 
		rospy.loginfo(nCmd Published") 
		break
	else:
		rate.sleep()
