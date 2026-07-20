from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def get_info(self):
        return f"{self.brand} - {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()} - {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def get_info(self):
        return f"{super().get_info()} - {self.type} motorcycle"


def main():
    car = Car("Toyota", 2020, 4)
    motorcycle = Motorcycle("Harley-Davidson", 2019, "Cruiser")

    print(car.get_info())
    print(motorcycle.get_info())

if __name__ == "__main__":
    main()