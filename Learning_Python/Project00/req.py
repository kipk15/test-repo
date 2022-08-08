class Requests():
    new_requests = {}
    requests_made = 0

    def __init__(self, user, date, timeslot=[], status='pending'):
        self.user = user
        self.date = date
        self.timeslot = timeslot
        self.status = status

        Requests.requests_made += 1 
        
    def add_request(self):
        Requests.new_requests[self.user] = [self.timeslot, self.status]

    
    def display_requests():
        for key, value in Requests.new_requests.items():
            print (f"\n{key}: {value}")

    def accept_request(user):
        for key, value in Requests.new_requests.items():
            if key == user:
                value[1] = 'accepted' # change status to accepted
                times_accepted = (value[0]) # list of times accepted
                print (times_accepted)
            if key != user:
                times_4review = (value)
                    
                print (times_4review)
    """def cancel_request(cls):
        for item1 in times_accepted:
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
                    
           
                
                
req_1 = Requests('Jill', 'dd/mm/yy', ['1-2', '3-6'])
req_2 = Requests('nuse', 'dd/mm/yy', ['1-2', '8-6'])
req_3 = Requests('Josl', 'dd/mm/yy', ['2-1', '3-6'])
req_4 = Requests('Jodjd', 'dd/mm/yy', ['1-2', '9-6'])
req_1.add_request()
req_2.add_request()
req_3.add_request()
req_4.add_request()


Requests.accept_request("nuse")
"\n"
#Requests.cancel_request(Requests.accept_request("nuse"))
#print(Requests.requests_made)
#Requests.display_requests()
#req_1.review_request('')
#print(req_1.status)