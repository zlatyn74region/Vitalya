from abc import ABC

class Robot(ABC):
    inv_num: str = "АА001221-56"
    name: str
    place: str

    def __str__(self) -> str:
        return f'Инвентарный номер: {self.inv_num}\n' + \
                f'Наименование: {self.name}\n' + \
                f'Местонахождение: {self.place}'

class RobotV(Robot):
    def __init__(self):
        self.name = "В"
        self.place = "Робозавод"

class Decorator(Robot, ABC):
    robot: Robot

    def __init__(self, robot: Robot):
        self.robot = robot

    def build_home(self) -> str:
        return self.robot.build_home()

    def build_barn(self) -> str:
        return self.robot.build_barn()

    def add_floor(self) -> str:
        return self.robot.add_floor()

    def remove_floor(self) -> str:
        return self.robot.remove_floor()

class RobotVita(Decorator):
    def __init__(self, robot: Robot):
        super().__init__(robot=robot)
        self.name = 'Вита' 
        self.place = 'Первичное обучение'   

    def build_home(self) -> str:
        return 'Постройка домов'

    def build_barn(self) -> str:
        return 'Постройка сараев'

class RobotVitaliy(Decorator):
    def __init__(self, robot: Robot):
        super().__init__(robot=robot)
        self.name = 'Виталий' 
        self.place = 'Предприятие "ООО Кошмарик"'

    def add_floor(self) -> str:
        return 'Добавление этажей к постройкам'

    def remove_floor(self) -> str:
        return 'Снос верних этажей у построек'