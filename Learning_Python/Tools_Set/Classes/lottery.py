from random import randint


# randomly pick an index, and display value at that index
pocket = [34, 14, 'w', 8, 1, 6, 'y', 33, 0, 3, 'd', 4, 'e', 7,'f']
my_ticket = 34
#print("These are the lucky tickets: \n")
i = randint(0, (len(pocket)-1))
count = 0
while my_ticket != pocket[i]:
    count += 1
    i = randint(0, (len(pocket)-1))
print(f"Your ticket number, {my_ticket}, emerged a winner after {count} rolls")

