class Vehicle:
    def general_usage(self):
        print("general use: Transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheel = 4
        self.has_roof = True
    def specific_usage(self):
        print("specific use: Communicate to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motorcycle")
        self.wheel = 2
        self.has_roof = False
    def specific_usage(self):
        print("specific use: alone vacation")

c = Car()
m = MotorCycle()

print(isinstance(c,Car))

