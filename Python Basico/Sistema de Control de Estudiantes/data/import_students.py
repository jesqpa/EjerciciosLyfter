def import_students_from_csv(file_path):
    import csv

    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            students = []
            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish_grade": float(row["spanish_grade"]),
                    "english_grade": float(row["english_grade"]),
                    "social_studies_grade": float(row["social_studies_grade"]),
                    "science_grade": float(row["science_grade"])
                }
                students.append(student)

        from data.students import set_students
        set_students(students)
        print(f"CSV file imported successfully: {file_path}")
        
    except Exception as e:
        print(f"Error importing students: {e}")