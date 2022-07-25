# write a simple program
# that illustrates the flow of power
# throughout the bike(i.e battery, controller, throtle, motor)

batteries1 = [["a", "full"]["b", "empty"]]
switch1 = ("a", "none", "b")
# ignition
# checks if bike is on
# returns True or False
def is_ignited():
    # switches (a, b, c)
    # checks battery power status, switch selection
    # returns True of False
    def is_battery(batteries, switch):
        i = 0
        while i < len(batteries):
            if batteries[i][1] == "full" and switch == batteries[i][0]:
                print(f"we have power in {batteries[i][0]}")
                i = i + 1
                return True
    is_battery(batteries1[], switch1)
is_ignited()

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

