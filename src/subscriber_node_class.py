#!/user/bin/env python
# subscriber_node.py

import rospy
from geometry_msgs.msg import Point

class subscriber_node:

	def _init_(self):
		self.sub=rospy.Subscriber('robot_location',Point, self.callback)
		rospy.spin()
	
	def callback(self,location):
		rospy.loginfo("Recieved location:(0),(1)".format(location.x,location.y));

	
	def my_subscriber_method():
		rospy.init_node('robot_location_listener')
		rospy.Subscriber('robot_location',Point, my_callback)
		rospy.spin()
	
if _name_ =='_main_':
 	try:
		rospy.init_node('robot_location_listener')
		sn=subscriber_node()
	except	rospy.RoSInterrruptException:
		pass
