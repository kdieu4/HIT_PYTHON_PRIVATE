from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def chuVi(self):
        pass

    def print_information(self):
        print(f"Diện tích: {self.size()}")
        print(f"Chu vi: {self.chuVi()}")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def size(self):
        return self.width * self.height

    def chuVi(self):
        return 2 * (self.width + self.height)


h1 = Rectangle(100, 200)
h1.print_information()


class ComputeSum:
    @staticmethod
    def compute_sum(*args):
        return sum(args)


print(ComputeSum.compute_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(ComputeSum.compute_sum(1, 2, 3, 4, 5))
