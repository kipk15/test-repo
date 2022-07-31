# inheriting from parent class car
class Car:
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """set odometer reading to the given value"""
        self.odometer_reading = mileage
    
    def increment_odometer(self, miles):
        """add given amount to the odometer reading"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """represent aspects of a car, specific to 
    electric vehicles"""
    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)

my_ebike = ElectricCar('Beast-made', 'model fz1', 2023)
print(my_ebike.get_descriptive_name())