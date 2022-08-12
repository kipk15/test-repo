
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

        

       

#print("\n",Request.all_user_requests)

#print("\n",Request.all_users,"\n")


        