class Controller():
    # class variables
    
    #instance variables
    def __init__(self, model, volts, oc_protection, dom):
        self.self.volts = volts
        self.oc_protection = oc_protection
        self.dom = dom
        self.model = model

    @property # access this method as an attribute
    def controller_info(self):
        controller_specs = (
                f"\n\tModel: {self.model}"
                f"\n\tWorking Voltage: {self.volts} Volts"
                f"\n\tOver-Current Protection: {self.oc_protection} Ah"
                f"\n\tDate of Manufacture: {self.dom}")
        return (controller_specs)

controller_0 = Controller('DHFKW3849WS', 60, 15, '04/05/2022')
print(f"{controller_0.controller_info}")
