#if statement
age = 64
if age < 4:
    #print("Your admission cost is $0")
    price = 0
elif age < 18:
    #print("Your admission cost is $25")
    price = 25
elif age < 40:
    #print("Your admission cost is $25")
    price = 50
elif age < 70:
    #print("Your admission cost is $25")
    price = 100
else: 
    #print("Your admission cost is $40")
    price = 30
#print(f"Your admission cost is ${price}")

#python doesn"t require an else block at the end
#of an if-elif chain, In fact
#there are times when it"s clearer to use 
#an additional elif instead of an else e.g elif age>=70

alien_color = "yellow"

if (alien_color == "green"):
    #print("You just earned 5points")
    points = 5
#if (alien_color!="green"):
elif (alien_color == "yellow"):
    #print("You just earned 10points")
    points = 10
elif(alien_color == "red"):
    #print("You just earned 15points")
    points = 15
#print(f"You just earned {points}points")

age = 37

if (age <2 ):
    stage = "a baby"
elif (age < 4):
    stage = "a toddler"
elif (age < 13):
    stage = "a kid"
if (age < 20):
    stage = "a teenager"
elif (age < 65):
    stage = "an adult"
if (age >= 65):
    stage = "an elder"
#print(f"You are {stage}")

#check if list is not empty
#pizzeria
requested_toppings = ["tomatoes","spinach","cheese"]
requested_toppings0 = []
def notify_Customer(request):
    if request:
        print("Your request has been received")
        for item in request:
            print(f"Adding {item}")
    else:
        print("Are you sure you want plain fried dough?")
#notify_Customer(requested_toppings)
#notify_Customer(requested_toppings0)

#looping through items in a list
#do not trust user's capitalization

#users=[" mArk ", " teRRy", "Meg", "ADMIN ", " MAc"]
users = []
if users:
    for name in users:
        user = name.lower().strip()
        if (user == "admin"):
            tag="would you like to check status report"
        else:
            tag = "thank you for loggin in again"
        print(f"\n Hello {user.title()}, {tag}")
else:
    print("We need to find some users!")

current_users = [" mArk ", " teRRy", "Meg", "ADMIN ", " MAc", "viN"]
new_users = [" Mary ", " Eagle", "maC", "Alpho ", " adMiN"]
def compare_elements(list1, list2):
    users0=[]
    for user in current_users:
        username = user.strip().lower()
        users0.append(username)
    for name in new_users:
        item = name.lower().strip()
        if item in users0:
            print(f"\n {item.title()} is taken, choose a different username")
        elif item not in users0:
            print(f"\n {item.title()} is available, proceed?")
#compare_elements(new_users, current_users)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def ordinal_numbers(number_list):
    if digits:
        for item in digits:
            if item in range(4, 10):
                tag = "th"
            elif item == 3:
                tag = "rd"
            elif item == 2:
                tag = "nd"
            elif item == 1:
                tag = "st"
            print(f"\t{item}{tag} ")
#ordinal_numbers(digits)

