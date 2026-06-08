
def repeat_twice(func):
    """Decorator that executes the function twice"""
    def wrapper(*args):
        func(*args)
        func(*args)
    return wrapper


@repeat_twice
def greet(name):
    print(f"Hola, {name}")


def main():
    greet("Carlos")


if __name__ == "__main__":
    main()