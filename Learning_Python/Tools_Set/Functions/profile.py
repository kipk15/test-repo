# using arbitrary arguments
# accepts as many key-value pairs
# as the calling statement provides

def build_profile(formatted_name, **user_info):
    """build a dictionary containing
        everything we know about a user"""
    if formatted_name:
        user_info['name'] = formatted_name
    return user_info


