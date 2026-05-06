

def add_students():
    from data.students import get_students, set_students

    students = get_students()   
    from actions.validators import validate_name, validate_section, validate_grade, validate_not_duplicate, validate_number_of_students
    num_students = validate_number_of_students("Cuántos estudiantes desea agregar? >>> ")
    
    try:
        for i in range(num_students):            

            name = validate_name(f"Nombre completo del estudiante {i + 1}: >>> ")
            section = validate_section(f"Sección del estudiante: >>> ")
            spanish_grade = validate_grade(f"Nota de español: >>> ")
            english_grade = validate_grade(f"Nota de inglés: >>> ")
            social_studies_grade = validate_grade(f"Nota de estudios sociales: >>> ")
            science_grade = validate_grade(f"Nota de ciencias: >>> ")
            student = {
                "name": name,
                "section": section,
                "spanish_grade": spanish_grade,
                "english_grade": english_grade,
                "social_studies_grade": social_studies_grade,
                "science_grade": science_grade
            }
            if(validate_not_duplicate(students, student)):
                students.append(student)   
                set_students(students)
            
    except ValueError as error:
        print(f"Error: {error}. ")