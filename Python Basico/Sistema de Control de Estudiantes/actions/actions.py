
def ask_repeat_action():
    while True:
        repeat = input("¿Desea realizar otra acción? (s/n): >>> ").strip().lower()
        if repeat in ("s", "si"):
            from menu.menu import send_menu
            send_menu()
            break
        elif repeat in ("n", "no"):
            print("Gracias, se cierra el programa.")
            break
        else:
            print("Opción no válida. Ingrese 's' o 'n'.")


def action(input_user):
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
        file_path = validate_csv_export("Indique el nombre del archivo CSV a exportar (ej: estudiantes.csv): >>> ")
        export_students_to_csv(file_path)
    elif input_user == "6":
        from data.import_students import import_students_from_csv
        from actions.validators import validate_csv_import
        file_path = validate_csv_import("Indique el nombre del archivo CSV a importar (ej: estudiantes.csv): >>> ")
        import_students_from_csv(file_path) 
    elif input_user == "7":        
        from actions.delete_student import delete_student
        delete_student()        
    elif input_user == "8":
        from actions.view_students import view_reprobed_students
        view_reprobed_students()        

    ask_repeat_action()
