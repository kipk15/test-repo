schedule = {
    '08/05/21': {
        'available': ['11am', '12pm', '1pm', '2pm', '3pm', '4pm', '7pm'],
        'accepted': [],
        'pending': []},
        '08/06/21': {
        'available': ['11am', '1pm', '4pm', '7pm'],
        'accepted': [],
        'pending': [],
        }
    }
class Request():

    def __init__(self, user_info, request_info):
        self.user_info = self.User()

        self.request_info = self.Request()
    
    
    class User():
        
        def __init__(self, fname, lname, email, phone):
            self.fname = fname
            self.lname = lname
            self.email = email
            self.phone = phone

        @property
        def user_info(self):
            return(self.fname, self.lname, self.email, self.phone)

        def create_request(self, date, timeslots=[]):
            request = []

            if date in schedule.keys():
                for time in timeslots:
                    cond1 = (time in schedule[date]['available'])
                    if cond1:
                        request.append([self.email, time]) 
                    if not cond1:
                        request=[]
                        print(f"\nSorry, {self.fname.title()}, {time} is currently not"
                            f" available on {date}. Please revise your request accordingly")
                        break
    
                schedule[date]['pending'].extend(request)

            else:
                print(f'\n {self.fname.title()}, We do not currently have anything available on {date}.')
                   

            return(schedule)



