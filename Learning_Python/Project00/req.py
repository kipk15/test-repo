schedule = {
    'dd/mm/yy1': {
        'available': ['12pm', '1pm', '7pm'],
        'accepted': [],
        'pending': []

    }
}

class Request():
    all_users = {}
    user_count = 0

    all_user_requests = {}
    request_count = 0

    def __init__(self, user_info, request_info):
        self.user_info = self.User()

        self.request_info = self.Request()
    
    
    class User():
        
        def __init__(self, fname, lname, email, phone):
            self.fname = fname
            self.lname = lname
            self.email = email
            self.phone = phone

            Request.all_users[f"user_{Request.user_count}"] = [self.fname, self.lname, self.email, self.phone]
            Request.user_count += 1
        @property
        def user_info(self):
            return(self.fname, self.lname, self.email, self.phone)

        def create_request(self, date, timeslots=[]):
            request = [self.email , date, timeslots]

            Request.all_user_requests[f'request_{Request.request_count}'] = request
            Request.request_count += 1

#user1 = Request.User('Joe', 'Roe', 'jR@email.com', '315 328 9034')
user2 = Request.User('seth', 'tue', 'St@email.com', '315 678 9034')
user3 = Request.User('hui', 'hutf', 'hH@email.com', '315 328 6774')
#user1.create_request('08/05/21', ['1pm-2pm', '2pm-3pm'])
user2.create_request('02/05/23', ['2pm-3pm', '3pm-4pm'])
#user3.create_request('03/01/05', ['5pm-6pm', '6pm-7pm'])
print("\n",Request.all_user_requests)

print("\n",Request.all_users,"\n")


        