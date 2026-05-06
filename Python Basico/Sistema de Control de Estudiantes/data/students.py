import json

STUDENTS_FILE = "data/students.json"

def get_students(): 
    try:
        with open(STUDENTS_FILE, 'r', encoding='utf-8' ) as file: 		
            return json.load(file)
    except FileNotFoundError:
        return []

def set_students(students):  
    with open(STUDENTS_FILE, 'w', encoding='utf-8' ) as file: 
        json.dump(students, file)




