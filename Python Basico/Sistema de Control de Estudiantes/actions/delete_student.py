
def delete_student():
    from data.students import get_students, set_students
    from actions.validators import validate_name, validate_section
    
    try:
        students = get_students()    
        if len(students) == 0:
            print("No hay estudiantes registrados.")
            return

        name = validate_name("Nombre completo del estudiante a eliminar: >>> ")
        section = validate_section("Sección del estudiante a eliminar: >>> ")

        student_to_delete = None
        for student in students:
            if student['name'].lower() == name.lower() and student['section'].lower() == section.lower():
                student_to_delete = student
                break

        if student_to_delete:
            students.remove(student_to_delete)
            set_students(students)
            print(f"Estudiante '{name}' de la sección '{section}' eliminado exitosamente.")
        else:
            print(f"No se encontró un estudiante con el nombre '{name}' en la sección '{section}'.")
    
    except Exception as e:
        print(f"Error al eliminar el estudiante: {e}")