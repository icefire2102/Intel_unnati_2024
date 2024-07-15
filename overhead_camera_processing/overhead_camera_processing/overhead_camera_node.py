import os
import time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class OverheadCameraNode(Node):
    def __init__(self):
        super().__init__('overhead_camera_node')
        
        # Declare the parameter
        self.declare_parameter('camera_id', 1)
        self.camera_id = self.get_parameter('camera_id').get_parameter_value().integer_value
        self.bridge = CvBridge()

        # Directory to save images
        self.image_save_directory = "/home/riyanshi/turtlebot3_ws/images"
        
        # Create directory if it doesn't exist
        if not os.path.exists(self.image_save_directory):
            os.makedirs(self.image_save_directory)

        # Subscribe to image topic
        self.image_subscriber = self.create_subscription(
            Image,
            f'/camera{self.camera_id}/image_raw',
            self.image_callback,
            10
        )
        self.get_logger().info(f"Overhead Camera Node for camera {self.camera_id} has been started.")

    def image_callback(self, msg):
        try:
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

            # Save images in a specific directory
            image_save_path = os.path.join(self.image_save_directory, f"camera_{self.camera_id}_{int(time.time())}.png")
            cv2.imwrite(image_save_path, gray_image)

            # Log saved image path
            self.get_logger().info(f"Saved image: {image_save_path}")

            # Display the image
            cv2.imshow(f"Camera {self.camera_id}", gray_image)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f'Error in image_callback: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    node = OverheadCameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

