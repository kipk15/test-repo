# takes a pair of times from requests dictionary 
# and cancels one
# based on user
requests0 = {'date': 'a', 'schedule':[
    ['user1', ['1 pm - 2 pm', '2 pm - 3 pm', '3 pm - 4 pm', '12 pm - 1 pm']],
    ['user2', ['1 pm - 2 pm', '4 pm - 5 pm']],
    ['user3', ['12 pm - 1 pm', '2 pm - 3 pm']]]}
def invalidate_request(requests, user):
    base_request= []
    other_request= []
    for req in (requests['schedule']):
        if (req[0] == user):
            base_request.append (req[1])
        if (req[0] != user):
            other_request.append(req[1])
    print (f'base: {base_request}\n')
    print (f'other: {other_request}\n')

    i=0
    clashing_times = []
    for time1 in base_request[0]:
        for time2 in other_request[i]:
            if(time1==time2):
                print(time1)
                clashing_times.append(time1)
    print(f'\nlist of clashing times: {clashing_times}')

invalidate_request(requests0, 'user1')