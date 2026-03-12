from person import Person
from student import Student

class Teacher(Person):

    def __init__(self, name, surname, course = None):
        super().__init__("Teacher UNITS", name, surname)
        if course is None:
            self.course = []
        else:
            self.course = course
    
    def saluta(self):
        return super().saluta() + f""" > Teacher of courses {self.course}"""
    
    def teach_all_subject(self, studente : Student):
        for course in studente.course:
            if course not in self.course:
                return False
        return True