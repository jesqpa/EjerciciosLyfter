def validate_grade(text):
    while True:
        try:
            grade = float(input(text))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: La nota debe estar entre 0 y 100. Por favor, ingrese una nota válida.")             
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def validate_name(text):
    while True:
        name = input(text).strip()
        if name == "":
            print("Error: El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")
        elif any(char.isdigit() for char in name):
            print("Error: El nombre no puede incluir números. Por favor, ingrese un nombre válido.")
        else:
            return name

def validate_section(text):
    import re
    while True:
        section = input(text).strip().upper()
        if section == "":
            print("Error: La sección no puede estar vacía. Por favor, ingrese una sección válida.")
            continue        
        pattern = r"^(1[0-1]|[1-9])[A-G]$"
        if re.match(pattern, section):
            return section
        else:
            print("Error: La sección debe tener el formato correcto: (ej: 11B). De 1 a 11 y de A a G . Por favor, ingrese una sección válida.")

def validate_number_of_students(text):
    while True:
        try:
            num_students = int(input(text))
            if num_students > 0:
                return num_students
            else:
                raise ValueError("El número de estudiantes debe ser un entero positivo.")                
        except ValueError as error:
            print(f"Error: {error}. Ingrese un valor numérico válido.")

def validate_not_duplicate(students, new_student):   
    try:          
        for student in students:  
            if (student["name"].lower() == new_student["name"].lower() and student["section"].upper() == new_student["section"].upper()):
                raise ValueError(f"El estudiante {new_student['name']} en la sección {new_student['section']} ya existe. No se pueden agregar estudiantes duplicados.")
    except ValueError as error:
        print(f"Error: {error} El estudiante no se agregará.")
        return False
    return True
