from actions.actions import action

def print_menu(menu_options):
    print(">>> Selecione la acción a realizar") 
    for key, value in menu_options.items():
        print(f"{key}. {value}")

def validate_input(menu_options):    
    input_user = input(">>> ")
    if input_user in menu_options:
        action(input_user)            
    else:
        print("Opción no válida, por favor seleccione una opción del menú.")
        validate_input(menu_options)


def send_menu():
    menu_options = {
        "1": "Agregar estudiantes",
        "2": "Mostrar información de estudiantes",
        "3": "Mostrar promedios de estudiantes",
        "4": "Mostrar mejores promedios estudiantes",
        "5": "Exportar información de estudiantes",
        "6": "Importar información de estudiantes",
        "7": "Eliminar estudiante",
        "8": "Mostrar estudiantes reprobados"
    }
    print_menu(menu_options)    
    validate_input(menu_options)