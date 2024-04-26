class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = "blue"
        self.speed = 0
    
    def accelerate(self):
        self.speed += 1
    
    def brake(self):
        self.speed -= 1
    
    def get_status(self):
        return f"The car is {self.color} and has a speed of {self.speed}"

# create an instance of the Car class
car = Car("Toyota", "Camry", 2020)

# call the accelerate method on the car object
car.accelerate()
print(car.get_status()) # prints "The car is blue and has a speed of 1"

# call the brake method on the car object
car.brake()
print(car.get_status()) # prints "The car is blue and has a speed of 0"

# set the color property to "red"
car.color = "red"
print(car.get_status()) # prints "The car is red and has a speed of 0"

# create another instance of the Car class
another_car = Car("Honda", "Civic", 2015)

# call the accelerate method on the another_car object
another_car.accelerate()
print(another_car.get_status()) # prints "The car is blue and has a speed of 1"