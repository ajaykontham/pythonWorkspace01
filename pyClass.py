
class vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self,speed):
        self.speed = speed

class car(vehicle):
    def __init__(self,engineType):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engineType = engineType

    def drive(self,speed):
        super().drive(speed)
        print("Driving", self.engineType, "car at", self.speed)

class moterbike(vehicle):
    def __init__(self, engineType, hasSideCar):
        super().__init__("Moterbike")
        self.engineType = engineType
        if(hasSideCar):
            self.wheels = 3
        else:
            self.wheels = 2

    def drive(self,speed):
        super().drive(speed)
        print("Driving", self.engineType, "motorbike at", self.speed)

car1 = car("Gas")
car2 = car("Electric")
mb1 = moterbike("Gas",True)
mb2 = moterbike("Gas", False)

print(car1.doors)
print(car2.engineType)
print(mb1.wheels)
print(mb2.wheels)

car1.drive(50)
car2.drive(80)
mb1.drive(45)