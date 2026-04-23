def get_lastname():
    lastname = input("Indique su apellido: ")
    print(f"Su apellido es: {lastname}")    


def get_name():
    name = input("Indique su nombre: ")
    print(f"Su nombre es: {name}")
    get_lastname()


get_name()