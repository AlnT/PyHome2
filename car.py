class Car():
    def __init__(self, model, year, volume, price, mileage):
        self.model = model
        self.year = year
        self.volume = volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4
        self.type = "Car"
    def display(self):
        return(self.type + " model: " + str(self.model) + "\nYear of manufacture: " + str(self.year) + "\nEngine capacity: " + str(self.volume) + "\nPrice: " + str(self.price) + " $"
              + "\nMileage: " + str(self.mileage) + " mi" + "\nNumber of wheels: " + str(self.wheels))
