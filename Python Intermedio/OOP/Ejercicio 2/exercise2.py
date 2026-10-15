
def load_passengers(bus):
    nombres = [
        "Ana", "Luis", "Juan", "Sofía",
        "Diego", "Lina", "Mario", "Eva",
        "Leo", "Sara", "Pablo", "Noa",
        "Iris", "Hugo", "Elia", "Raúl"
    ]
    import person
    for nombre in nombres:
        if not bus.load_passenger(person.Person(nombre)):
            break

def unload_passengers(bus):
    nombres = [
        "Hugo", "Ana", "Pablo", "Lina",
        "Raúl", "Leo", "Sofía", "Mario",
        "Iris", "Juan", "Elia", "Sara",
        "Diego", "Noa", "Luis", "Eva"
    ]    
    import person
    for nombre in nombres:
        bus.unload_passenger(person.Person(nombre)) 




def main():
    import bus

    bus = bus.Bus(10)

    print("Loading passengers...")
    load_passengers(bus)
    
    print("\nUnloading passengers...")
    unload_passengers(bus)

    

if __name__ == "__main__":
    main()