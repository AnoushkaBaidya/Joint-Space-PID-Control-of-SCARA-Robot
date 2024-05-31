import sys
from ser_interfaces.srv import Position
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState
import pickle as pkl

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(Position, 'serial_killer')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Position.Request()
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.fwk,
            10)
        self.subscription 
        self.publisher_ = self.create_publisher(Float64MultiArray,'/forward_effort_controller/commands', 10)
        timer_period = 0.5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback) #Freq is at joint/states
        self.u1_ref = 0
        self.u2_ref = 0
        self.u3_ref = 0 
        self.e1_prev = 0
        self.e2_prev = 0
        self.e3_prev = 0
        self.data_u1 = []

    def fwk(self, msg):
        u1 = msg.position[0]
        u2 = msg.position[1]
        u3 = msg.position[2]
        self.data_u1.append(u1)
        Kp=5
        Kd=7
        dt=0.01 # Frequency at which /joint_states is published
        e_1 = self.u1_ref-u1
        e_2 = self.u2_ref-u2
        e_3 = self.u3_ref-u3
        e_1_dot = e_1-self.e1_prev/dt
        e_2_dot = e_2-self.e2_prev/dt
        e_3_dot = e_3-self.e3_prev/dt
        updated_u1 = Kp*e_1+Kd*e_1_dot
        updated_u2 = Kp*e_2+Kd*e_2_dot
        updated_u3 = Kp*e_3+Kd*e_3_dot
        e1_prev = e_1
        e2_prev = e_2
        e3_prev = e_3

        my_msg = Float64MultiArray()  
        my_msg.data = [updated_u1,updated_u2,updated_u3]
        self.publisher_.publish(my_msg)

    def send_request(self,data):
        #print(self.req.data)
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.result = self.future.result()
        self.u1_ref = self.result.u1_ref
        self.u2_ref = self.result.u2_ref
        self.u3_ref = self.result.u3_ref

def main():
    rclpy.init()
    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(int(sys.argv[1]))
    rclpy.spin(minimal_client)
    minimal_client.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
