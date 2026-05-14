def get_average_grade(student):
    average = (student["spanish_grade"] + student["english_grade"] + student["social_studies_grade"] + student["science_grade"]) / 4 
    return average

def print_students_list(students):
    print("Student List:")
    for i, student in enumerate(students, start=1):
        print(f"- Student: {i} \n\tName: {student['name']}, \n\tSection: {student['section']}, \n\tSpanish grade: {student['spanish_grade']}, \n\tEnglish grade: {student['english_grade']}, \n\tSocial studies grade: {student['social_studies_grade']}, \n\tScience grade: {student['science_grade']}")

def print_students_with_averages(students):
    print("Student List with Average:")
    total_averages = 0
    for i, student in enumerate(students, start=1):
        average = get_average_grade(student)
        total_averages += average
        print(f"\t{i}. {student['name']} - Section: {student['section']} - Average: {average:.2f}")
    
    overall_average = total_averages / len(students)
    print(f"\tOverall Average: {overall_average:.2f}")

def reprobed_students(students):    
    print("Failed Students List:")
    reprobed = False
    for student in students:   
        grades = {
            "Spanish": student["spanish_grade"],
            "English": student["english_grade"],
            "Social Studies": student["social_studies_grade"],
            "Science": student["science_grade"]
        }     
        for key, value in grades.items():
            if value < 60:
                print(f"\t- Student: {student['name']} - Section: {student['section']} - Subject: {key} - Grade: {value}")
                reprobed = True
    if not reprobed:
        print("No failed students.")


def print_top_students(students, top_n=3):
    students_with_averages = [(student, get_average_grade(student)) for student in students]
    sorted_students = sorted(students_with_averages, key=lambda x: x[1], reverse=True)
    top_students = sorted_students[:top_n]

    print(f"Top {top_n} Students by Average:")
    for i, (student, average) in enumerate(top_students, start=1):
        print(f"\t{i}. {student['name']} - Section: {student['section']} - Average: {average:.2f}")

def view_top_students(students):
        
    try:               
        if len(students) == 0:
            print("No registered students.")
            return

        print_top_students(students)
    
    except Exception as e:
        print(f"Error getting the student list: {e}")
        return

    

def view_students(students):    

    try:            
        if len(students) == 0:
            print("No registered students.")
            return

        print_students_list(students)
        
    except Exception as e:
        print(f"Error getting the student list: {e}")
        return

def view_reprobed_students(students):
    try:              
        if len(students) == 0:
            print("No registered students.")
            return

        reprobed_students(students)

    except Exception as e:
        print(f"Error getting the student list: {e}")
        return

def view_students_with_averages(students):
    
    try:    
        if len(students) == 0:
            print("No registered students.")
            return

        print_students_with_averages(students)
        
    except Exception as e:
        print(f"Error getting the student list: {e}")
        return