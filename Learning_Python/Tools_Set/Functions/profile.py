# using arbitrary arguments
# accepts as many key-value pairs
# as the calling statement provides

# inputs 
# create a profile based on information from 

#import format_name as format, formatted_name, **user_info
def build_profile():
    """build a dictionary containing
        everything we know about a user"""
    info_needed = ['first_name', 'last_name', 'middle_name', 'age', 'occupation']
    info_entered = []
    for item in info_needed:
        if item == 'age':
            answer = (input(f"Please enter your {item}: "))
        else:
            answer = input(f"Please enter your {item}: ").lower()
        info_entered.append({item, answer})
    print (info_entered)

    nemesis = []
    i=0
    while i < len(info_entered):
        for key, value in info_entered[i]:
            if key == "first_name":
                f_name = value
            elif key == "last_name":
                l_name = value
            elif key == "middle_name":
                m_name = value
        i = i + 1
    formatted_name = format.get_formatted_name(f_name, l_name, m_name, init = 'Mr.')
    if formatted_name:
        user_info['name'] = formatted_name
    return user_info
build_profile()


# to call, enter the name of the module,
# followed by the name of the function,separated by a dot
# eg profile.build_profile 
#user_profile_01 = profile.build_profile(formatted_name, Age = 30, occupation = 'doctor' )
