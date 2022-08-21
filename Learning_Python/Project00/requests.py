schedule = {
    '08/05/21': {
        'available': ['11am', '12pm', '1pm', '3pm', '7pm'],
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
                        print(f"Sorry, {self.fname.title()}, some of your requested"
                            " times are currently not available on our schedule")
                        break
    
                schedule[date]['pending'].extend(request)
               
                    


            else:
                print(f'Date, {date}, not available'
                    'Please select date available on schedule')

            return(schedule)



