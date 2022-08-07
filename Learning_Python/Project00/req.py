class Requests():
    new_requests = {}
    requests_made = 0

    def __init__(self, user, date, timeslot, status='pending'):
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

    def review_request(user):
        for key, value in Requests.new_requests.items():
            if key == user:
                value[1] = 'accepted'
                times_accepted = value[0]
            """else:
                i = 0
                while i < len (Requests.new_requests.values()):
                    for a in Requests.new_requests.values():
                        for b in 
                for value[0]= 'declined'"""
req_1 = Requests('Jill', 'dd/mm/yy', ['1-2', '3-6'])
req_2 = Requests('nuse', 'dd/mm/yy', ['1-2', '8-6'])
req_3 = Requests('Josl', 'dd/mm/yy', ['2-1', '3-6'])
req_4 = Requests('Jodjd', 'dd/mm/yy', ['1-2', '9-6'])
req_1.add_request()
req_2.add_request()
req_3.add_request()
req_4.add_request()


Requests.display_requests()
"\n"
Requests.review_request('nuse')
print(Requests.requests_made)
Requests.display_requests()
#req_1.review_request('')
#print(req_1.status)