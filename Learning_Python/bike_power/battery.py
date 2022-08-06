# battery class

class Battery():
    def __init__(self, voltage, switch = 'on',status = 'charged'):
        self.voltage = voltage
        self.status = status
        self.switch = switch

    @property
    def is_on(self):
        if self.switch == 'on':
            return True
        return False

    @property
    def is_charged(self):
        if self.status == 'charged':
            return True
        return False

    @property
    def capacity(self):
        return self.voltage

    def running(self):
        if self.is_on and self.is_charged:
            return True
        return False
        
battery_a = Battery(60, 'off', 'charged')
battery_b = Battery(60, 'on', 'empty')
print(battery_a.running())
print(battery_b.running())