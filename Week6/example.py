from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    @abstractmethod
    def move(self):
        pass

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")


class Car(Vehicle):
    def __init__(self, name, color, price, wheels):
        Vehicle.__init__(self, name, color, price)
        self.wheels = wheels

    def move(self):
        print("Car is moving")

    def print_information(self):
        super().print_information()
        print(f"Wheels: {self.wheels}")


class Ship(Vehicle):
    def __init__(self, name, color, price, tubin):
        Vehicle.__init__(self, name, color, price)
        self.tubin = tubin

    def move(self):
        print("Ship is moving")

    def print_information(self):
        super().print_information()
        print(f"Tubin: {self.tubin}")


class Special_Car(Car, Ship):
    def __init__(self, name, color, price, wheels, tubin):
        Car.__init__(self, name, color, price, wheels)
        Ship.__init__(self, name, color, price, tubin)

    def move(self):
        super().move()

    def print_information(self):
        super().print_information()


bmw = Car("BMW", "Black", 400, 4)
bmw.print_information()
bmw.move()
print("-----------------------------")
warship = Ship("Warship", "White", 400, 4)
warship.print_information()
warship.move()
print("-----------------------------")
spc = Special_Car("SPC", "Black", 400, 4, 2)
spc.print_information()
spc.move()
