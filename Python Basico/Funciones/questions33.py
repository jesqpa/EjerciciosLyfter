def set_name():
    global name
    name = input("Indique su nombre: ")
    print(f"Su nombre es: {name}")

def print_name():    
    print(f"Desde otra función: {name}")

set_name()
print_name()