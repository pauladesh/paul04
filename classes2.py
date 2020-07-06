class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination=destination
        self.duration=duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

def main():
    f1=Flight(origin="Cuttuck", destination="Surat", duration=240)
    f1.print_info()
    f2=Flight(origin="Mangalore", destination="Istanbul", duration=400)
    f2.print_info()
if __name__=='__main__':
    main()
