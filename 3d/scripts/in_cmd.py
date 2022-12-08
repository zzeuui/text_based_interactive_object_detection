#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def input_cmd():
    pub = rospy.Publisher("text_command", String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        print("You:", end="")
        cmd = input()

        if len(cmd) > 0:
            pub.publish(cmd)
        rate.sleep()


if __name__=='__main__':
    rospy.init_node('in_cmd', anonymous=False)

    try:
        input_cmd()

    except rospy.ROSInterruptException:
        pass



