# a simple class that represents a dog in general
# and which we can use to create individual instances
# to represent specific dogs

# each instance created from the Dog class 
# will store a name and an age
# and we'll give each dog the ability to
# sit() and roll_over()
class Dog:
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Tusker', 8)
your_dog = Dog('Lame', 72)
# dot notation to access attributes and to call methods
print(f"My dog, {my_dog.name}, is {my_dog.age} years old."
    f"\nBut, your {your_dog.name} dog is {your_dog.age} years older")

my_dog.roll_over()
my_dog.sit()

