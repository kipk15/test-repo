# A program to build user's profiles
# by utilizing modules

# 1. import entire module
import profile

import format_name as f_name
formatted_name = f_name.get_formatted_name('Nelson', 'Keys', 'Soja', init = 'Mr.')

# to call, enter the name of the module,
# followed by the name of the function,separated by a dot
# eg profile.build_profile 
user_profile_01 = profile.build_profile(formatted_name, Age = 30, occupation = 'doctor' )
print ("\n",user_profile_01)