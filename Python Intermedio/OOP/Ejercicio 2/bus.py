class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def load_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus.")
            return True
        else:
            print("Bus is full!")
            return False
    
    def unload_passenger(self, person):
        name = person if isinstance(person, str) else getattr(person, "name", None)
        for passenger in self.passengers:
            if passenger.name == name:
                self.passengers.remove(passenger)
                print(f"{passenger.name} has left the bus.")
                return True
        print(f"{name} is not on the bus!")
        return False
        

