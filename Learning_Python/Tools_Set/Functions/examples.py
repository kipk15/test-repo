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

# Making an argument optional
# to allow people using the function to provide
# extra information, only if they want to

# you can use default values to make arguments optional
# e.g adding middle name to function above,
# with a default value of ''
"""
performer = get_formatted_name('Raphy', 'Jr.', 'Scons')
print(f"\nDJ {performer} is performing tonight!")
"""

# Returning a Dictionary
def build_person(first_name, last_name, occupation=None):
    """ return a dictionary of information abt a person. """
    if occupation:
        person = {'first': first_name, 'last': last_name, 'Job title': occupation}
    else:
        person = {'first': first_name, 'last': last_name}
    return person

"""
dancer = build_person('didDidi', 'the_dancer')
print (dancer)"""

# you can easily extend this function to accept 
# optional values e.g middle name, age, occupation etc
# you just have to change the function accordingly

# add occupation to function above
"""
surveyor = build_person('Lansh', 'the_lot', 'surveyor')
print (surveyor)
"""

# make_album() function
# takes in an artist name and album title
# and returns a dictionary with these info
def make_album(artist_name, album_title, songs=None):
    if songs:
        album = {'Artist': artist_name.title(), 
    'Album_title': album_title.title(), 'Songs': songs}
    else:
        album = {'Artist': artist_name.title(), 'Album_title': album_title.title()}
    return album
album0 = make_album('JImJam', 'tomORROw')
album1 = make_album('Wash', 'tOODAY', 12)
album2 = make_album('Denzel', 'EVVeryday', 4)
print("\n",album0,"\n", album1,"\n", album2)

# prevemting a function from modifying a list
# we send a copy of the list to the function 
# as arguments
"""function_name(list_name[:])"""
def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print(f"\n sending {current_message.title()} now")
        sent_messages.append(current_message)
    return(sent_messages)
messages0 = ['hey', 'where', 'are', 'you']
sent_messages0 = send_messages(messages0[:])
print(sent_messages0)
print (messages0)

# Passing Arbitrary number of arguments
# to allow a parameter to collect as many arguments
# as the calling line provides
def make_pizza(size, *toppings):
    """summarize pizza being made"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# note that the asterisk in the parameter name *toppings
# tells python to make an empty tuple called toppings
# and pack whatever values it receives into this tuple
make_pizza(18, 'pepperoni')
make_pizza(12, 'mushrooms', 'pepper', 'onions', 'cheesy')

# Mixing positional and arbitrary arguments(*args)
# lets add size to function above


