class Student:
    def __init__(self,imie,nazwisko,id_stud):
        self.imie = imie
        self.nazwisko = nazwisko
        self.id_stud = id_stud



student1 = Student(imie="Alicja",nazwisko="Nowak", id_stud=467)
student2 = Student(imie="Marek",nazwisko="Bryś", id_stud=743)

print(student1)
print(student2)



