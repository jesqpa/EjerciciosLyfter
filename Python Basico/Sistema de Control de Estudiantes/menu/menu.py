from actions.actions import action

def print_menu(menu_options):
    print(">>> Select the action to perform")
    for key, value in menu_options.items():
        print(f"{key}. {value}")

def validate_input(menu_options):
    while True:
        input_user = input(">>> ")
        if input_user in menu_options:
            return input_user
        print("Invalid option, please select an option from the menu.")

def send_menu(students):  
    menu_options = {
        "1": "Add students",
        "2": "Show students information",
        "3": "Show students averages",
        "4": "Show general average",
        "5": "Show top students averages",
        "6": "Export students information",
        "7": "Import students information",
        "8": "Delete student",
        "9": "Show failed students",
        "10": "Exit"
    }
    while True:
        print_menu(menu_options)
        input_user = validate_input(menu_options)
        if action(input_user, students):
            break