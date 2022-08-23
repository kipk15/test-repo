import requests


sch = requests.schedule
def accept_request(date, user_email):
    to_accept=[]
    for key, value in sch.items():
        if date == key:
            pending_list = value['pending']
            for item in pending_list:
                if user_email == item[0]:
                    #print(f"accepting {item[0]}'s {item[1]}") 
                    to_accept.append(item)  

     
    for a in to_accept:
        #print(a) - 
        # for each accepted time, remove it from available
        if a[1] in sch[date]['available']:
            sch[date]['available'].remove(a[1])
            
        # for each accepted time, remove it from pending
        to_remove=[]
        crash_remove=[]
        for item in sch[date]['pending']:
            if a[1] == item[1]:
                to_remove.append(item)
       
        for b in to_remove:
            # removing times accepted from pending
            if b[0] == user_email:
                sch[date]['pending'].remove(b)
            
            # removing request affected by the 'accept' action, i.e clashing times
            if b[0] != user_email:
                print(f"\n{b[0]} request for {date} out the window, inform them so")
                for item in sch[date]['pending']:
                    if b[0] == item[0]:
                        crash_remove.append(item)
        for c in crash_remove:

            sch[date]['pending'].remove(c)
            
            
                                
    sch[date]['accepted'].extend(to_accept)
                

user1 = requests.Request.User('Joe', 'Roe', 'jR@email.com', '315 328 9034')
user2 = requests.Request.User('seth', 'tue', 'St@email.com', '315 678 9034')
user3 = requests.Request.User('hui', 'hutf', 'hH@email.com', '315 328 6774')
user1.create_request('08/05/21', ['1pm', '2pm', '7pm'])
user2.create_request('08/05/21', ['2pm', '4pm'])

print(f'\n\tSchedule: \n {sch}') 

accept_request('08/05/21','jR@email.com')

user3.create_request('08/04/21', ['1pm', '4pm'])
user3.create_request('08/06/21', ['1pm', '4pm'])


print(f'\n\t Updated Schedule: \n{sch}')



