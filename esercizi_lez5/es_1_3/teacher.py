from person import Person
from student import Student

class Teacher(Person):
    teachers = []
    def __init__(self, name, surname, course = None):
        super().__init__("Teacher UNITS", name, surname)
        self.course = course or []
        Teacher.teachers.append(self)
    
    def saluta(self):
        return super().saluta() + f""" > Teacher of courses {self.course}"""
    
    def teach_all_subject(self, studente : Student):
        return all(course in self.course for course in studente.course)