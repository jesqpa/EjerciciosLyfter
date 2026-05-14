def export_students_to_csv(students, file_path):
    import csv

    try:           
        if len(students) == 0:
            print("No registered students to export.")
            return  
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            headers = ["name", "section", "spanish_grade", "english_grade", "social_studies_grade", "science_grade"]
            writer = csv.DictWriter(csv_file, headers)
            writer.writeheader()            
            for student in students:
                writer.writerow(student)

        print(f"CSV file created successfully: {file_path}")
        
    except Exception as e:
        print(f"Error exporting students: {e}")
