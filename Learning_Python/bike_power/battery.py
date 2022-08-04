# fuction0: is_ignited
# checks if bike is i.e
# if key is inserted or not
key0 = True
key1 = False
def is_ignited(key):
    #prep data for reading
    if key:
        batteries = [["a", "full"],["b", "empty"]]
        switch= ("a", "none", "b")
        switch_a = switch[0]
        switch_none = switch[1]
        switch_b = switch[2]
        battery_a = batteries[0]
        battery_b = batteries[1]
        print(f"{battery_a} is {battery_a[1]}")
        print(f"{battery_b} is {battery_b[1]}")
        

        # fuction1: is_battery
        # switches (a, b, c)
        # checks battery power status, switch selection
        # returns True of False
        def is_battery(battery, switch):
            battery_name = battery[0]
            battery_status = battery[1]
            if (switch == battery_name) and (battery_status == "full"):
                print(f"Switch is on, and battery '{battery_name}' is charged --> Ignition Ready!")
            elif (switch == battery_name) and (battery_status == "empty"):
                print(f"Switch is on, but battery '{battery_name}' isn't charged")
            elif (switch != battery_name) and (battery_status == "full"):
                print(f"Switch not on, but battery '{battery_name}' is charged")
            elif (switch != battery_name) and (battery_status == "empty"):
                print(f"Switch not on, and neither is battery '{battery_name}' charged")
        is_battery(battery_a, switch_a)
        is_battery(battery_a, switch_none)
        is_battery(battery_a, switch_b)
        is_battery(battery_b, switch_b)
        is_battery(battery_b, switch_a)
        is_battery(battery_b, switch_none)

is_ignited(key0)