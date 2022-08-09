class App():
    users_count = 0
    users = []

    all_requests = []
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
            request = [self.fname, date, [timeslots]]

            App.requests_count += 1
            App.all_requests.append(request)

            return(App.all_requests)

user1 = App.User('Joe', 'Roe', 'jR@email.com', '315 328 9034')
print(user1.create_request('dd/mm/yy', ['1pm-2pm', '2pm-3pm']))


        