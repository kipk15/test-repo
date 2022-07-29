# User Input and While Loops
# allows you to write fully interactive programs
prompt = "We collect information, but keep it confidential"
prompt += "\nPlease enter your first name: "

name = input(prompt)
print(f"\nHello {name.strip().title()}")

# using int() to accept numerical input
# input = int(input)

# The Modulo Operator (%)
# divides one number by another and returns the remainder
# e.g (4 % 3 = 1), (5 % 3 = 2), (6 % 3 = 0)
"""number = input ("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")"""

# Letting the User Choose when the program quits
# by putting the program inside a while loop
# you can use a flag- i.e a variable that determines whether
# or not the entire program is active
active = True
prompt = ("Enter a number "
    "and I'll tell you if it's even or odd. ")
prompt += "\nEnter 'quit' to end program: "
while active:
    number = input(prompt)
    if number == 'quit':
        active = False
    else:
        number = int(number)
        if number % 2 == 0:
            print(f"The number {number} is even")
        else:
            print(f"The number {number} is odd")

# break - breaks out of a loop entirely
# without executing the rest of its code
# continue statement - returns to the beginning of the loop
# based on the result of a conditional test
current_number = 0
while current_number < 10:
    current_number += 1
    # stop at number 
    if current_number == 9:
        break
    # print only odd numbers
    if current_number % 2 == 0:
        continue
    print(current_number)

# theater ticket charges
# depending on a person's age


seats = 0
# add a flag, as long as active
# python runs the while loop
active = True
while active:
    prompt = "How old are you: "
    age = int(input(prompt))
    # no toddlers and babies allowed in
    if (age <= 4):
        print("Sorry, too young for theater")
        continue
    elif (age < 13):
        price = 10
    elif (age < 20):
        price = 20
    elif (age < 65):
        price = 30
    elif (age >= 65):
        price = 15
    print(f"\nYour ticket price is {price}")
    seats = seats + 1

    # we only have 5 seats in the house
    # break out of loop when full
    if (seats == 2):
        print("The theater is now full!")
        break

# Moving items from one list to another
# Deli - loop thru list of sandwich orders
# print a message for each sandwich
# add it to finished
sandwich_orders = ['tuna', 'san1', 'san2', 'tuna', 'san3', 'sanH', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    # deli has no tuna
    if (current_sandwich == 'tuna'):
        print("Sorry, we are out of tuna")
        continue

    print(f"Making {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)

# display all finished sandwiches
print("\nThe following Sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()}")

# poll-taking
# Dream Vacation example
responses = {}

# add a flag
polling_active = True
while polling_active:
    prompt0 = "What is your name? "
    prompt1 = "If you could visit one place in the world, "
    prompt1 += "where would you go? "
    name = input(prompt0)
    response = input(prompt1)

    # store responses in a dictionary
    responses[name] = response

    # check if someone else would like to take poll
    prompt3 = "Would you like to let another person respond? (yes/no) "
    repeat = input(prompt3)

    if repeat == 'no':
        polling_active = False
    
    # Polling complete, show results
print("\n\t--Poll Results--\t")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}")


# using functions with a while loop
while True:
    print("Please tell me your name:")
    print("Enter 'q' at any time to quit")

    f_name = input("First name: ")
    if(f_name == 'q'):
        break
    l_name = input("Last name: ")
    if(l_name == 'q'):
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!\n")

    

    