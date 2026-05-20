class Student():
    def __init__(self, name, section, spanish_grade, english_grade, social_studies_grade,science_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade

    def average(self):
        return (
            self.spanish_grade
            + self.english_grade
            + self.social_studies_grade
            + self.science_grade
        ) / 4

    def grades(self):
        return {
            "Spanish": self.spanish_grade,
            "English": self.english_grade,
            "Social Studies": self.social_studies_grade,
            "Science": self.science_grade,
        }

    def failed_subjects(self, threshold=60):
        failed = []
        for subj, grade in self.grades().items():
            if grade < threshold:
                failed.append((subj, grade))
        return failed

    def transform_to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_studies_grade": self.social_studies_grade,
            "science_grade": self.science_grade,
        }

    def __str__(self):
        return f"{self.name} (Section: {self.section})"