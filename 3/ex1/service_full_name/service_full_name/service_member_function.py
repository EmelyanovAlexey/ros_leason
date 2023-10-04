from example_interfaces.srv import AddTwoInts
from full_name_interface.srv import FullNameService
import rclpy
from rclpy.node import Node
class MinimalService(Node):

    def __init__(self):
        # Конструктор MinimalServiceкласса инициализирует узел именем minimal_service. Затем он создает 
        # службу и определяет тип, имя и обратный вызов.
        super().__init__('minimal_service')
        self.srv = self.create_service(FullNameService, 'full_name', self.full_name_callback)

    # Определение обратного вызова службы получает данные запроса, суммирует 
    # их и возвращает сумму в качестве ответа.
    def full_name_callback(self, request, response):
        response.full_name = request.last_name + ' ' + request.name + ' ' + request.first_name
        self.get_logger().info('Incoming request\nlast name: %s name: %s  first name: %s' % (request.last_name, request.name, request.first_name))

        return response

def main():
    rclpy.init()
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# 1:
# colcon build --packages-select service_full_name
# colcon build
# source install/setup.bash
# ros2 run service_full_name service_name

# 2:
# source install/setup.bash
# ros2 run service_full_name client_name Emelyanov Alex Alexeevich