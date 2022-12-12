from models import *

def print_functionality(*funs):
    print('Функциональность:', 
          ', '.join([fun for fun in funs]).capitalize(),
          end='.\n')

if __name__ == "__main__":
    print('Робот после создания')
    print('---------------------')
    robot = RobotV()
    print(robot)
    print()

    print('Робот после первичного обучения')
    print('---------------------')
    robot = RobotVita(robot=robot)
    print(robot)
    print_functionality(
        robot.build_home(), 
        robot.build_barn(),
    )
    print()

    print('Робот после практики')
    print('---------------------')
    robot = RobotVitaliy(robot=robot)
    print(robot)
    print_functionality(
        robot.build_home(), 
        robot.build_barn(),
        robot.add_floor(),
        robot.remove_floor(),
    )