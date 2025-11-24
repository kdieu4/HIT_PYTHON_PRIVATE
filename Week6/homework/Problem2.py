class Student:
    def __init__(self, name: str, yob: int, grade: str):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self) -> None:
        print(f"Student name: {self.name}")
        print(f"Student yob: {self.yob}")
        print(f"Student grade: {self.grade}\n")


class Teacher:
    def __init__(self, name: str, yob: int, subject: str):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self) -> None:
        print(f"Teacher name: {self.name}")
        print(f"Teacher yob: {self.yob}")
        print(f"Teacher subject: {self.subject}\n")


class Doctor:
    def __init__(self, name: str, yob: int, specialist: str):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self) -> None:
        print(f"Doctor name: {self.name}")
        print(f"Doctor yob: {self.yob}")
        print(f"Doctor specialist: {self.specialist}\n")


class Ward:
    def __init__(self, name, persons: list = None):
        if persons is None:
            persons = list()
        self.name = name
        self.persons = persons

    def add_person(self, person):
        self.persons.append(person)

    def describe(self) -> None:
        print(f"Ward name: {self.name}")
        for (i, person) in enumerate(self.persons):
            person.describe()

    def count_doctor(self) -> int:
        return sum(1 for p in self.persons if isinstance(p, Doctor))

    def sort_age(self):
        self.persons.sort(key=lambda p: p.yob, reverse=True)

    def avg_teacher_yob(self) -> float:
        total = sum(p.yob for p in self.persons if isinstance(p, Teacher))
        cnt = sum(1 for p in self.persons if isinstance(p, Teacher))
        return total / cnt


ward1 = Ward("Thuan Thanh")
ward1.add_person(Student("Dang Phuong Anh", 2006, "12"))
ward1.add_person(Teacher("Nguyen Van An", 1998, "Math"))
ward1.add_person(Teacher("Tran Phung Anh", 1996, "Literature"))
ward1.add_person(Doctor("Le Thanh Long", 1991, "Surgery"))
ward1.add_person(Doctor("Hoang Thi Giang", 1994, "Internal medicine"))

ward1.describe()
print(f"The number of doctor in {ward1.name} is {ward1.count_doctor()}")
ward1.sort_age()
ward1.describe()
print(f"\nAverage teacher yob: {ward1.avg_teacher_yob()}")