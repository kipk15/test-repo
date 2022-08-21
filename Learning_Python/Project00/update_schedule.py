import requests

schedule = {
    '08/05/21': {
        'available': ['12pm', '1pm', '3pm', '7pm'],
        'accepted': [],
        'pending': [],
    },
        '02/05/23': {
        'available': ['11am', '1pm', '2pm', '3pm', '5pm'],
        'accepted': [],
        'pending': []
    }
    
}


#schedule_dict['available'] = available timeslots list
#
#req = requests.Request.all_user_requests
# = date
#req.values() = request_list
#request_list[1] = user.email
#request[2] = requested timeslots list
#
user1 = requests.Request.User('Joe', 'Roe', 'jR@email.com', '315 328 9034')
user2 = requests.Request.User('seth', 'tue', 'St@email.com', '315 678 9034')
user3 = requests.Request.User('hui', 'hutf', 'hH@email.com', '315 328 6774')
user1.create_request('08/05/21', ['1pm', '3pm'])
user2.create_request('02/05/23', ['12pm', '3pm', '7pm'])
user3.create_request('03/01/05', ['5pm-6pm', '6pm-7pm'])
req = requests.Request.all_user_requests
# move one users request to accepted
def accept_request(req):
    for request_date in req.keys():
        try:
            cond1 =(request_date in schedule.keys())
            
        except HandleableErrors:
            cond1 = False
        finally:
            if cond1:
                for request_list in req.values():
                    r_timeslots = request_list[1]
                    requestor = request_list[0]
                    print(f"\n{requestor} has made a request for {request_date} "
                        f"\n\trequested timeslots: {r_timeslots}")

                    for schedule_dict in schedule.values():
                        available_timeslots = schedule_dict['available']

                    for r_time in r_timeslots:
                        cond2 = (r_time in available_timeslots)
                        try:
                            cond2 = True
                            
                        except HandleableErrors:
                            cond2 = False 
                        
                        finally:
                            if not cond2:
                                for r_time in r_timeslots:
                                    print(f"Sorry, your request, {r_timeslots},"
                                        f"has times not available on {request_date}")
                                        
                            else:
                                print(f"Hoorah, requested time, {r_time}, "
                                    f"on {request_date} is available!")
                                pending_requests = schedule_dict['pending']
                                accepted_requests = schedule_dict['accepted']

                                accepted_requests.append(r_time)
                                #schedule_dict['available'].remove(r_time)
                print(f"verified: {accepted_requests}")
            else:
                for request_list in req.values():
                    requestor = request_list[0]
                    print(f"\nSorry {requestor}, we do not currently have"
                        f" a schedule for {request_date}")
    
    #print(schedule)
def decline_request(request):
    pass

def update_request(accept_request, decline_request):
    pass

accept_request({'08/05/21': ['jR@email.com',['1pm', '3pm']]})
#accept_request({'03/01/05': ['hH@email.com',['5pm', '7pm']]})
accept_request({'02/05/23': ['St@email.com',['12pm', '3pm', '7pm']]})
#accept_request({'08/07/23': ['St@email.com',['s3pm', '7pm']]})



# takes req n check 

sch = {'08/05/21': {'av_timeslots': ['12pm', '2pm', '3pm','7pm'],
                    'pend_reqs':[],
                    'acc_reqs':[]}}
req = {'08/05/21':{'timeslots': ['2pm', '1pm', '3pm'],
                    'contact': 'ef@mail.com',
                    'name': 'max ter'} }
def accept_req(sch, req):
    # check if req_date matches sch date
    for a in req.keys():
            req_date = a
            print(req_date)
    
    try:
        
        condition1 = (req_date in sch.keys())

    except HandleableErrors:
        condition1 = False

    finally:
        if condition1:
            print("we found a matching date."
                    f"\n\ttimeslots available on {req_date}:"
                    f"{sch[req_date]['av_timeslots']}")

            print(f"\n\tyour request--> {req} ")
            
            
            for time1 in req[req_date]['timeslots']:
                if time1 in sch[req_date]['av_timeslots']:
                    print(time1)
                    sch[req_date]['av_timeslots'].remove(time1)
              
                    sch[req_date]['acc_reqs'].append(f"{time1}")

                else:
                    print(f"sorry {req[req_date]['name'].title()}, your requested timeslot {time1} is not available")
            #print(f"availabe_after: {sch[req_date]['av_timeslots']}")
            print(f"accepted request: {[req[req_date]['name'].title(), req[req_date]['contact'], sch[req_date]['acc_reqs']]}")
            
            print(f"\t\n\tUpdated Schedule:\n{sch}")


accept_req(sch, req)









