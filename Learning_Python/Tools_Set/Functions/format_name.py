def get_formatted_name(first_name, last_name, middle_name = '', init=None):
    """ return a full name, neatly formatted """
    # init and middle name are optional?
    if init:
        full_name = f"{init} {first_name} {middle_name} {last_name}"
    elif middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()