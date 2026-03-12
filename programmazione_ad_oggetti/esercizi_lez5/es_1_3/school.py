from student import Student
from teacher import Teacher

def all_subject_are_teach(students : list, teachers : list):
    return all(any(teacher.teach_all_subject(student) for teacher in teachers) for student in students)

#Students
irene = Student("Irene", "Rossi", ["Algebra Lineare", "Analisi 2"])
Student("x", "x", ["Analisi 1", "Analisi 2"])
Student("y", "y", ["Algebra Lineare", "Analisi 1"])

#Teachers
matteo = Teacher("Matteo", "Prof", ["Algebra Lineare", "Analisi 2", "Analisi 1"])
Teacher("z", "z", ["Analisi 1"])

print(f"Il professore/ssa {matteo.nome} {matteo.cognome} " + ("insegna" if matteo.teach_all_subject(studente=irene) else "non insegna") + f" allo/a studente/ssa {irene.nome} {irene.cognome}")

print(("Tutti" if all_subject_are_teach(students=Student.students, teachers=Teacher.teachers) else "Non tutti") + " i corsi degli studenti sono coperti dai professori")