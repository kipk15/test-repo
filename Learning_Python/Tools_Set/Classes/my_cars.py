from car import Car
import electric_car

my_used_car = Car('subaru', 'outback', 2015)
print(f"\n{my_used_car.get_descriptive_name()}")

my_used_car.update_odometer(23_400)
my_used_car.read_odometer()

my_used_car.increment_odometer(300)
my_used_car.read_odometer()

my_ebike = electric_car.ElectricCar('Beast-made', 'model fz1', 2023)
print(my_ebike.get_descriptive_name())
my_ebike.battery.describe_battery()
my_ebike.battery.upgrade_battery()
my_ebike.battery.describe_battery()
my_ebike.battery.get_range()