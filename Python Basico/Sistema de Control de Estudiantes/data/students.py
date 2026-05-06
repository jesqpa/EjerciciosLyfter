import json

STUDENTS_FILE = "data/students.json"

def get_students(): 
    try:
        with open(STUDENTS_FILE, 'r', encoding='utf-8' ) as json_file: 		
            return json.load(json_file)
    except FileNotFoundError:
        return []

def set_students(students):  
    with open(STUDENTS_FILE, 'w', encoding='utf-8' ) as json_file: 
        json.dump(students, json_file)




