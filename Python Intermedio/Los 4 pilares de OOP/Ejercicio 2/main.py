
class Shape():
    def __init__(self, name):
        self.__name = name

    def calculate_perimeter(self):
        pass
        
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.__radius

    def calculate_area(self):
        return 3.14159 * self.__radius ** 2

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.__side = side

    def calculate_perimeter(self):
        return 4 * self.__side

    def calculate_area(self):
        return self.__side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.__base = base
        self.__height = height

    def calculate_perimeter(self):
        return self.__base + self.__height * 2

    def calculate_area(self):
        return 0.5 * self.__base * self.__height

def main():
    radius = int(input("Ingrese el radio del circulo: >> "))
    circle = Circle(radius)
    print(f"Perimetro circulo: {circle.calculate_perimeter()}")
    print(f"Area circulo: {circle.calculate_area()}")

    side = int(input("Ingrese el lado del cuadrado: >> "))
    square = Square(side)
    print(f"Perimetro cuadrado: {square.calculate_perimeter()}")
    print(f"Area cuadrado: {square.calculate_area()}")

    base = int(input("Ingrese la base del triangulo: >> "))
    height = int(input("Ingrese la altura del triangulo: >> "))
    triangle = Triangle(base, height)
    print(f"Perimetro triangulo: {triangle.calculate_perimeter()}")
    print(f"Area triangulo: {triangle.calculate_area()}")


if __name__ == "__main__":
    main()