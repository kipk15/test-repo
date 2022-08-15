import req

schedule = {
    '08/05/21': {
        'available': ['12pm', '1pm', '3pm' '7pm'],
        'accepted': [],
        'pending': [],
    },
        '02/05/23': {
        'available': ['11am', '1pm', '2pm', '3pm', '5pm'],
        'accepted': [],
        'pending': []
    }
    
}
user1 = req.Request.User('Joe', 'Roe', 'jR@email.com', '315 328 9034')
user2 = req.Request.User('seth', 'tue', 'St@email.com', '315 678 9034')
user3 = req.Request.User('hui', 'hutf', 'hH@email.com', '315 328 6774')
user1.create_request('08/05/21', ['1pm', '3pm'])
user2.create_request('02/05/23', ['12pm', '3pm', '7pm'])
user3.create_request('03/01/05', ['5pm-6pm', '6pm-7pm'])
requests = req.Request.all_user_requests
# move one users request to accepted
def accept_request(request):
   # print(schedule)
    for key2, value2 in request.items():
        try:
            pk =(value2[1] in schedule.keys())
        except HandleableErrors:
            pk = False
        finally:
            if pk:
                schedule[value2[1]]['accepted'].extend([value2[0], value2[2]])
                print(f"\n{key2} accepted")
            else:
                print(f"\nwe do not have a schedule for {value2[1]}"
                        f"\n\t{key2}  not accepted")

    print(schedule)
def decline_request(request):
    pass

def update_request(accept_request, decline_request):
    pass

accept_request({'request_0': ['jR@email.com', '08/05/21', ['1pm', '3pm']]})
#accept_request({'request_2': ['hH@email.com', '03/01/05', ['5pm', '7pm']]})
accept_request({'request_1': ['St@email.com', '02/05/23', ['12pm', '3pm', '7pm']]})
accept_request({'request_4': ['St@email.com', '08/07/23', ['s3pm', '7pm']]})