
from datetime import datetime


def validate_numbers(func):
    """Decorator that validates all arguments are numeric"""
    def wrapper(*args, **kwargs):
        for arg in args + tuple(kwargs.values()):
            if type(arg) not in (int, float):
                raise TypeError(f"Argumento debe ser numérico, no {type(arg).__name__}")
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    """Decorator that logs function call with arguments and return value"""
    def wrapper(*args, **kwargs):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        print(f"Función: {func.__name__}")
        print(f"Argumentos: {args} {kwargs}")
        print(f"Fecha: {now}")
        print(f"Retorno: {result}")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b


def main():
    print("=== Caso válido ===")
    multiply(53,4)
    
    


if __name__ == "__main__":
    main()