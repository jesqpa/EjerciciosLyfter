from menu.menu import send_menu
from data.students import get_students, set_students

def main():
    print("Welcome to the Student Control System")
    # Cargar datos en memoria una sola vez
    students = get_students()
    
    # Pasar datos al menú
    send_menu(students)
    
    # Guardar datos al cerrar
    set_students(students)
    print("Data saved. Goodbye!")

if __name__ == "__main__":
    main()