
class Vehicle:
    def __init__(self, color=None, wheels=4):
        self.color = color
        self.wheels = wheels

    def start(self):
        print(f"Starting a {self.color} vehicle...")

    def stop(self):
        print("Stopping the vehicle.")

class Car(Vehicle):
    def __init__(self, color=None, wheels=4, num_doors=4):
        super().__init__(color, wheels)
        self.num_doors = num_doors

my_car = Car("red")
print(my_car.color)  # Output: red
print(my_car.wheels)  # Output: 4
print(my_car.num_doors)  # Output: 4

my_car.start()  # Output: Starting a red vehicle...
my_car.stop()   # Output: Stopping the vehicle.
