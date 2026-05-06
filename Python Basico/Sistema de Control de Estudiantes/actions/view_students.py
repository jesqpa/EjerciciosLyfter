def get_average_grade(student):
    average = (student["spanish_grade"] + student["english_grade"] + student["social_studies_grade"] + student["science_grade"]) / 4 
    return average

def print_students_list(students):
    print("Lista de Estudiantes:")
    for i, student in enumerate(students, start=1):
        print(f"- Estudiante: {i} \n\tNombre: {student['name']}, \n\tSección: {student['section']}, \n\tNota de Español: {student['spanish_grade']}, \n\tNota de Inglés: {student['english_grade']}, \n\tNota de Sociales: {student['social_studies_grade']}, \n\tNota de Ciencias: {student['science_grade']}")

def print_students_with_averages(students):
    print("Lista de Estudiantes con Promedio:")
    for i, student in enumerate(students, start=1):
        average = get_average_grade(student)
        print(f"\t{i}. {student['name']} - Sección: {student['section']} - Promedio: {average:.2f}")

def reprobed_students(students):    
    print("Lista de Estudiantes Reprobados:")
    reprobed = False
    for student in students:   
        grades = {
            "Español": student["spanish_grade"],
            "Inglés": student["english_grade"],
            "Sociales": student["social_studies_grade"],
            "Ciencias": student["science_grade"]
        }     
        for key, value in grades.items():
            if value < 60:
                print(f"\t- Estudiante: {student['name']} - Sección: {student['section']} - Materia: {key} - Nota: {value}")
                reprobed = True
    if not reprobed:
        print("No hay estudiantes reprobados.")
        
def print_top_students(students, top_n=3):
    students_with_averages = [(student, get_average_grade(student)) for student in students]
    sorted_students = sorted(students_with_averages, key=lambda x: x[1], reverse=True)
    top_students = sorted_students[:top_n]

    print(f"Top {top_n} Estudiantes con Mejor Promedio:")
    for i, (student, average) in enumerate(top_students, start=1):
        print(f"\t{i}. {student['name']} - Sección: {student['section']} - Promedio: {average:.2f}")

def view_top_students():
    from data.students import get_students
    
    try:    
        students = get_students()    
        if len(students) == 0:
            print("No hay estudiantes registrados.")
            return

        print_top_students(students)
    
    except Exception as e:
        print(f"Error al obtener la lista de estudiantes: {e}")
        return

    

def view_students():
    from data.students import get_students

    try:    
        students = get_students()
        if len(students) == 0:
            print("No hay estudiantes registrados.")
            return

        print_students_list(students)
        
    except Exception as e:
        print(f"Error al obtener la lista de estudiantes: {e}")
        return

def view_reprobed_students():
    from data.students import get_students

    try:    
        students = get_students()    
        if len(students) == 0:
            print("No hay estudiantes registrados.")
            return

        reprobed_students(students)

    except Exception as e:
        print(f"Error al obtener la lista de estudiantes: {e}")
        return

def view_students_with_averages():
    from data.students import get_students

    try:    
        students = get_students()    
        if len(students) == 0:
            print("No hay estudiantes registrados.")
            return

        print_students_with_averages(students)
        
    except Exception as e:
        print(f"Error al obtener la lista de estudiantes: {e}")
        return