#!/usr/bin/env python3

import rospy
import cv2
import numpy as np

from std_msgs.msg import String
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes

class show:
    def __init__(self):

        self.boxes = None
        self.cmd = None
        
        self.flag = False

        self.height = 720
        self.width = 1280

        self.obj_sub = rospy.Subscriber("/darknet_ros/bounding_boxes",
                                        BoundingBoxes, self.set_obj)
        self.cmd_sub = rospy.Subscriber("/text_command", 
                                        String, self.set_cmd)
        self.img_sub =  rospy.Subscriber("/camera/color/image_raw", 
                                        Image, self.set_img)

    def set_obj(self, data):
        self.boxes = data.bounding_boxes

    def set_cmd(self, data):
        self.cmd = data.data
        self.flag = False

    def set_img(self, data):

        obj_num = 0
        
        img = np.frombuffer(data.data, dtype=np.uint8)
        img = img.reshape(self.height, self.width, -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.boxes is not None:
            for box in self.boxes:
                if box.probability > 0.5:
                    x1 = box.xmin
                    y1 = box.ymin
                    x2 = box.xmax
                    y2 = box.ymax

                    label = box.Class

                    if self.cmd == label:
                        color = (255, 0, 0)
                        obj_num += 1
                        if not self.flag:
                            print("COM: Which one?")
                            self.flag = True
                    else:
                        color = (0, 255, 255)

                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                    cv2.putText(img, label, (x1, y1), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow('output', img)
        cv2.waitKey(3)

if __name__=='__main__':
    rospy.init_node('show', anonymous=False)
    show()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo('shutting down')

    cv2.destroyAllWindows()
