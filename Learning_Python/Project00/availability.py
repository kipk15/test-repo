#list_of_lists
availability = {'date': "01", "times": [["open", "3-4pm"],["open", "2-3pm"],["taken", "1-2pm"]]}

#request object
####
requests= {'date': '01', 'requests': [['user_1', ['12-1pm','4-5pm']],
['user_2', ['1-2pm', '3-4pm']], 
['user_3', ['12-1pm', '1-2pm']]]}

print()                                                                         

#print times and their status
####
user_date = input("What day do you want to make a booking for?: ")
if (user_date == availability["date"]):
        print(availability["times"][0])

#user selected a date that has available timeslots
####
        user_time =input("Which time slot would you like to book?: ")
        i=0
    #loop to see which time slot user wanted
    ###
        for i in availability["times"]:
            print (availability["times"])
            if(user_time == availability["times"]):
                    print("confirming the selection")

print("we do not have a schedule for date selected. Please revise accordingly")
        




"""  (user_input={
    date_requested = "dateR",
    time_requested = "timeR"
}


