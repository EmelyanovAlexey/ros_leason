#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import cv2
    
class Turtle(Node):
    def __init__(self):
        super().__init__('depth_image_Node')
        self.pose_sub = self.create_subscription(Image, '/depth/image', self.callback, 1)

    def callback(self, data):
        try:
            bridge = CvBridge()
            img = bridge.imgmsg_to_cv2(data,desired_encoding="passthrough")

        except CvBridgeError as e:
            print(e)
    
        cv2.imshow('image', img)
        cv2.waitKey(1)
          

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = Turtle()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
