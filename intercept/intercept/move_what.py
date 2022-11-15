# ros2 launch franka_moveit_config moveit.launch.py robot_ip:=dont-care use_fake_hardware:=true
import rclpy
from rclpy.node import Node
from moveit_msgs.action import MoveGroup
from rclpy.action import ActionServer


class MoveWhat(Node):
    def __init__(self):
        super().__init__('move_what')
        self.tmr = self.create_timer(1., self.timer_callback)
        self._action_server = ActionServer(
            self,
            MoveGroup,
            '/move_action',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        print("Execute Callback")
        toprint = str(goal_handle.request).replace(',',',\n')
        self.get_logger().info("Hello?")
        self.get_logger().info(f"{toprint}")
        # print(goal_handle.request)
        return MoveGroup.Result()

    def timer_callback(self):
        pass


def main(args=None):
    rclpy.init(args=args)
    mw = MoveWhat()
    rclpy.spin(mw)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
