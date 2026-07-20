

def add_students(students):

    from actions.validators import validate_name, validate_section, validate_grade, validate_not_duplicate, validate_number_of_students
    num_students = validate_number_of_students("How many students do you want to add? >>> ")
    
    try:
        for i in range(num_students):            

            name = validate_name(f"Full name of student {i + 1}: >>> ")
            section = validate_section(f"Student section: >>> ")
            spanish_grade = validate_grade(f"Spanish grade: >>> ")
            english_grade = validate_grade(f"English grade: >>> ")
            social_studies_grade = validate_grade(f"Social studies grade: >>> ")
            science_grade = validate_grade(f"Science grade: >>> ")
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
            
    except ValueError as error:
        print(f"Error: {error}. ")