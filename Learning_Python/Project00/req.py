class Requests():
    new_requests = {}
    times_accepted = []
    times_4review = []
    requests_made = 0

    def __init__(self, user, date, timeslots=[], status='pending'):
        self.user = user
        self.date = date
        self.timeslots = timeslots
        self.status = status

        Requests.requests_made += 1 

    # group requests made by day
     
    def all_requests(self):
        Requests.new_requests[self.date] = [self.user, self.timeslots, self.status]
        print(Requests.new_requests)

    # given requests made, select one request to approve
    def accept_this_request(user):
        for key, value in Requests.new_requests.items():
            print(key, value)
            if (value[0] == user):
                times_accepted = value
                print(times_accepted)

            if (value[0] != user):
                times_4review = value
                print(times_4review)
    # check if the approval of one request affected any other
    def review_other_requests(cls):
        for item1 in cls.times_accepted[1]:
            for item2 in cls.times_4review[1]:
                if item1 == item2:
                    print(item1)
            

    """
    def display_requests():
        print("Requests made today:")
        for key, value in Requests.new_requests.items():
            print (f"\n\t{key}: {value}")
            
            def cancel_request():
        print(Requests.times_accepted)
        if item1 in times_4review[0]:
                    print('yay')



                #print(f"times_4review: {times_4review}")

            i=0
                while i<len(times_accepted):
                    if times_accepted[i] in times_4review[0]:
                        times_4review[1] = 'declined'
                        i+=1
                    
                print(times_4review)
"""
                    
           
                
                
req_1 = Requests('Jill','dd/mm/yy', ['1-2', '3-6'])
req_2 = Requests('nuse', 'dd/mm/yy', ['1-2', '8-6'])
req_3 = Requests('Josl', 'dd/mm/yy', ['2-1', '3-6'])
req_4 = Requests('Jodjd', 'dd/mm/yy', ['1-2', '9-6'])

Requests.all_requests(self)
Requests.accept_this_request('nuse')

#Requests.cancel_request()
#Requests.cancel_request(Requests.accept_request("nuse"))
#print(Requests.requests_made)
#Requests.display_requests()
#req_1.review_request('')
#print(req_1.status)