# working with classes and instances
# since you'll spend most of your time working
# with instances created from a class, it's best
# to modify the attributes associated with a particular 
# instance earlier on, either directly or via methods

# the Car class
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
    
my_new_whip = Car('audi', 'a4', 2019)
print(my_new_whip.get_descriptive_name())
my_new_whip.odometer_reading = 45
my_new_whip.read_odometer()

# to add attributes that change over time
# we set a default value for an attribute
"""add odometer_reading to function above"""

