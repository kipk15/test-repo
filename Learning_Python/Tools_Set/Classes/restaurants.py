# class Restaurant

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, increase):
        self.number_served += increase
