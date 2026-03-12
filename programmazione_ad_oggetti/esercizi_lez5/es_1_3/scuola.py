from student import Student
from teacher import Teacher



def all_subject_are_teach(studenti : list, professori : list):

    for studente in studenti:
        for course in studente.course:
            boolean = False
            for professore in professori:
                if course in professore.course:
                    boolean = True
            if not boolean:
                return False
    return True        




irene = Student("Irene", "Rossi", ["Algebra Lineare", "Analisi 2"])
matteo = Teacher("Matteo", "Gallet", ["Algebra Lineare", "Analisi 2", "Analisi 1"])

studenti = [irene, Student("x", "x", ["Analisi 1", "Analisi 2"]), Student("y", "y", ["Algebra Lineare", "Analisi 1"])]
professori = [matteo, Teacher("z", "z", ["Analisi 1"])]

print(f"Il professore/ssa {matteo.nome} {matteo.cognome} " + ("insegna" if matteo.teach_all_subject(studente=irene) else "non insegna") + f" allo/a studente/ssa {irene.nome} {irene.cognome}")

print(("Tutti" if all_subject_are_teach(studenti=studenti, professori=professori) else "Non tutti") + " i corsi degli studenti sono coperti dai professori")