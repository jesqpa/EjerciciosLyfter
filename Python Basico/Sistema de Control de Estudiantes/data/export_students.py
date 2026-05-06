def export_students_to_csv(file_path):
    import csv

    try:
        from data.students import get_students
        students = get_students()   
        if len(students) == 0:
            print("No hay estudiantes registrados para exportar.")
            return  
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            headers = ["name", "section", "spanish_grade", "english_grade", "social_studies_grade", "science_grade"]
            writer = csv.DictWriter(csv_file, headers)
            writer.writeheader()            
            for student in students:
                writer.writerow(student)

        print(f"Archivo CSV creado exitosamente: {file_path}")
        
    except Exception as e:
        print(f"Error al importar estudiantes: {e}")
