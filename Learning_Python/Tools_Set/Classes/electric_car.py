# inheriting from parent class car
#from car import Car 
""" above: importing specific class
    below: importing entire module- and using dot notation 
    to specify classes"""
import car

class Battery():
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):# 75 is default
        """initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This vehicle has a {self.battery_size}kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(car.Car):# since we imported entire module
    """represent aspects of a car, specific to 
    electric vehicles"""
    def __init__(self, make, model, year):
        """initialize attributes of the parent class.
        Then initialize attributes specific to child class"""
        super().__init__(make, model, year)
        self.battery = Battery()
               
"""my_ebike = ElectricCar('Beast-made', 'model fz1', 2023)
print(my_ebike.get_descriptive_name())
#my_ebike.battery_size = 100
my_ebike.battery.describe_battery()
my_ebike.battery.upgrade_battery()
my_ebike.battery.describe_battery()
my_ebike.battery.get_range()"""
