class Transport:
    # class variables
    Allocated_fare = 0
    fare = 100
    means = 0

    def __init__ (self, preference, travel_buddy):
        self.preference = preference
        self.travel_buddy = travel_buddy

    def Calculate_fare(self):
        
        if self.preference == 'plane':
            means = 3

        elif self.preference == 'car':
            means = 2
        
        elif self.preference == 'foot':
            means = 1 
        
        Total_fare = (means*self.fare) + (means*self.fare*self.travel_buddy)
        print(Total_fare) 

bu = Transport('plane', 2)
bi = Transport('car', 1)
ba = Transport('foot', 2)

bu.Calculate_fare()
bi.Calculate_fare()
ba.Calculate_fare()
