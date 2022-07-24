#if statement
age=64
if age<4:
    #print("Your admission cost is $0")
    price=0
elif age<18:
    #print("Your admission cost is $25")
    price=25
elif age<40:
    #print("Your admission cost is $25")
    price=50
elif age<70:
    #print("Your admission cost is $25")
    price=100
else: 
    #print("Your admission cost is $40")
    price=30
print(f"Your admission cost is ${price}")

#python doesn't require an else block at the end
#of an if-elif chain, In fact
#there are times when it's clearer to use 
#an additional elif instead of an else e.g elif age>=70

alien_color = "yellow"

if (alien_color=="green"):
    #print("You just earned 5points")
    points=5
#if (alien_color!="green"):
elif (alien_color=="yellow"):
    #print("You just earned 10points")
    points=10
elif(alien_color=="red"):
    #print("You just earned 15points")
    points=15
print(f"You just earned {points}points")

age=37

if (age<2):
    stage="a baby"
elif (age<4):
    stage="a toddler"
elif (age<13):
    stage="a kid"
if (age<20):
    stage="a teenager"
elif (age<65):
    stage="an adult"
if (age>=65):
    stage="an elder"
print(f"You are {stage}")