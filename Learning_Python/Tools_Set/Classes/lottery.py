from random import randint

# randomly pick an index, and display value at that index
pocket = [34, 14, 'w', 8, 1, 6, 'y', 33, 0, 3, 'd', 4, 'e', 7,'f']
m = 0
print("These are the lucky tickets: \n")
while m < 4:
    i = randint(0, (len(pocket)-1))
    print (i)
    print(f"\t{pocket[i]}")
    m +=1
