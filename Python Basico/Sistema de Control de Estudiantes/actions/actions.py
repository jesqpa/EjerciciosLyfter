
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
        print("")
    elif input_user == "6":
        print("")
    elif input_user == "7":
        from actions.delete_student import delete_student
        delete_student()        
    elif input_user == "8":
        print("")

    ask_repeat_action()
