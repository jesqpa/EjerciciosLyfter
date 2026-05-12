from actions.actions import action

def print_menu(menu_options):
    print(">>> Select the action to perform")
    for key, value in menu_options.items():
        print(f"{key}. {value}")

def validate_input(menu_options):    
    input_user = input(">>> ")
    if input_user in menu_options:
        action(input_user)            
    else:
        print("Invalid option, please select an option from the menu.")
        validate_input(menu_options)


def send_menu():
    menu_options = {
        "1": "Add students",
        "2": "Show students information",
        "3": "Show students averages",
        "4": "Show top students averages",
        "5": "Export students information",
        "6": "Import students information",
        "7": "Delete student",
        "8": "Show failed students",
        "9": "Exit"
    }
    print_menu(menu_options)    
    validate_input(menu_options)