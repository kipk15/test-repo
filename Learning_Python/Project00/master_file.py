# these are called dictionaries

# 0) it all start with asking user for the date of their session
# to be replaced by actual date time?
r_date_input = input("\nPlease select the date of your session ")

# 1) there is a constant availability
# there is a function that adjusted the availability
# "schedule" dictionary needs work. it has to keep track of status
# i.e. there could be list of requests, or it can be open/closed
availability = {"date": "a", "schedule": [["open", "1 pm - 2 pm"],["booked", "2 pm - 3 pm"],["open", "3 pm - 4 pm"],["open", "4 pm - 5 pm"]]}

# 2) requests keeps track of users submitting requests for particular times slots
# the admin will have the ability to look through the requests, and for 
# a particular user, accept it. This will adjust the schedule for the times the
# request was for, and reject the requests that were for similar times
requests = {"date": "a", "schedule": [["user1", ["1 pm - 2 pm", "3 pm - 4 pm"]], ["user3", ["1 pm - 2 pm", "4 pm - 5 pm"]], ["user4", ["4 pm - 5 pm"]]]}

# create a request function
# user is presented with available dates
# then user indicates whether they are interested in any

""" 
reqs = ['new_user', ['1 pm - 2 pm', '3 pm - 4 pm']]
requests = {"date": "a", "schedule": [["user1", ["1 pm - 2 pm", "3 pm - 4 pm"]], ["user3", ["1 pm - 2 pm", "4 pm - 5 pm"]], ["user4", ["4 pm - 5 pm"]]]}
def add_request(req, requestas):
    i=0
    time_stamp = []
    while (i < len(reqs[1])):
        print(f'\n time {i}: {req[1][i]}')
        time_stamp.append(req[1][i])
        i=i+1
    return ()

        

add_request(reqs, requests)

"""
#gets updated request from add_request fuction
#and asks admin what user's time-slots would they want to approve
updated_requests = []
user_select = input('which user would you like to approve?: ')
admins_answer = 
def confirm_request(requests):

def schedule_function(date):
    if (availability["date"]==date):
        i = 0
        print("\nHERE ARE THE AVAILABLE TIMES: \n")
        while i < len(availability["schedule"]):
            if (availability["schedule"][i][0] == "open"):
                print(availability["schedule"][i][1])
            i = i + 1
        proceed = input("\nwould you like to proceed with booking these? indicate with 'yes' or 'no': ")

        if (proceed == "yes"):
            i = 0
            req = ["user2", []]
            print("\nplease indicate which time slots are you interested in: ")
            while i < len(availability["schedule"]):                     
                day = availability["schedule"][i][1]          

                if (availability["schedule"][i][0] != "open"):
                    i = i + 1

                if (availability["schedule"][i][0] == "open"):
                    # prompt here
                    choice = input(f"would you like to book {day} ? indicate with 'yes' or 'no': ")          
                    
                    if (choice == "no"):
                        i = i + 1
                    # create a request dictionary
                    # store requeqst day, and stores list of lists indicating preference

                    if (choice == "yes"):
                        req[1].append(availability["schedule"][i][1])
                        i = i + 1
            i = 0
            print("\nYou requested: ")
            while i < len(req[1]):
                print(req[1][i])
                i = i + 1
            booking_confirm = input("\nwould you like to submit this booking request? indicate with 'yes' or 'no': ")
            
            if (booking_confirm == "yes"):
                requests["schedule"].append(req)
            print("\nawesome, thanks!")
            print("we'll get back to you shortly about confirmation!")
            # conditional statement -- if yes then we store the request for that time slot
            # inside the availability object, specifically for the 
        
        
        # figure out how to deal with user submitting != n or != y
        # if (proceed != "y" or proceed != "n"):
        #     proceed = input("wrong answer. please select either y or n")


        # booking_function():
        #     booking_request = availability["schedule"]
            # loop through booking_request, ask for user input
            # print("would you like to book {availability["schedule"][i][1]}))")
    else:
        print("we don't have schedule for this day")

#schedule_function(r_date_input)

#write a request function, that adds request 
