#! /user/bin/env python

import rospy
from actionlib import SimpleActionServer
from my_packge.msg import FibonacciAction, FibonacciFeedback, FibonacciResult

class fibonacci_server:
    def __init__(self,name):
        # To do!
if __name=='__main__':
    print "Startin Ros Fibonacci Server module"
    rospy.init_node('fibonacci_server', anonymout=True, log_level=rospy.DEBUG)
    fib=fibonacci_server('fibonacci_server')
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down Ros Fibonacci Server module"
