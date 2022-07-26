# Functions are named blocks of code 
# designed to do one specific job
# Allows you to perform a task many times
# without having to rewrite the code 
def greet_function(username): # variable username is a parameter
    print(f"\nHello {username.title()}")
greet_function("bWoGy") # bWoGy here is an argument

# Passing Arguments

# 1. Positional Arguments: arguments need to be
# in the same order the parameters were written
def describe_pet(username, pet_name, animal_type='dog', ):
    print(f"\n{username.title()} has a {animal_type}.")
    print(f"{username.title()}'s {animal_type}'s name is {pet_name.title()}")
describe_pet("Kilo", "tedMos", "giraffe")
describe_pet("KanSS", "CarrOTY", "parrot")
describe_pet("SWsus",  "tedMos", "giraffe")

# 2. Keyword Arguments: is a name-value pair
# that you pass to a function, by directly associating
# name and the value within the argument
# clarifies the role of each value in the function call, so
# order of arguments doesnt matter

# using keyword arguments for fuction above:
describe_pet(animal_type="larvae", username="Drum", pet_name="smOL")
describe_pet(pet_name="SmUGGG", animal_type="Crocodile", username="BaaDDy")

# default values
# allows you to define default values for parameters
# and if an argument for a parameter is provided 
# in the fuction call, python uses the argument value

# any parameters with default values need to be listed
# after all the parameters without default values
# this allows python to continue interpretting 
# positional arguments correctly

# in describe_pet() function, set animal_type to 'dog'
# call the function without providing an argument for animal_type
describe_pet(pet_name="SmUGGG", username="BaaDDy")
describe_pet(pet_name="Flan", username="Jos")

# Avoid Argument Errors
# e.g unmatched arguments, i.e you provide fewer or more
# arguments than a function needs to do its work 


