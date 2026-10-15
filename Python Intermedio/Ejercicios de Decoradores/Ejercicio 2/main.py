class Calculadora:    
    
    class ValidarNumeros:
        """Decorador que valida que todos los parámetros sean números"""
        def __init__(self, func):
            self.func = func
        
        def __call__(self, *args):
            for arg in args:
                if type(arg) not in (int, float):
                    raise TypeError(f"Parámetro debe ser número, no {type(arg).__name__}")
            return self.func(*args)
    
        @ValidarNumeros
        @staticmethod
        def sumar(a, b):
            return a + b
        
        @ValidarNumeros
        @staticmethod
        def multiplicar(x, y, z):
            return x * y * z


def main():
    # Casos válidos
    print("Sumar 5 + 3 =", Calculadora.sumar(5, 3))
    print("Multiplicar 2 * 3 * 4 =", Calculadora.multiplicar(2, 3, 4))
    
    


if __name__ == "__main__":
    main()