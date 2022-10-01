from car import Car

class Truck(Car):
    def __init__(self, model, year, volume, price, mileage):
        super().__init__(model, year, volume, price, mileage)
        self.wheels = 8
        self.type = "Truck"

    def display(self):
        return (Car.display(self))
