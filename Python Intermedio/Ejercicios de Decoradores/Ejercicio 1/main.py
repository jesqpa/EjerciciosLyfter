

class PrintInfo:
    """Decorador en forma de clase que imprime parámetros y retorno"""
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"Parámetros: {args} {kwargs}")
        resultado = self.func(*args, **kwargs)
        print(f"Retorno: {resultado}")
        return resultado


@PrintInfo
def sumar(a, b):
    return a + b


@PrintInfo
def saludar(nombre):
    return f"Hola, {nombre}!"


def main():
    sumar(5, 3)
    saludar("Carlos")


if __name__ == "__main__":
    main()