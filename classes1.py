class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination=destination
        self.duration=duration

def main():

    f=Flight(origin='Haridwar',destination='Ernakulam',duration=345) # "f" is a variable of type Flight class.

    f.duration += 10

    print(f.origin)
    print(f.destination)
    print(f.duration)
if __name__=='__main__':
    main()
