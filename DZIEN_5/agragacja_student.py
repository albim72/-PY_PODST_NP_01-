class Student:
    def __init__(self,imie,nazwisko,id_stud):
        self.imie = imie
        self.nazwisko = nazwisko
        self.id_stud = id_stud

class Uniwersytet:
    def __init__(self,nazwa_uczelni):
        self.nazwa_uczelni = nazwa_uczelni
        self.studenci = []

    def dodaj_studenta(self,student):
        self.studenci.append(student)

    def print_studenci(self):
        print(f"Studenci uczelni: {self.nazwa_uczelni}\n")
        for student in self.studenci:
            print(f" -> student {student.imie} {student.nazwisko} - id: {student.id_stud}")


student1 = Student(imie="Alicja",nazwisko="Nowak", id_stud=467)
student2 = Student(imie="Marek",nazwisko="Bryś", id_stud=743)

print(student1)
print(student2)


univ = Uniwersytet(nazwa_uczelni="Uniwersytet Marii Curie-Skłodowskiej w Lublinie")
univ.dodaj_studenta(student1)
univ.dodaj_studenta(student2)

univ.print_studenci()



