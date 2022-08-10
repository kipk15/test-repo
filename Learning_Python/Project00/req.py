schedule = {
    'dd/mm/yy1': {
        'available': ['12pm', '1pm', '7pm'],
        'accepted': [],
        'pending': []

    }
}

class Request():
    users_count = 0
    users = []

    all_requests = {}
    requests_count = 0

    def __init__(self, user_info, request_info):
        self.user_info = self.User()
        users_count += 1

        self.request_info = self.Request()
    
    def show_info(cls):
        users[f"user_1:"] = [cls.User.info]
        print(cls.users)
    
    class User():
        
        def __init__(self, fname, lname, email, phone):
            self.fname = fname
            self.lname = lname
            self.email = email
            self.phone = phone

        @property
        def info(self):
            return(self.fname, self.lname, self.email, self.phone)

        def create_request(self, date, timeslots=[]):
            request = [self.fname , date, timeslots]

            Request.requests_count += 1
            Request.all_requests[f'request_{Request.requests_count}'] = request

user1 = Request.User('Joe', 'Roe', 'jR@email.com', '315 328 9034')
user2 = Request.User('seth', 'tue', 'St@email.com', '315 678 9034')
user3 = Request.User('hui', 'hutf', 'hH@email.com', '315 328 6774')
user1.create_request('08/05/21', ['1pm-2pm', '2pm-3pm'])
user2.create_request('02/05/23', ['2pm-3pm', '3pm-4pm'])
user3.create_request('03/01/05', ['5pm-6pm', '6pm-7pm'])
print(Request.all_requests)


        