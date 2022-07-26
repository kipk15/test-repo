# return values
# a function can process some data and then return 
# a value or set of values

# the return statement takes a values from inside a function 
# and sends it back to the line that called the function
def get_formatted_name(first_name, last_name, middle_name = ''):
    """ return a full name, neatly formatted """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
dj = get_formatted_name('Lasso', 'magoy')
print(f"\nDJ {dj} is performing tonight!")

# Making an argument optional
# to allow people using the function to provide
# extra information, only if they want to

# you can use default values to make arguments optional
# e.g adding middle name to function above,
# with a default value of ''
performer = get_formatted_name('Raphy', 'Jr.', 'Scons')
print(f"\nDJ {performer} is performing tonight!")
