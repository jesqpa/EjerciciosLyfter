name = "Carlos"

def set_name():
    print(f"El nombre original es: {name}")
    name = input("Indique su nombre: ")
    print(f"Su nombre es: {name}")


set_name()
print(f"Desde afuera: {name}")