def validate_grade(text):
    while True:
        try:
            grade = float(input(text))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: The grade must be between 0 and 100. Please enter a valid grade.")             
        except ValueError:
            print("Error: Enter a valid numeric value.")

def validate_name(text):
    while True:
        name = input(text).strip()
        if name == "":
            print("Error: The name cannot be empty. Please enter a valid name.")
        elif any(char.isdigit() for char in name):
            print("Error: The name cannot contain numbers. Please enter a valid name.")
        else:
            return name

def validate_section(text):
    import re
    while True:
        section = input(text).strip().upper()
        if section == "":
            print("Error: The section cannot be empty. Please enter a valid section.")
            continue        
        pattern = r"^(1[0-1]|[1-9])[A-G]$"
        if re.match(pattern, section):
            return section
        else:
            print("Error: The section must have the correct format: (e.g. 11B). From 1 to 11 and from A to G. Please enter a valid section.")

def validate_csv_import(text):
    import os
    while True:
        file_path = input(text).strip()
        if not file_path.endswith(".csv"):
            print("Error: The file name must end with '.csv'. Please enter a valid file name.")
        elif not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist. Please enter a valid file name.")
        else:
            return file_path

def validate_csv_export(text):
    import os
    while True:
        file_path = input(text).strip()
        if not file_path.endswith(".csv"):
            print("Error: The file name must end with '.csv'. Please enter a valid file name.")
        elif os.path.exists(file_path):
            overwrite = input(f"The file '{file_path}' already exists. Do you want to overwrite it? (y/n): >>> ").strip().lower()
            if overwrite in ("y", "yes"):
                return file_path
            else:
                print("Export canceled. Please enter a new file name.")
        else:
            return file_path
        
def validate_number_of_students(text):
    while True:
        try:
            num_students = int(input(text))
            if num_students > 0:
                return num_students
            else:
                raise ValueError("The number of students must be a positive integer.")                
        except ValueError as error:
            print(f"Error: {error}. Enter a valid numeric value.")

def validate_not_duplicate(students, new_student):   
    try:          
        for student in students:  
            if (student["name"].lower() == new_student["name"].lower() and student["section"].upper() == new_student["section"].upper()):
                raise ValueError(f"The student {new_student['name']} in section {new_student['section']} already exists. Duplicate students cannot be added.")
    except ValueError as error:
        print(f"Error: {error} The student will not be added.")
        return False
    return True
