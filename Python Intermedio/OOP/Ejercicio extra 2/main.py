class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Hace un sonido"


class Dog(Animal):
    def speak(self) -> str:
        return "Guau"


class Cat(Animal):
    def speak(self) -> str:
        return "Miau"


def main():
    dog = Dog("Firulais")
    cat = Cat("Misingo")

    
    print(f"{dog.name} (Perro) hace: {dog.speak()}")
    print(f"{cat.name} (Gato) hace: {cat.speak()}")


if __name__ == "__main__":
    main()