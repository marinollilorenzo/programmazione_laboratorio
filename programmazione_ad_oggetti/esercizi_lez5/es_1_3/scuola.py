from student import Student
from teacher import Teacher


irene = Student("Irene", "Rossi", ["Algebra Lineare", "Analisi 2"])
matteo = Teacher("Matteo", "Gallet", ["Algebra Lineare", "Analisi 2", "Analisi 1"])

print(f"Il professore/ssa {matteo.nome} {matteo.cognome} " + ("insegna" if matteo.teach_all_subject(studente=irene) else "non insegna") + f" allo/a studente/ssa {irene.nome} {irene.cognome}")