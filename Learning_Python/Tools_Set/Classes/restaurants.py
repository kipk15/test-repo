# class Restaurant

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, customers_served):
        self.number_served += customers_served

class IceCreamStand(Restaurant):
    """initialize super attributes"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)# no self here
        """then sub"""
        self.flavors = ['cherry', 'merry', 'perry']# sub attributes

    def describe_flavors(self):
        print(f"\n{self.restaurant_name} ice-cream stand has these flavors: ")
        for item in self.flavors:
            print(f"\t{item}")

my_stand = IceCreamStand('my-stand', 'cream-ice')
my_stand.describe_flavors()