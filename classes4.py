class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # Keep track of id number.
        self.id = Flight.counter  #whatever the counter is, that going to be the id.
        Flight.counter += 1 #Next time when you create a Flight, then counter will increment by 1.

        # Keep track of passengers.
        self.passengers = []    # maintain list of all passengers in a flight.

        # Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

    print()
    print("Passengers:")
    for passenger in self.passengers:   #self.passenger is a list.
        print(f"{passenger.name}") #name is parameter of Passenger class

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):   #self is Flight class object and p is Passenger class object.
        self.passengers.append(p) #self.passengers is list to which we append passengers (see line 53-54).
        p.flight_id = self.id #we uptdate passenger object to keep track of what flight is associated


class Passenger:

    def __init__(self, name):
        self.name = name    #Keeping track of its own name.


def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)

    # Create passengers.
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    # Add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    # Add delay.
    f1.delay(60)

    f1.print_info()


if __name__ == "__main__":
    main()
