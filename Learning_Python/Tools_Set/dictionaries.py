# A dictionary is a collection of key-value pairs, wrapped in {}
# allows you to model a variety of real-world objects more accurately
# allows you to connect pieces of related info
# can be nested, e.g dictionaries inside lists
# lists inside dictionaries and even dictionaries inside dictionaries

alien_0 = {'color': 'yellow', 'trait': 'grumpy'}
# they're dynamic, i.e you can add new key-value pairs
# to a dictionary at any time 
#print (alien_0)
alien_0['level'] = 27
alien_0['name'] = 'mrGrums'
#print(alien_0)

# sometimes it's necessary to start with an empty dictionary
# and then add each new item to it
alien_1 = {}
alien_1['name'] = 'mrSkim'
alien_1['color'] = 'purple'
alien_1['trait'] = 'tentative'
alien_1['speed'] = 'fast'
alien_1['points'] = 15
#print(alien_1)

# changing key-value pairs
alien_1['speed'] = 'slow'
del alien_1['points']
#print(alien_1)

# A dictionary of similar objects
fav_languages = {
    'GrAce ': 'EngLish ',
    ' vic': ' numbers',
    ' aLloy ': 'c++ ',
    }
fav_languages['JeAN '] = 'python '
fav_languages[' PetE'] = ' English'

# accessing values
#language = fav_languages['Jean'].title()
#print(f"Jeans favorite language is {language}")

# using get() method to access values
# allows you to set a default return value
# if requested key doesn't exist
#lang = fav_languages.get("Pete", 'No such key in file')
#print(f"\n Pete: {lang}")
#lang2 = fav_languages.get("Szn", 'No such key in file')
#print(f"\n Szn: {lang2}")

# loop through dictionary 
# 1. loop through all key-value pairs
for key, value in fav_languages.items():
    name = key.lower().strip()
    language = value.lower().strip()
    #print(f"\n {name.title()}'s favorite language is {language.title()}")

# 2. looping through all the keys
friends = ["grace", "alloy", "star", "struck"]
# sorted() fuction adds order
for key in sorted(fav_languages.keys()):
    name = key.lower().strip()
    language = fav_languages[key].title()
    if name in friends:
        print(f"\tHey {name.title()}, I see you like {language}!")
    else:
        print (f"\tHey {name.title()}, would you like to be friends?")

# looping through all values in a dictionary
# set - collection of unique items
# has no ordering
# for value in set(dictionary.values()):
   # print(value.title())

#nesting dictionaries in lists
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# modifying group if dictionaries
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print(f"\n Total number of aliens created: {len(aliens)}")

# Nesting

# 1. A list in a Dictionary
# store info about a pizza order
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'spinach']
    }
# summarize the order
print(f"You order is a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for toppings in pizza['toppings']:
    print("\t" + toppings)

# 2. a Dictionary in a Dictionary
users = {
    'Al': {
        'age': 23,
        'role': 'squid',
        'teeth': '23molars'
    },
    'Ed': {
        'age': 32,
        'role': 'scorpio',
        'teeth': '16incissors'
    }
}
# loop through the users dictionary
# and access its keys and values
# keys being the username
# values being the dictionaries with bio info
for username, bio in users.items():
    print(f"\n{username} is {bio['age']}, a {bio['role']} "
        f"with {bio['teeth']}")



