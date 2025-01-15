from dataclasses import dataclass

@dataclass
class Student:
    jmeno : str

class Skupina:
    def __init__(self):
        self.studenti = []

    def pridej_studenta(self, student):
        self.studenti.append(student)

albert = Student("Albert")
sk4084 = Skupina()
sk4084.pridej_studenta(albert)
from copy import deepcopy
export_studentu = deepcopy( sk4084.studenti )
print(f"id(sk4084.studenti) je: {id(sk4084.studenti)}")
print(f"id(export_studentu) je: {id(export_studentu)}")
export_studentu.append(Student("Jura"))
print(sk4084.studenti) #DOTAZ - bude tam Jura nebo ne???