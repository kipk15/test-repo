motorcycles = ['honda', 'civic', '2013']
motorcycles.append('yamaha')
motorcycles.append('V12')
motorcycles.append('tes la')
##print (motorcycles)
motorcycles_LiFo = motorcycles.pop()
#message=f"\nMy last in first out bike is {motorcycles_LiFo.title()}!"
##print(message)
##print(motorcycles)
motorcycles.append('rev1')
motorcycles.append('rev2')
motorcycles.append('rev2')
motorcycles.append('rev4')
motorcycles.append('rev5')
motorcycles.insert(int(len(motorcycles)/2), 'inserted_rev')
##print (motorcycles)
""" pop() method
    #can either take an index
    #or pop the last item in stack i.e [-1]
 """
motorcyles_rem_second = motorcycles.pop(1)
##print(f"\nI just removed {motorcyles_rem_second.title()}- it had index 1")
#i=0
#while(i<len(motorcycles)):
#    #print(f"bike no{i}: {motorcycles[i]}")
#    i=i+1

#print(motorcycles)
#motorcycles.reverse()
#print(motorcycles)

""" Create List--assign """
Guests = ['a', 'b', 'c']
#for i in range(0, len(Guests)):
#    print(f'\nbaby {Guests[i]}, welcome to the party!')
#print(f'dang, baby {Guests[1]}, didn't show!')
""" replace elements at a given index--reassign """
Guests[1]='d'
#for i in range(0, len(Guests)):
#   print(f'\{Guests[i]}, welcome to the list!')
#for g in Guests:
#    print(f'\n {g}, bigger table!')

""" insert( index, 'ItemName' ) method"""
Guests.insert(0, 'insert_guest@i0')
Guests.insert(int(len(Guests)/2), 'insert_mid_guest')

""" append('ItemName') method- adds item to end of list"""
Guests.append('appended_guest')

""" while loop
    #Guests list is too long
    #cut everyone but two
""" 

i=(len(Guests))
while(i > 2):
    "pop() method"
    #popped_guest = Guests.pop()
    #print(f'\nsorry {popped_guest}, we have to cut down the list')
    i=i-1
#print(Guests)

""" try reverse, i.e del starting w 1st element """
i=(len(Guests))
while (i > 2):
        popped_guest = Guests.pop(0)
        #print(f'\nsorry {popped_guest}, we have to cut down the list')
        i=i-1
for guest in Guests:
        i=0
        #print(f'\nyou , {guest}, are lucky! you retained your spot!')
#print(Guests)
"remove() method"
"del statement- when you dont need to work with the item"
i=0
while(i<len(Guests)):
    #print (Guests)
    #del Guests[i]
    Guests.remove(Guests[i])
    #print (Guests)

"organizing a list"

"sort() method- permanently order elements alphabetically"
names = ['bur1', 'lUs', 'suyhd', 'auhd']
names.sort()
#print (names)
names.sort(reverse=True)#sorts from z to a
"sorted() fuction- order temporarily"
message=(f'original order: {names}\n sorted order: {sorted(names)}\n original: {(names)}')
#print(message)
"reverse method"
names.reverse()
#print(names)
"len() function"
#print(f'{len(names)} items in names_list')

pizzas = [] #['pep','egg', 'tea']
for pizza in pizzas:
    if(pizza=='pep'):
        print(f'I like {pizza} on a pizza')
    elif((pizza=='egg')):
        print(f'{pizza} pizza is classic')
    else:
        print(f'{pizza} pizza, what is that?!')
#print('who dont like good dough though')

#methods vs fuctions 
#method- an action that python can perform on a piece of data
#Every method is followed by a set of parantheses
#bcz they need additional info to perform their task

input_name=(" SAm liM ")
#rstrip method
#looks for extra whitespace on the right of a string
#lstrip- on the left
#strip- both sides at once
'name=input_name.lower().rstrip().lstrip()'
name=input_name.lower().strip()

if (name == "sam lim "):
    print(f'\n\tThey call him{name.title()},\n\t"the man behind sponge-gate.."')

#numbers
# ** represents exponents
# python supports order of operations
# BODMAS?
rays = 2 + 3*4
rays1 = (2 + 3)*4
print (f'{rays}!={rays1}')

#Floats
#any number with a decimal
#dividing two numbers gives a float
#mixing an integer and a float = float
#underscores are used to make large numbers more readable
#i.e 1000==1_000==10_00
#python allows multiple assignments
i=10000
if (i==10_000):
    x,y,z = 0,1,2
#print(x,y,z)

#A constant stays the same throughout the life of a program
#python porgrammers uses all caps to indicate constants
#print('fav_number')#using BODMAS
#print(f"write \n\t{x}: meaningful descriptive comments\n\t{y}: well-designed, efficient & elegant code \n\t{z}: simple's better than complex, complex better than complicated,\nEssentially, Readability Counts!")
#print(f"This is called the philosopy of simplicity and clarity")

#range f    


#slicing a list
#list[start_i:end_i]
#as with range, python stops at (end_i -1)
numbers = [1, 2, 3, 0, 8, 4, 9]
#print(numbers[3:5])

#tuple
#an immutable list
#i.e cannot change
foods = ('pie', 'soy', 'lime', 'green', 'pepper')
i=0
while(i<len(foods)):
    print(foods[i])
    i=i+1
#this doesnt work   
#for item in foods:
    #item='hus'
foods=('a','b','v','m')
print(foods)

