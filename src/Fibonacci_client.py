#! /user/bin/env python

import rospy
from actionlib import SimpleActionServer
from my_packge.msg import FibonacciAction, FibonacciFeedback, FibonacciResult

class fibonacci_client:
    def __init__(self,name):
        # To do!
        self.action_client=SimpleActionClient('fibonacci_server',FibonacciAction)
        self.action_client.wait_for_server()

        goal=FibonacciGoal(order=20)
        self.action_client.send_goal(goal)
        self.action_client.wait_for_result()

        result= self.action_client.get_result()
        rospy.loginfo('[Fibonacci Client] Result:{}'.format(','.join([str(n)for n in result.
        sequence])))

if __name=='__main__':
    print "Startin Ros Fibonacci Server module"
    rospy.init_node('fibonacci_server', anonymout=True, log_level=rospy.DEBUG)
    fib=fibonacci_server('fibonacci_server')
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down Ros Fibonacci Server module"
