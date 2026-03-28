from person import Person

class Student(Person):
    students = []
    def __init__(self, name, surname, course = None):
        super().__init__("Student UNITS", name, surname)
        self.course = course or []
        Student.students.append(self)
    
    def saluta(self):
        return super().saluta() + f""" > follow the courses {self.course}"""