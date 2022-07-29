# using arbitrary arguments
# accepts as many key-value pairs
# as the calling statement provides

# inputs 
# create a profile based on information from 

def build_profile(formatted_name, **user_info):
    """build a dictionary containing
        everything we know about a user"""
    if formatted_name:
        user_info['name'] = formatted_name
    return user_info

import format_name as f_name
formatted_name = f_name.get_formatted_name('Nelson', 'Keys', 'Soja', init = 'Mr.')

# to call, enter the name of the module,
# followed by the name of the function,separated by a dot
# eg profile.build_profile 
user_profile_01 = profile.build_profile(formatted_name, Age = 30, occupation = 'doctor' )
