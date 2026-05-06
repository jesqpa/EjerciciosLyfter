
def delete_student():
    from data.students import get_students, set_students
    from actions.validators import validate_name, validate_section
    
    try:
        students = get_students()    
        if len(students) == 0:
            print("No registered students.")
            return

        name = validate_name("Full name of the student to delete: >>> ")
        section = validate_section("Section of the student to delete: >>> ")

        student_to_delete = None
        for student in students:
            if student['name'].lower() == name.lower() and student['section'].lower() == section.lower():
                student_to_delete = student
                break

        if student_to_delete:
            students.remove(student_to_delete)
            set_students(students)
            print(f"Student '{name}' from section '{section}' deleted successfully.")
        else:
            print(f"No student named '{name}' was found in section '{section}'.")
    
    except Exception as e:
        print(f"Error deleting the student: {e}")