name = "Carlos"


def set_name(new_name=None):
    global name
    print(f"El nombre original es: {name}")

    if new_name is None:
        new_name = input("Indique su nombre: ")

    if new_name == "":
        raise ValueError("The name cannot be empty")

    name = new_name
    print(f"Su nombre es: {name}")
    return name


if __name__ == "__main__":
    set_name()
    print(f"Desde afuera: {name}")