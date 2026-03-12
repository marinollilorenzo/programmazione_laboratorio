from person import Person

class Student(Person):

    def __init__(self, name, surname, course = None):
        super().__init__("Student UNITS", name, surname)
        if course is None:
            self.course = []
        else:
            self.course = course
    
    def saluta(self):
        return super().saluta() + f""" > follow the courses {self.course}"""