class Flight:
    counter = 1
    def __init__(self, origin, destination, duration):
        self.id=Flight.counter
        Flight += 1

        self.passengers[]

        self.origin=origin
        self.destination=destination
        self.duration=duration
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
    print()
    print("Passengers:")
    for passenger in self.passengers:
        print(f"{passenger.name}")

    def delay(self, amount):
        self.amount += amount
    def add_passenger(self, p)
        self.passenger.append(p)
        p.flight_id=self.id

class Passenger:
    def __init__(self, name):
        self.name=name
