def import_students_from_csv(students, file_path):
    import csv
    from actions.validators import validate_not_duplicate

    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            imported_count = 0

            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish_grade": float(row["spanish_grade"]),
                    "english_grade": float(row["english_grade"]),
                    "social_studies_grade": float(row["social_studies_grade"]),
                    "science_grade": float(row["science_grade"])
                }

                if validate_not_duplicate(students, student):
                    students.append(student)
                    imported_count += 1

        if imported_count > 0:
            print(f"Imported {imported_count} students from {file_path}.")
        else:
            print(f"No new students were imported from {file_path}.")
        
    except Exception as e:
        print(f"Error importing students: {e}")