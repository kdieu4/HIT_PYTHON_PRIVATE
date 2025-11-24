class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __introduce(self):
        print(f"Tên tôi là {self.__name}, năm nay tôi {self.__age} tuổi")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Tên không thể để trống!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Tuổi không thể nhỏ hơn hoặc bằng không!")


class Student(Person):
    gender = "female"

    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        # super()._introduce()
        print(f"Tôi là sinh viên trường {self.school}")

    def information(self):
        print(f"Tên: {super().get_name()}, trường: {self.school}")


person_1 = Person("Đặng Phương Anh", 20)
person_2 = Person("Nguyễn Phương Anh", 19)

# person_1._introduce()
# person_2._introduce()

# print(Student.gender)
student_1 = Student("Nguyễn Thanh Tú", 21, "HaUI")
student_1.introduce()
student_1.information()

student_1.set_name("Nguyễn Thanh Tùng")
student_1.introduce()
student_1.information()

student_1.age = 60
print(student_1.age)


class ClassA:
    def print_information(self):
        print("Xin chào mọi người")


class ClassB(ClassA):
    def print_information(self):
        print("Hello everyone!")


class ClassC(ClassA):
    def print_information(self):
        super().print_information()


class ClassD(ClassB, ClassC):
    def print_information(self):
        # super().print_information()
        pass


C = ClassC()
C.print_information()

D = ClassD()
D.print_information()

# print(D.mro)
