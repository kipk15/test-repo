# write a simple program
# that illustrates the flow of power
# throughout the bike(i.e battery, controller, throtle, motor)


# fuction0: is_ignited
# checks if bike is i.e
# if key is inserted or not
key0 = True
key1 = False
def is_ignited(key):
    #prep data for reading
    if key:
        batteries1 = [["a", "full"],["b", "empty"]]
        switch1 = ("a", "none", "b")
        # fuction1: is_battery
        # switches (a, b, c)
        # checks battery power status, switch selection
        # returns True of False
        def is_battery(batteries, switch):
            switch_status = switch[0]
            i = 0
            while i < len(batteries):
                battery_name = batteries[i][0]
                battery_status = batteries[i][1]
                if (switch_status == battery_name) and (battery_status == "full"):
                    print(f"we have power in {battery_name}, ready to ignite")
                if (switch_status == battery_name) and (battery_status == "empty"):
                    print(f"we do not have power in {battery_name}")
                if (switch_status != battery_name) and (battery_status == "full"):
                    print(f"The switch is not on, press {battery_name} to use battery")
                if (switch_status != battery_name) and (battery_status == "empty"):
                    print(f"The switch is not on, and neither does the battery have power")
                i = i + 1
        is_battery(batteries1, switch1)
is_ignited(key0)

    # checks if battery power reaches
    # the controller
    # returns True or False
    #def is_controller()

    # checks if bike throttle is in use
    # returns true or false
    #def is_throttle()

    # checks if both brakes are not engaged
    # returns True or False
    #def is_brakes()

