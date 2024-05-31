import rclpy
from rclpy.node import Node
import math
from ser_interfaces.srv import Position

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Position, 'serial_killer', self.inv_callback)

    def inv_callback(self,request,response):
        print(request.data)
        response.u1_ref = 1.57
        response.u2_ref = 1.57
        response.u3_ref = 1.57
      
        print('u1_ref =', response.u1_ref, 'u2_ref =', response.u2_ref,  'u3_ref =', response.u3_ref)     
        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
