# takes a pair of times from requests dictionary 
# and cancels one
# based on user
requests01 = {'date': 'a', 'schedule':[
    ['user1', ['1 pm - 2 pm', '2 pm - 3 pm', '3 pm - 4 pm', '12 pm - 1 pm']],
    ['user2', ['1 pm - 2 pm', '4 pm - 5 pm']],
    ['user3', ['12 pm - 1 pm', '2 pm - 3 pm']]]}
    
def invalidate_request(requests, user):
    base_request= []
    other_request= []
    req=requests['schedule']
    i=0

    #loop through req and find user of interest
    while (i < len(req)):
        if (req[i][0] != user ):
            for time in (req[i][1]):
                other_request.append(time)
        else:
            for time in (req[i][1]):
                base_request.append(time)
        i=i+1

    print(f'\n base: {base_request}')
    print(other_request)

    for time0 in base_request:
        for time1 in other_request:
            if(time0 != time1):
                print('y')
            else:
                print(f'\n {time1} clashes')


    """ while (i<len(req)):
        if (req[0] == user):
            for time in (req[1]):
                base_request.append (time)
                
        else:
            for time in (req[1]):
                other_request.append(req[1])
        i=i+1
        
    print (f'base: {base_request}\n')
    print (f'other: {other_request}\n')

    i=0
    clashing_times = []
    for time1 in base_request[0]    :
        for time2 in other_request[i][0]:
            if(time1==time2):
                print(time1)
                clashing_times.append(time1)
                i=i+1
    print(f'\nlist of clashing times: {clashing_times}')
 """
invalidate_request(requests01, 'user1')