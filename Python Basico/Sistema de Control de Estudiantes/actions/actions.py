
def ask_repeat_action():
    while True:
        repeat = input("Do you want to perform another action? (y/n): >>> ").strip().lower()
        if repeat in ("y", "yes"):
            from menu.menu import send_menu
            send_menu()
            break
        elif repeat in ("n", "no"):
            print("Thank you, the program will close.")
            break
        else:
            print("Invalid option. Enter 'y' or 'n'.")


def action(input_user):
    exit_option = False
    if input_user == "1":
        from actions.add_students import add_students
        add_students()  
    elif input_user == "2":
        from actions.view_students import view_students
        view_students()        
    elif input_user == "3":
        from actions.view_students import view_students_with_averages
        view_students_with_averages()                
    elif input_user == "4":
        from actions.view_students import view_top_students
        view_top_students()        
    elif input_user == "5":
        from data.export_students import export_students_to_csv
        from actions.validators import validate_csv_export
        file_path = validate_csv_export("Enter the CSV file name to export (e.g. students.csv): >>> ")
        export_students_to_csv(file_path)
    elif input_user == "6":
        from data.import_students import import_students_from_csv
        from actions.validators import validate_csv_import
        file_path = validate_csv_import("Enter the CSV file name to import (e.g. students.csv): >>> ")
        import_students_from_csv(file_path) 
    elif input_user == "7":        
        from actions.delete_student import delete_student
        delete_student()        
    elif input_user == "8":
        from actions.view_students import view_reprobed_students
        view_reprobed_students()    
    elif input_user == "9": 
        exit_option = True
        print("Thank you, the program will close.")   
    else:   
        print("Invalid option, please select an option from the menu.") 

    if not exit_option:
        ask_repeat_action()
