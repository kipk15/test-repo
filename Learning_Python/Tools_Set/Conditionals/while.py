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
    if (seats == 5):
        print("The theater is now full!")
        break
    


    

    