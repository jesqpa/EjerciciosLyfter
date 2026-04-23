def get_initial_number():
    """Solicita el número inicial al usuario."""
    try:
        return int(input("Ingrese el número inicial >> "))
    except ValueError:
        print("**ERROR** Debe ingresar un número válido")
        return None


def show_menu():
    """Muestra el menú de opciones."""
    print("Indique el número de la operación a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")
    print("6. Finalizar")


def get_operation():
    """Obtiene una operación válida del usuario."""
    try:
        operation = int(input(">> "))
        if operation < 1 or operation > 6:
            raise ValueError
        return operation
    except ValueError:
        print("***ERROR*** Operación inválida")
        return None


def get_next_number():
    """Solicita el siguiente número para operar."""
    try:
        return int(input("Ingrese el siguiente número >> "))
    except ValueError:
        print("***ERROR*** Debe ingresar un valor válido")
        return None

    
def add(a, b):        
    return a + b


def subtract(a, b):        
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def perform_operation(current, operation, number):
    """Ejecuta la operación matemática."""
    if operation == 1:
        return add(current, number)
    elif operation == 2:
        return subtract(current, number)
    elif operation == 3:
        return multiply(current, number)
    elif operation == 4:
        if number == 0:
            raise ZeroDivisionError
        return divide(current, number)


def show_result(result):
    """Muestra el resultado en pantalla."""
    print("**********************************************")
    print(f"El resultado de la operación es: {result}")
    print("**********************************************")


def calculator():
    """Función principal que controla el flujo."""
    calculated = get_initial_number()
    if calculated is None:
        return

    while True:
        show_menu()
        operation = get_operation()

        if operation is None:
            continue

        if operation == 6:
            print("Calculadora finalizada!!")
            break

        if operation == 5:
            calculated = 0
            print("Resultado borrado.")
            continue

        number = get_next_number()
        if number is None:
            continue

        try:
            calculated = perform_operation(calculated, operation, number)
            show_result(calculated)
        except ZeroDivisionError:
            print("***ERROR*** No se puede dividir entre cero")


calculator()