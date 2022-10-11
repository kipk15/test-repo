#print("hello Ricky")

kainet = input("Kigurenin ngo: ")
print(f"Iyomune o {kainet}")

answer1 = input(f"{kainet} Koiomishe i(ile ei anan acha): ")
while answer1 != 'ei' and answer1 != 'acha':
    answer1 = input(f"{kainet} Pagach story mingi, ei ana acha o: ")

if answer1 == 'ei':
    print('Ooo, kongoi any')

elif answer1 == 'acha':
    print('pole any')


    

