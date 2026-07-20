import csv
from .student import Student

STUDENTS_FILE = "data/students.csv"

def get_students(): 
    try:
        with open(STUDENTS_FILE, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            students = []
            for row in reader:
                if not row:
                    continue                
                students.append(Student(row["name"],row["section"],float(row["spanish_grade"]),float(row["english_grade"]),float(row["social_studies_grade"]),float(row["science_grade"])))
                
            return students
    except FileNotFoundError:
        return []

def set_students(students):  
    fieldnames = ["name", "section", "spanish_grade", "english_grade", "social_studies_grade", "science_grade"]
    with open(STUDENTS_FILE, 'w', newline='', encoding='utf-8') as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames)
        writer.writeheader()
        if students:
            rows = []
            for s in students:
                rows.append(s.transform_to_dict())
            writer.writerows(rows)



