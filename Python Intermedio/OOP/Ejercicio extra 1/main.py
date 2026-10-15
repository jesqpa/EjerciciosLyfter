


def validate_numeric(value_str: str) -> float:    
    try:
        return float(value_str)
    except ValueError:
        raise ValueError("El valor ingresado no es un número válido.")


def validate_positive(value: float) -> float:    
    if value < 0:
        raise ValueError("El valor no puede ser negativo.")
    return value


def ask_positive_float(prompt: str) -> float:    
    while True:
        try:
            raw_input = input(prompt).strip()
            numeric_value = validate_numeric(raw_input)
            positive_value = validate_positive(numeric_value)
            return positive_value
        except ValueError as ve:
            print(f"Error: {ve} Por favor, intente de nuevo.")


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self: float):
        area = self.width * self.height
        return area
    
    def get_perimeter(self: float):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

def main():

    height = ask_positive_float("Ingrese la altura: ")
    width = ask_positive_float("Ingrese el ancho: ")
    
    try:
        rect = Rectangle(width, height)

        area = rect.get_area()
        perimeter = rect.get_perimeter()

        print(f"El área del rectángulo es: {area}")
        print(f"El perímetro del rectángulo es: {perimeter}")

    except Exception as e:
        print(f"Error en creación del rectángulo: {e}")


if __name__ == "__main__":
    main()
