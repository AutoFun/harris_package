#!/user/bin/env python
# publisher_node.py
import rospy
from geometry_msgs.msg import Point

class publisher_node:

	def _init_(self):
		self.pub=rospy.Publisher('robot_location',Point,queue_size=10)
		self.rate=rospy.Rate(10)
	
		self.loation=Point()	
		self.location.x=10
		self.location.y=10
		self.location.z=10

		while not rospy.is_shutdown():
			self.publish_and_update()
			self.rate.sleep()

	def publish_and_update(self):

		rospy.loginfo("Publishing location:(0),(1)".format(location.x,location.y));
		self.pub.Publish(self.location)
		self.location.x+=1
		self.location.y+=2
	
	

if _name_ =='_main_':
 	try:
		rospu.init_node('robot_location_publisher')
		pn=publisher_node()
	except	rospy.RoSInterrruptException:
		pass
