class Requests():
    new_requests = {}
    times_accepted = {}
    times_4review = {}
    requests_made = 0

    def __init__(self, user, date, timeslots=[], status='pending'):
        self.user = user
        self.date = date
        self.timeslots = timeslots
        self.status = status

        Requests.requests_made += 1 

    @property 
    def request_template(self):
        Requests.new_requests[self.date] = [self.user, self.timeslots, self.status]
        return Requests.new_requests

    def display_request(cls):
        print(cls.request_template)
    
    
    @classmethod
    def accept_request(cls):
        for key, value in (cls.display_requests()):
            if key == date:
                print (value)
            

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



Requests.display_request(Requests)
"\n"
#Requests.cancel_request()
#Requests.cancel_request(Requests.accept_request("nuse"))
#print(Requests.requests_made)
#Requests.display_requests()
#req_1.review_request('')
#print(req_1.status)