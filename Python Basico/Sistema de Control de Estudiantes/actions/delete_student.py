
def delete_student():
    from data.students import get_students, set_students
    from actions.validators import validate_name, validate_section
    
    students = get_students()
    
    name = validate_name("Ingrese el nombre completo del estudiante a eliminar: >>> ")
    section = validate_section("Ingrese la sección del estudiante a eliminar (ej: 11B): >>> ")
    
    student_to_delete = None
    for student in students:
        if student["name"].lower() == name.lower() and student["section"].upper() == section.upper():
            student_to_delete = student
            break
    
    if (student_to_delete):
        students.remove(student_to_delete)
        set_students(students)
        print(f"El estudiante {name} en la sección {section} ha sido eliminado.")
    else:
        print(f"No se encontró un estudiante con el nombre {name} en la sección {section}.")