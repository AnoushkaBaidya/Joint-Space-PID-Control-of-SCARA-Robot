import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import math
import numpy as np
from geometry_msgs.msg import Pose
import matplotlib.pyplot as plt

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.fwk,
            10)
        self.subscription  # prevent unused variable warning
        self.x=[]

        # Create the publisher. This publisher will publish an Image
        # to the video_frames topic. The queue size is 10 messages.
        self.publisher_ = self.create_publisher(Pose,'fwd', 1)

    def fwk(self, msg):
        theta1 = msg.position[0]
        theta2 = msg.position[1]
        theta3 = msg.position[2]
        a=[2,1,0]
        theta=[theta1,theta2,theta3]
        d = [0,0,1]
        alpha = [0,0,0]
        A1 = np.array([[math.cos(theta[0]), -math.sin(theta[0])*math.cos(alpha[0]), math.sin(theta[0])*math.sin(alpha[0]), a[0]*math.cos(theta[0])], [math.sin(theta[0]),math.cos(theta[0])*math.cos(alpha[0]),-math.cos(theta[0])*math.sin(alpha[0]), a[0]*math.sin(theta[0])], [0, math.sin(alpha[0]), math.cos(alpha[0]), d[0]], [0,0,0,1]])
        A2 = np.array([[math.cos(theta[1]), -math.sin(theta[1])*math.cos(alpha[1]), math.sin(theta[1])*math.sin(alpha[1]), a[1]*math.cos(theta[1])], [math.sin(theta[1]),math.cos(theta[1])*math.cos(alpha[1]),-math.cos(theta[1])*math.sin(alpha[1]), a[1]*math.sin(theta[1])], [0, math.sin(alpha[1]), math.cos(alpha[1]), d[1]], [0,0,0,1]])
        A3 = np.array([[math.cos(theta[2]), -math.sin(theta[2])*math.cos(alpha[2]), math.sin(theta[2])*math.sin(alpha[2]), a[2]*math.cos(theta[2])], [math.sin(theta[2]),math.cos(theta[2])*math.cos(alpha[2]),-math.cos(theta[2])*math.sin(alpha[2]), a[2]*math.sin(theta[2])], [0, math.sin(alpha[2]), math.cos(alpha[2]), d[2]], [0,0,0,1]])
        temp = np.matmul(A1,A2)
        T = np.matmul(temp,A3)
        print(T)

        ans = Pose()    
        ans.position.x= T[0,3]
        ans.position.y= T[1,3]
        ans.position.z= T[2,3]

        #publishing on topic 
        self.publisher_.publish(ans)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()